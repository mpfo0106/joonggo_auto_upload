from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException
import time


class NaverLogin:
    def __init__(self, driver, user_id, user_pw):
        self.driver = driver
        self.id = user_id
        self.pw = user_pw
        self.wait = WebDriverWait(self.driver, 10)

    def login(self):
        self.driver.get("https://cafe.naver.com/joonggonara")
        login_btn = self.driver.find_element(By.ID, "gnb_login_button")
        try:
            login_btn.click()
        except ElementNotInteractableException:
            return
        time.sleep(0.5)
        self.driver.execute_script(
            f"document.getElementsByName('id')[0].value='{self.id}'"
        )
        time.sleep(1)
        self.driver.execute_script(
            f"document.getElementsByName('pw')[0].value='{self.pw}'"
        )
        time.sleep(1)
        login_maintain = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='keep']"))
        )
        login_maintain.click()
        self.driver.find_element(By.ID, "log.login").click()
