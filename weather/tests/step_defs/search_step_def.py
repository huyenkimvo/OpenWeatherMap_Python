from helpers.custom_log import CustomLog
from weather.pages.search_page import SearchPage
from selenium.webdriver.remote.webdriver import WebDriver

logger = CustomLog()


class SearchStepDef:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.search_page = SearchPage(driver)

    def verify_search_results_display_correctly(self, expected_result):
        self.search_page.search_results_ready.visibility_of_element_located()
        result_elements = self.search_page.city_lnk_list.get_web_elements()
        if expected_result is None:
            assert len(result_elements) == 0, 'The search results should be empty.'
        else:
            for element in result_elements:
                city_name = element.text
                assert expected_result in city_name, f'The search results are incorrect. Expected result: "{expected_result}". Actual result: "{city_name}".'
        logger.debug('Verified search results is display correctly.')
                
