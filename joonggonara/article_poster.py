from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import random
import os

from config import PROJECT_ROOT, IMAGES_DIR


class ArticlePoster:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def post_article(self, row):
        self._select_category(row["카테고리"])
        self._switch_to_frame_and_write()
        self._input_product_info(row)
        self._input_quality_status(row["상품상태"])
        self._input_payment_and_delivery_info(row["배송방법"])
        self._attach_image(row["디렉토리명"])
        self._input_content(row["본문"])
        self._submit_post()

    def _select_category(self, category):
        categories = {
            "공연": "menuLink1285",
            "연극": "menuLink1285",
            "영화": "menuLink1285",
            "스포츠": "menuLink1286",
            "남성패션": "menuLink358",
            "남성잡화": "menuLink358",
        }
        category_element_id = categories.get(category)
        self.driver.find_element(By.ID, category_element_id).click()

    def _switch_to_frame_and_write(self):
        self.driver.switch_to.frame("cafe_main")
        write_form_btn = self.wait.until(
            EC.element_to_be_clickable((By.ID, "writeFormBtn"))
        )
        write_form_btn.click()

    def _input_product_info(self, row):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(1)
        product_input = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "textarea_input"))
        )
        product_input.send_keys(row["상품명"])
        price_input = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "input_text"))
        )
        price_input.send_keys(int(row["판매가격"]))

    def _input_quality_status(self, product_condition):
        quality_status_mapping = {
            "미개봉": 1,
            "거의새것": 2,
            "사용감있음": 3,
        }
        quality_status = quality_status_mapping.get(product_condition)
        self.driver.find_element(By.ID, f"quality{quality_status}").click()

    def _input_payment_and_delivery_info(self, delivery_method):
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='deal1']"))
        ).click()
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='deal2']"))
        ).click()

        delivery_status_mapping = {
            "직거래": 0,
            "택배거래": 1,
            "온라인전송": 2,
        }
        delivery_status = delivery_status_mapping.get(delivery_method)
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f'//label[@for="delivery{delivery_status}"]')
            )
        ).click()

        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='agree1']"))
        ).click()
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='agree2']"))
        ).click()

    def _attach_image(self, directory_name):
        image_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[@data-name="image"]'))
        )

        # 이미지가 저장된 디렉토리 경로 생성
        image_directory = os.path.join(PROJECT_ROOT, IMAGES_DIR, directory_name)

        # 디렉토리 내의 이미지 파일 목록 가져오기
        image_files = [
            f
            for f in os.listdir(image_directory)
            if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))
        ]

        # 각 이미지마다 첨부 버튼 클릭 및 창 닫기 반복
        for _ in image_files:
            image_button.click()
            time.sleep(2)
            os.system(
                """osascript -e 'tell application "System Events" to keystroke "w" using command down' """
            )
            time.sleep(1)

        # 모든 hidden-file 요소 찾기
        input_file_elements = self.driver.find_elements(
            By.CSS_SELECTOR, "input[type='file'][id^='hidden-file']"
        )

        for i, image_file in enumerate(image_files):
            full_image_path = os.path.join(image_directory, image_file)
            if os.path.exists(full_image_path):
                if i < len(input_file_elements):
                    input_file_elements[i].send_keys(full_image_path)
                else:
                    print(
                        f"Warning: Not enough file input elements for image - {full_image_path}"
                    )
                time.sleep(random.uniform(2, 4))
            else:
                print(f"Warning: Image file not found - {full_image_path}")

        time.sleep(random.uniform(8, 10))

    def _input_content(self, content):
        webdriver.ActionChains(self.driver).send_keys(content).perform()
        time.sleep(random.uniform(4, 8))

    def _submit_post(self):
        self.driver.find_element(
            By.XPATH, '//a[@role="button"][contains(@class, "BaseButton")]'
        ).click()
        time.sleep(random.uniform(3, 5))
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(random.uniform(10, 40))
