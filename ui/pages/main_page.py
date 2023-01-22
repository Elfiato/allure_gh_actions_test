import allure

from ui.pages.base_page import BasePage
from ui.locators.basic_locators import MainPageLocators, PicturePageLocators
from selenium.webdriver.common.keys import Keys
from ui.pages.result_page import ResultPage
from ui.pages.picture_page import PicturePage


class MainPage(BasePage):
    locators = MainPageLocators()

    def search_text(self, text):
        with allure.step(f'Ввод текста {text} в поле поиска.'):
            self.input_text(*self.locators.SEARCH_TEXT_FORM, text, self.get_clickable_element)
        with allure.step(f'Проверка, что отображается окно всплывающих подсказок.'):
            self.is_element_visible(*self.locators.SUGGEST)
        with allure.step(f'Нажатие на кнопку поиск.'):
            self.get_clickable_element(*self.locators.SEARCH_TEXT_FORM).send_keys(Keys.ENTER)
        return ResultPage(driver=self.driver)

    @allure.step('Переход на страницу картинок с главной страницы.')
    def go_to_picture_page(self):
        with allure.step('Нажатие на кнопку всех сервисов.'):
            self.get_clickable_element(*self.locators.ALL_SERVICES).click()
        with allure.step('Нажатие на кнопку картинок.'):
            self.get_clickable_element(*self.locators.PICTURE_SECTION).click()
        self.switch_to_next_window()
        return PicturePage(driver=self.driver)
