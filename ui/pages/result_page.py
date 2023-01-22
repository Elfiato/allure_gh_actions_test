import allure

from ui.pages.base_page import BasePage
from ui.locators.basic_locators import ResultPageLocators


class ResultPage(BasePage):
    locators = ResultPageLocators()

    def is_requirement_url_in_first_link(self, req_url):
        with allure.step(f"Проверка, что первый результат выдачи имеет ссылку: {req_url}"):
            if self.is_element_present(*ResultPageLocators.SEARCH_RES):
                link = self.get_present_element(*self.locators.FIRST_SEARCH_RESULT)
                assert req_url in link.get_attribute("href"), f'Первая ссылка не ведет на {req_url}.'
            else:
                assert False, 'Результаты поиска не найдены.'
