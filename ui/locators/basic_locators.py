from selenium.webdriver.common.by import By


class MainPageLocators:
    SEARCH_TEXT_FORM = (By.CSS_SELECTOR, "#text")
    SUGGEST = (By.XPATH, '//*[contains(@id, "suggest-list")]')
    ALL_SERVICES = (By.CSS_SELECTOR, ".services-pinned__content a")
    PICTURE_SECTION = (By.CSS_SELECTOR, ".services-more-popup__section a:nth-child(15)")


class ResultPageLocators:
    SEARCH_RES = (By.CSS_SELECTOR, '#search-result')
    FIRST_SEARCH_RESULT = (By.CSS_SELECTOR, '#search-result > .serp-item:nth-child(3) a.OrganicTitle-Link')


class PicturePageLocators:
    FIRST_CATEGORY_URL = (By.CSS_SELECTOR, '.PopularRequestList-Item_pos_0 a.Link')
    FIRST_CATEGORY = (By.CSS_SELECTOR, '.PopularRequestList-Item_pos_0')
    PICTURE_MAIN_ICON = (By.CSS_SELECTOR, 'a.home-link[data-id="images"]')
    PICTURE_SEARCH_STR = (By.CSS_SELECTOR, '.search2__input .input__box .input__control')
    FIRST_PICTURE_IN_SEARCH = (By.CSS_SELECTOR, '.serp-list_type_search .serp-item:nth-child(4) a')
    OPENED_PICTURE = (By.CSS_SELECTOR, '.MMImage-Origin')
    NEXT_BUTTON = (By.CSS_SELECTOR, '.CircleButton_type_next')
    PREV_BUTTON = (By.CSS_SELECTOR, '.CircleButton_type_prev')
