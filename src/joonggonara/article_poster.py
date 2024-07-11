import os
import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from config import CATEGORIES, QUALITY_STATUS, DELIVERY_STATUS
from config.timings import *
from src.handlers.image_handler import ImageHandler
from src.handlers.web_element_handler import WebElementHandler
from src.utils.logger import setup_logger


class ArticlePoster:
    def __init__(self, driver):
        self.driver = driver
        self.web_handler = WebElementHandler(driver)
        self.logger = setup_logger("article_poster", "logs/article_poster.log")

    def post_article(self, row):
        try:
            self.logger.info(f"Started posting article: {row['상품명']}")
            self._select_category(row["카테고리"])
            self._switch_to_frame_and_write()
            self._input_product_info(row)
            self._input_quality_status(row["상품상태"])
            self._input_payment_and_delivery_info(row["배송방법"])
            self._attach_image(row["디렉토리명"])
            self._input_content(row["본문"])
            self._submit_post()
            self.logger.info(f"Successfully posted article: {row['상품명']}")
        except Exception as e:
            self.logger.error(f"Error posting article {row['상품명']}: {str(e)}")

    def _select_category(self, category):
        category_element_id = CATEGORIES.get(category)
        if category_element_id:
            self.web_handler.click_element((By.ID, category_element_id))
        else:
            self.logger.warning(f"Category '{category}' not found in CATEGORIES")

    def _switch_to_frame_and_write(self):
        self.web_handler.switch_to_frame("cafe_main")
        self.web_handler.click_element((By.ID, "writeFormBtn"))

    def _input_product_info(self, row):
        self.web_handler.switch_to_window(-1)
        time.sleep(1)
        self.web_handler.input_text((By.CLASS_NAME, "textarea_input"), row["상품명"])
        self.web_handler.input_text(
            (By.CLASS_NAME, "input_text"), str(int(row["판매가격"]))
        )

    def _input_quality_status(self, product_condition):
        quality_status = QUALITY_STATUS.get(product_condition)
        if quality_status:
            self.web_handler.click_element((By.CSS_SELECTOR, f"label[for='quality{quality_status}']"))
        else:
            self.logger.warning(
                f"Quality status '{product_condition}' not found in QUALITY_STATUS"
            )

    def _input_payment_and_delivery_info(self, delivery_method):
        self.web_handler.click_element((By.CSS_SELECTOR, "label[for='deal1']"))
        self.web_handler.click_element((By.CSS_SELECTOR, "label[for='deal2']"))

        delivery_status = DELIVERY_STATUS.get(delivery_method)
        if delivery_status is not None:
            self.web_handler.click_element(
                (By.XPATH, f'//label[@for="delivery{delivery_status}"]')
            )
        else:
            self.logger.warning(
                f"Delivery method '{delivery_method}' not found in DELIVERY_STATUS"
            )

        self.web_handler.click_element((By.CSS_SELECTOR, "label[for='agree1']"))
        self.web_handler.click_element((By.CSS_SELECTOR, "label[for='agree2']"))

    def _attach_image(self, directory_name):
        image_button = (By.XPATH, '//button[@data-name="image"]')
        image_files = ImageHandler.get_image_files(directory_name)

        for _ in image_files:
            self.web_handler.click_element(image_button)
            time.sleep(CLICK_DELAY)
            os.system(
                """osascript -e 'tell application "System Events" to keystroke "w" using command down' """
            )
            time.sleep(1)

        input_file_elements = self.driver.find_elements(
            By.CSS_SELECTOR, "input[type='file'][id^='hidden-file']"
        )

        for i, image_file in enumerate(image_files):
            if i < len(input_file_elements):
                input_file_elements[i].send_keys(image_file)
                time.sleep(random.uniform(*UPLOAD_DELAY))
            else:
                self.logger.warning(
                    f"Not enough file input elements for image - {image_file}"
                )

        time.sleep(random.uniform(*UPLOAD_DELAY))

    def _input_content(self, content):
        webdriver.ActionChains(self.driver).send_keys(content).perform()
        time.sleep(random.uniform(*UPLOAD_DELAY))

    def _submit_post(self):
        self.web_handler.click_element(
            (By.XPATH, '//a[@role="button"][contains(@class, "BaseButton")]')
        )
        time.sleep(random.uniform(*POST_DELAY))
        self.web_handler.switch_to_window(0)
        time.sleep(random.uniform(*FINAL_DELAY))
