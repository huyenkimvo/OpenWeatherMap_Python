from helpers.custom_log import CustomLog
from weather.pages.dashboard_page import DashboardPage
from selenium.webdriver.remote.webdriver import WebDriver

logger = CustomLog()


class DashboardStepDef:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.dashboard_page = DashboardPage(driver)

    def navigate_to_the_url(self, url):
        self.driver.maximize_window()
        self.driver.get(url)
        logger.debug(f'Navigated to {url}.')

    def wait_for_loading_to_disappear(self):
        self.dashboard_page.dashboard_loading.invisibility_of_element_located()
 
    def verify_search_box_is_display(self):
       assert self.dashboard_page.search_txt.is_visible(), 'The Search box is NOT display.'

    def enter_search_key(self, search_key):
        self.dashboard_page.search_txt.set_text(search_key)
        self.dashboard_page.search_txt.press_enter()
        logger.debug(f'Inputted {search_key} into Search text box and pressed enter.')


