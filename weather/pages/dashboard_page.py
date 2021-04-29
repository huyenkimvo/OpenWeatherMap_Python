from selenium.webdriver.common.by import By
from helpers.base_page import BasePage, Control


class DashboardPage(BasePage):
    search_txt: Control = (By.XPATH, "//div[@id = 'desktop-menu']//input[@type = 'text']")
    dashboard_loading: Control = (By.XPATH, "//div[contains(@class, 'owm-loader-container')]/div[@aria-label = 'Loading']")
