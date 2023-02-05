import time
from YandexPages import SearchHelper
from selenium.webdriver.common.keys import Keys
from urllib.parse import unquote


def test_yandex_search(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    assert yandex_main_page.check_search_field()

    yandex_main_page.enter_word("Тензор")
    assert yandex_main_page.check_suggest()

    yandex_main_page.enter_word(Keys.ENTER)
    if yandex_main_page.captcha_button():
        yandex_main_page.captcha_button().click()
    assert yandex_main_page.search_elements()

    link = yandex_main_page.first_link()
    assert link == "https://tensor.ru/"


def test_yandex_pictures(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.enter_word("Тензор")
    yandex_main_page.enter_word(Keys.ENTER)
    if yandex_main_page.captcha_button():
        yandex_main_page.captcha_button().click()
    images_button = yandex_main_page.check_images_button()
    assert "Картинки" == images_button.text

    images_button.click()
    yandex_main_page.driver.switch_to.window(yandex_main_page.driver.window_handles[1])
    assert 'https://yandex.ru/images/' in yandex_main_page.driver.current_url

    yandex_images_page = yandex_main_page
    yandex_images_page.driver.get('https://yandex.ru/images/')
    first_category_name = yandex_images_page.find_first_category().text
    yandex_images_page.find_first_category().click()
    time.sleep(4)
    assert first_category_name in unquote(yandex_images_page.driver.current_url)

    yandex_images_page.find_first_image().click()
    first_main_image = yandex_images_page.driver.current_url
    time.sleep(1)
    yandex_images_page.button_next_image().click()
    time.sleep(1)
    second_main_image = yandex_images_page.driver.current_url
    assert first_main_image != second_main_image

    yandex_images_page.button_prev_image().click()
    time.sleep(1)
    assert first_main_image in yandex_images_page.driver.current_url
