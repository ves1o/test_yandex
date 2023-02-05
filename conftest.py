import pytest
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ['enable-automation'])


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path="/Users/anastasiia/PycharmProjects/test_yaru/driver/chromedriver",
                              options=options)
    yield driver
    driver.quit()
