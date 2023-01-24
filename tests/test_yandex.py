import allure
import pytest
from _pytest.fixtures import FixtureRequest

from base import BaseCase
from searched_data import TEXT, URL


@pytest.mark.UI
class TestUISearch(BaseCase):
    @allure.title("Тест поиска.")
    @allure.description(
        """
        Тест на наличие ссылки на сайт компании в первом результате поиска Яндекс по запросу ее названия.
        В файле searched_data.py, в переменных TEXT и URL хранятся название компании и ее сайт,
        проверяемый в результатах поиска.
        Тест-кейс:
        1. Открытие главной страницы Яндекс;
        2. Ввод названия компании в поисковую строку;
        3. Проверка, что появилось таблица с подсказками;
        4. Поиск по запросу;
        5. Проверка на наличие сайта компании в первом результате выдачи.
        """
    )
    # @pytest.mark.xfail(reason="Открывается страница с капчей при использовании Selenium Webdriver.")
    def test_search_site_in_search_engine(self, request: FixtureRequest):
        with allure.step("Открытие главное страницы Яндекс."):
            main_page = request.getfixturevalue('main_page')
            main_page.is_opened()
        result_page = main_page.search_text(TEXT)
        result_page.is_requirement_url_in_first_link(URL)


@pytest.mark.UI
class TestUIPicture(BaseCase):
    @allure.title("Тест переключения картинок.")
    @allure.description(
        """
        Тест на корректную работу кнопок 'вперед' и 'назад' при перелистывании картинок в 'Яндекс Картинках'.
        Шаги тест-кейса:
        1. Открытие главной страницы Яндекс;
        2. Переход в категорию картинок;
        3. Открытие первой категории;
        4. Открытие первой картинки;
        5. Переход на следующую картинку;
        6. Возвращение на предыдущую картинку;
        7. Проверка на соответствие изначально открытой картинки и картинки, полученной при возвращении. 
        """
    )
    # @pytest.mark.xfail(reason="Открывается страница с капчей при использовании Selenium Webdriver.")
    def test_picture(self, request: FixtureRequest):
        with allure.step("Открытие главное страницы Яндекс."):
            main_page = request.getfixturevalue('main_page')
            main_page.is_opened()
        picture_page = main_page.go_to_picture_page()
        picture_page.is_opened()
        category_name = picture_page.go_to_first_category()
        picture_page.is_valid_search_text(category_name)
        picture_page.open_first_picture_in_search()
        picture_page.should_be_opened_picture()
        picture_page.move_to_opened_picture()
        picture_page.should_be_next_button()
        prev_picture = picture_page.open_next_picture()
        picture_page.move_to_opened_picture()
        picture_page.should_be_prev_button()
        picture_page.open_prev_picture(prev_picture)
