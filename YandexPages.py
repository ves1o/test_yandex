from BaseApp import BasePage
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as BS


class YandexSearchLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search3__button.mini-suggest__button")
    LOCATOR_YANDEX_SUGGEST = (By.CLASS_NAME, "mini-suggest__popup-content")
    LOCATOR_YANDEX_SEARCH_RESULT = (By.ID, "search-result")
    LOCATOR_YANDEX_CAPTCHA = (By.CLASS_NAME, "CheckboxCaptcha-Button")
    LOCATOR_YANDEX_FIRST_LINKS = (By.CLASS_NAME, "VanillaReact.OrganicTitle.OrganicTitle_multiline."
                                                 "Typo.Typo_text_l.Typo_line_m.organic__title-wrapper")
    LOCATOR_YANDEX_NAVIGATION_BAR = (By.CSS_SELECTOR, ".service__name")
    LOCATOR_YANDEX_IMAGES_BAR = (By.CSS_SELECTOR, ".tabs-navigation__tab-over-inner")
    LOCATOR_YANDEX_FIRST_CATEGORY = (By.CLASS_NAME, "PopularRequestList-Item.PopularRequestList-Item_pos_0")
    LOCATOR_YANDEX_FIRST_IMAGE = (By.CSS_SELECTOR, ".serp-item__preview")
    LOCATOR_YANDEX_NEXT_IMAGE_BUTTON = (By.CSS_SELECTOR, ".CircleButton_type_next")
    LOCATOR_YANDEX_PREV_IMAGE_BUTTON = (By.CSS_SELECTOR, ".CircleButton_type_prev")


class SearchHelper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_BUTTON, time=2).click()

    def check_search_field(self):
        search_field = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD, time=2)
        return search_field

    def check_suggest(self):
        suggest = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SUGGEST, time=2)
        return suggest

    def search_elements(self):
        result = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_RESULT, time=2)
        return result

    def captcha_button(self):
        try:
            captcha = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_CAPTCHA, time=2)
            return captcha

        except Exception:
            return False

    def first_link(self):
        soup = BS(self.driver.page_source, 'html.parser')
        first_link = soup.select(".VanillaReact.OrganicTitle.OrganicTitle_multiline."
                    "Typo.Typo_text_l.Typo_line_m.organic__title-wrapper")[0]

        return first_link.select_one('a')['href']

    def check_images_button(self):
        all_elements = self.find_elements(YandexSearchLocators.LOCATOR_YANDEX_NAVIGATION_BAR, time=2)
        for element in all_elements:
            if element.text == 'Картинки':
                return element
        return False

    def check_images_bar_button(self):
        all_elements = self.find_elements(YandexSearchLocators.LOCATOR_YANDEX_IMAGES_BAR, time=2)
        for element in all_elements:
            if element.text == 'Картинки':
                return element
        return False

    def find_first_category(self):
        first_category = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_FIRST_CATEGORY, time=2)
        return first_category

    def find_first_image(self):
        first_image = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_FIRST_IMAGE, time=2)
        return first_image

    def button_next_image(self):
        next_button = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_NEXT_IMAGE_BUTTON, time=2)
        return next_button

    def button_prev_image(self):
        prev_button = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_PREV_IMAGE_BUTTON, time=2)
        return prev_button
