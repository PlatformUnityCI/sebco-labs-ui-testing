import pytest
import pytest_html
import base64
from lib_core.utils.screenshots.screenshots import take_screenshot
import shutil
import os

from lib_core.drivers.web_driver import get_web_driver
from lib_core.drivers.mobile_driver import get_mobile_driver
from lib_core.pages.web_login_page import WebLoginPage


@pytest.fixture(scope="function")
def web_driver():
    driver = get_web_driver()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def mobile_driver():
    driver = get_mobile_driver()
    yield driver
    driver.quit()

@pytest.fixture
def web_login_page(web_driver):
    return WebLoginPage(web_driver)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        driver = item.funcargs.get("web_driver")

        if driver:
            name = "FAIL" if report.failed else "SUCCESS"
            path = take_screenshot(driver, name)

            with open(path, "rb") as image_file:
                encoded = base64.b64encode(image_file.read()).decode()

            extra = getattr(report, "extra", [])
            extra.append(
                pytest_html.extras.image(
                    encoded,
                    mime_type="image/png"
                )
            )
            report.extra = extra

def pytest_sessionstart(session):
    folder = "reports/screenshots"
    if os.path.exists(folder):
        shutil.rmtree(folder, ignore_errors=True)

    os.makedirs(folder, exist_ok=True)