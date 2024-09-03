import pandas as pd

import src.joonggonara
from config.env_setup import EXCEL_PATH, NAVER_ID, NAVER_PW
from config.webdriver_setup import setup_webdriver
from src.joonggonara.login import NaverLogin
from src.utils.logger import setup_logger


def main():
    logger = setup_logger("main", "logs/main.log")
    logger.info("Starting the auto upload process")

    driver = setup_webdriver()

    login_handler = NaverLogin(driver)
    login_handler.login(NAVER_ID, NAVER_PW)

    poster = src.joonggonara.JoongNaArticlePoster(driver)

    df = pd.read_excel(EXCEL_PATH)

    for _, row in df.iterrows():
        poster.post_article(row)

    driver.quit()
    logger.info("Auto upload process completed")


if __name__ == "__main__":
    main()
