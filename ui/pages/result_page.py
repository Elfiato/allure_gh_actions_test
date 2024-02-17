import allure

from ui.pages.base_page import BasePage
from ui.locators.basic_locators import ResultPageLocators


class ResultPage(BasePage):
    locators = ResultPageLocators()

    def check_search_res(self):
        assert self.is_element_present(*self.locators.SEARCH_RES), 'Результаты поиска не найдены.'

    def check_requirement_url_in_first_link(self, req_url):
        with allure.step(f"Проверка, что первый результат выдачи имеет ссылку: {req_url}"):
            self.check_search_res()
            assert req_url in self.get_present_element(*self.locators.FIRST_SEARCH_RESULT).get_attribute("href"), \
                f'Первая ссылка не ведет на {req_url}.'

    def close_modal_window(self):
        self.get_clickable_element(*self.locators.MODAL_WINDOW_CLOSE).click()
