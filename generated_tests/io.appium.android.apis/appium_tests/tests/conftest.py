import pytest
import os
import time
import base64
from dotenv import load_dotenv
from appium import webdriver
from appium.options.android import UiAutomator2Options

load_dotenv()

@pytest.fixture(scope="session")
def driver():
    server_url = os.getenv("APPIUM_SERVER_URL", "http://localhost:4723")
    options = UiAutomator2Options()
    options.platform_name = os.getenv("MOBILE_PLATFORM", "Android")
    options.device_name = os.getenv("MOBILE_DEVICE_NAME", "emulator-5554")

    # App path: only set if file exists locally AND server is local
    is_local_server = "localhost" in server_url or "127.0.0.1" in server_url
    skip_install = os.getenv("MOBILE_SKIP_APP_INSTALL", "").lower() in ("true", "1", "yes")
    app_path = os.getenv("MOBILE_APP_PATH", "")
    if app_path and is_local_server and not skip_install:
        if not os.path.isabs(app_path):
            app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", app_path))
        if os.path.isfile(app_path):
            options.app = app_path

    options.app_package = os.getenv("MOBILE_APP_PACKAGE", "io.appium.android.apis")
    options.app_activity = os.getenv("MOBILE_APP_ACTIVITY", ".ApiDemos")
    options.automation_name = os.getenv("MOBILE_AUTOMATION_NAME", "UiAutomator2")

    # App lifecycle: always start from a clean state
    reset_app = os.getenv("MOBILE_RESET_APP", "true").lower() in ("true", "1", "yes")
    options.no_reset = not reset_app
    options.force_app_launch = True
    options.should_terminate_app = True
    options.set_capability("enableNotificationListener", False)

    # Device unlock
    unlock_type = os.getenv("MOBILE_UNLOCK_TYPE", "").strip().lower()
    unlock_key = os.getenv("MOBILE_UNLOCK_KEY", "")
    if unlock_type and unlock_key:
        options.unlock_type = unlock_type
        options.unlock_key = unlock_key
        options.unlock_strategy = "uiautomator"

    # Retry session creation
    d = None
    last_err = None
    for attempt in range(1, 4):
        try:
            d = webdriver.Remote(server_url, options=options)
            break
        except Exception as e:
            last_err = e
            print(f"Session attempt {attempt}/3 failed: {e}")
            time.sleep(10)
    if d is None:
        raise last_err

    d.implicitly_wait(10)

    # Start screen recording
    try:
        d.start_recording_screen()
    except Exception as e:
        print(f"Could not start screen recording: {e}")

    yield d

    # Teardown: stop recording, save video, terminate app
    try:
        video_data = d.stop_recording_screen()
        os.makedirs("recordings", exist_ok=True)
        video_path = os.path.join("recordings", "test_recording.mp4")
        with open(video_path, "wb") as f:
            f.write(base64.b64decode(video_data))
        print(f"Screen recording saved: {video_path}")
    except Exception as e:
        print(f"Failed to save screen recording: {e}")

    try:
        app_package = os.getenv("MOBILE_APP_PACKAGE", "io.appium.android.apis")
        if app_package:
            d.terminate_app(app_package)
        d.press_keycode(3)  # HOME key
    except Exception:
        pass
    d.quit()
