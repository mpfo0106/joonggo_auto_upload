import pandas as pd
import time
import random
from config.env_setup import (
    EXCEL_PATH,
    NAVER_ID,
    NAVER_PW,
)
from config.webdriver_setup import setup_webdriver
from joonggonara.login import NaverLogin
from joonggonara.article_poster import ArticlePoster


def main():
    driver = setup_webdriver()
    naver_login = NaverLogin(driver, NAVER_ID, NAVER_PW)
    article_poster = ArticlePoster(driver)
    df = pd.read_excel(EXCEL_PATH)

    naver_login.login()
    for idx in reversed(range(len(df.index))):
        article_poster.post_article(df.iloc[idx])
        time.sleep(random.uniform(20, 50))

    driver.quit()


if __name__ == "__main__":
    while True:
        main()
        time.sleep(1800)  # 30분
