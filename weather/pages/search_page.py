from selenium.webdriver.common.by import By
from helpers.base_page import Control, BasePage

class SearchPage(BasePage):
    city_lnk_list: Control = (By.XPATH, "//div[@id = 'forecast-list']//a[contains(@href, '/city/')]")
    search_results_ready : Control = (By.XPATH, "//div[@id = 'forecast_list_ul']/*")