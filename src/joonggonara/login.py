import time

from selenium.webdriver.common.by import By

import src.utils.logger
from src.handlers.web_element_handler import WebElementHandler


class NaverLogin:
    def __init__(self, driver):
        self.driver = driver
        self.web_handler = WebElementHandler(driver)
        self.logger = src.utils.logger.setup_logger(
            "naver_login", "logs/naver_login.log"
        )

    def login(self, username, password):
        try:
            self.logger.info("Starting login process")
            self.driver.get("https://cafe.naver.com/joonggonara")
            login_btn = self.driver.find_element(By.ID, "gnb_login_button")
            login_btn.click()

            time.sleep(0.5)
            self.driver.execute_script("document.getElementById('id').value = arguments[0];", username)

            time.sleep(0.5)
            self.driver.execute_script("document.getElementById('pw').value = arguments[0];", password)

            self.web_handler.click_element((By.ID, "log.login"))
            self.logger.info("Login successful")
        except Exception as e:
            self.logger.error(f"Login failed: {str(e)}")
