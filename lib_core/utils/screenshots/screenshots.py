import os
from datetime import datetime

def take_screenshot(driver, name="screenshot"):
    folder = "reports/screenshots"
    os.makedirs(folder, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"{folder}/{name}_{timestamp}.png"

    driver.save_screenshot(path)
    return path