from appium import webdriver

def get_mobile_driver():
    desired_caps = {
        "platformName": "Android",
        "deviceName": "Android Emulator",
        "appPackage": "com.example.app",
        "appActivity": ".MainActivity",
        "automationName": "UiAutomator2"
    }

    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    return driver