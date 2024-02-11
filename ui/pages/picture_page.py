import allure

from ui.pages.base_page import BasePage
from ui.locators.basic_locators import PicturePageLocators


class PicturePage(BasePage):
    url = 'https://ya.ru/images/'
    locators = PicturePageLocators()

    @allure.step('Открытие первой категории картинок.')
    def go_to_first_category(self):
        category = self.get_visible_element(*self.locators.FIRST_CATEGORY_URL)
        category_name = self.get_visible_element(*self.locators.FIRST_CATEGORY).get_attribute(
            'data-grid-text')
        print(f'Открываем категорию: {category_name}')
        category.click()
        return category_name

    @allure.step('Проверка, что в строке поиска показан текст, совпадающий с названием категории.')
    def is_valid_search_text(self, category_name):
        search_text = self.get_visible_element(*self.locators.PICTURE_SEARCH_STR).get_attribute('value')
        print(f'В строке поиска текст: {category_name}')
        assert category_name == search_text, 'Текст в строке поиска не соответсвует названию категории'

    @allure.step('Открытие первой картинки в поиске.')
    def open_first_picture_in_search(self):
        if self.is_element_visible(*self.locators.FIRST_PICTURE_IN_SEARCH):
            self.get_visible_element(*self.locators.FIRST_PICTURE_IN_SEARCH).click()
        else:
            assert self.is_element_visible(
                *self.locators.FIRST_PICTURE_IN_SEARCH), 'Не найдено картинок доступных для открытия.'

    @allure.step('Проверка, что картинка из поиска открылась.')
    def should_be_opened_picture(self):
        assert self.is_element_present(*self.locators.OPENED_PICTURE), 'Картинка из поиска не открылась.'

    @allure.step('Открытие следующей картинки, нажатием на стрелку.')
    def open_next_picture(self):
        if self.is_element_visible(*PicturePageLocators.NEXT_BUTTON):
            prev_picture_url = self.get_present_element(*self.locators.OPENED_PICTURE)
            pic_url = prev_picture_url.get_attribute('src')
            self.get_visible_element(*self.locators.NEXT_BUTTON).click()
            print(f'Ссылка на первую открытую картинку: {pic_url}')
            return pic_url
        else:
            assert self.is_element_visible(
                *self.locators.NEXT_BUTTON), 'Кнопка открытия следующей картинки при переходе не найдена.'

    @allure.step('Открытие предыдущей картинки, нажатием на стрелку.')
    def open_prev_picture(self, prev_url):
        if self.is_element_visible(*self.locators.PREV_BUTTON):
            next_pic_url = self.get_present_element(*self.locators.OPENED_PICTURE).get_attribute('src')
            print(f'Ссылка на следующую открытую картинку: {next_pic_url}')
            self.get_visible_element(*self.locators.PREV_BUTTON).click()
            current_picture_url = self.get_present_element(*self.locators.OPENED_PICTURE)
            pic_url = current_picture_url.get_attribute('src')
            print(f'Ссылка на картинку при возвращении назад: {pic_url}')
            assert pic_url == prev_url, 'Предыдущая картинка не совпадает с запомненной.'
        else:
            assert self.is_element_visible(
                *PicturePageLocators.PREV_BUTTON), 'Кнопка открытия предыдущей картинки при переходе не найдена.'

    @allure.step('Проверка, что есть стрелка вперед.')
    def should_be_next_button(self):
        assert self.is_element_visible(
            *self.locators.NEXT_BUTTON), 'Кнопка открытия следующей картинки не найдена.'

    @allure.step('Проверка, что есть кнопка назад.')
    def should_be_prev_button(self):
        assert self.is_element_visible(
            *self.locators.PREV_BUTTON), 'Кнопка открытия предыдущей картинки не найдена.'

    @allure.step('Наведение курсора на открытую картинку.')
    def move_to_opened_picture(self):
        self.move_to_present_element(*self.locators.OPENED_PICTURE)
