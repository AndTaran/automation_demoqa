import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('log-level=3')

    print("\nstart browser..")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    yield driver
    print("\nquit browser..")
    driver.quit()
