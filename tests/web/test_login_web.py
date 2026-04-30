import pytest
import os

@pytest.mark.regression
class TestLoginWeb:
           
    def test_login_web(self, web_login_page):

        web_login_page.open()
        web_login_page.login("ads.scouto@gmail.com", os.getenv("SECRET_PASSWORD"))
        assert web_login_page.is_on_check_inbox_screen()

    def test_invalid_user(self, web_login_page):

        web_login_page.open()
        web_login_page.login("admin@gmail.com", os.getenv("SECRET_PASSWORD_ERROR"))  # dispara validación HTML
        error_text = web_login_page.get_login_error_message()
        assert "That email and password combination is incorrect." in error_text

    def test_invalid_email(self, web_login_page):

        web_login_page.open()
        web_login_page.login("admin", os.getenv("SECRET_PASSWORD_ERROR"))  # dispara validación HTML
        error = web_login_page.get_email_validation_message()
        assert "Please include an '@' in the email address" in error