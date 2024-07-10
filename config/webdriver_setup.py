from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def setup_webdriver():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument(
        "user-data-dir=/Users/kangjoon/WORKSPACE/personal/toyProject/seleniumOptions/joonggo"
    )
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    )

    service = ChromeService(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)
