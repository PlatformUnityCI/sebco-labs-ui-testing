from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebLoginPage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.figma.com/login")

    # def login(self, user, password):
    #     self.driver.find_element(By.ID, "email").send_keys(user)
    #     self.driver.find_element(By.ID, "password").send_keys(password)
    #     self.driver.find_element(By.XPATH, "//button[@type='submit' and contains(., 'Log in')]")

    def login(self, user, password):
        wait = WebDriverWait(self.driver, 10)

        email = wait.until(
            EC.visibility_of_element_located((By.ID, "email"))
        )
        email.send_keys(user)

        password_input = wait.until(
            EC.visibility_of_element_located((By.ID, "current-password"))
        )
        password_input.send_keys(password)

        login_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and contains(., 'Log in')]"))
        )
        login_btn.click()
        
    def is_logged_in(self):
        return "dashboard" in self.driver.current_url
    
    def is_on_check_inbox_screen(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//h1[contains(., 'Check your inbox')]")
                )
            )
            return True
        except:
            return False
    
    def get_login_error_message(self):
        wait = WebDriverWait(self.driver, 10)

        error = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[@role='alert']//p")
            )
        )
        return error.text
    
    def get_email_validation_message(self):
        email_input = self.driver.find_element(By.ID, "email")
        return email_input.get_attribute("validationMessage")