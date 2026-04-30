from appium.webdriver.common.appiumby import AppiumBy

class MobileLoginPage:

    def __init__(self, driver):
        self.driver = driver

    def login(self, user, password):
        self.driver.find_element(AppiumBy.ID, "user").send_keys(user)
        self.driver.find_element(AppiumBy.ID, "pass").send_keys(password)
        self.driver.find_element(AppiumBy.ID, "login").click()

    def is_logged_in(self):
        return self.driver.find_element(AppiumBy.ID, "dashboard").is_displayed()