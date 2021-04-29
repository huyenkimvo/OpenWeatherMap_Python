from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from functools import wraps
from selenium.webdriver.common.keys import Keys


class BasePage:
    __By = By.__dict__.values()

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def __getattribute__(self, attr):
        ori_attr = super().__getattribute__(attr)
        if type(ori_attr) is tuple and ori_attr[0] in self.__By:
            return Control(self.driver, ori_attr)
        return ori_attr


class Control(tuple):

    default_timeout = 60

    def __new__(cls, driver, locator):
        return super().__new__(cls, locator)

    def __init__(self, driver, locator):
        self.driver = driver

    def get_web_element(self):
        try:
            WebDriverWait(self.driver, Control.default_timeout).until(
                EC.presence_of_element_located(self)
            )
        except (StaleElementReferenceException, NoSuchElementException, TimeoutException) as error:
            raise error(
                "An exception of type " + type(e).__name__ +
                " occurred. With Element -: " + self +
                " - locator: (" + self[0] + ", " + self[1] + ")"
            )
        element = self.driver.find_element(*self)
        element._locator = self
        return element

    def get_web_elements(self):
        return self.driver.find_elements(*self)

    def _find_web_element(orig_func):

        @wraps(orig_func)
        def wrapper(self, *args):
            if type(self) is Control:
                self = self.get_web_element()
            return orig_func(self, *args)

        return wrapper

    @_find_web_element
    def set_text(self, value):
        """
        type text in input box
        :param: Text to be Enter
        :return: webElement
        """
        self.clear()
        self.send_keys(value)
        return self

    @_find_web_element
    def get_text(self):
        """
        get text from input box
        :param: None
        :return: text from webElement
        """
        return self.text

    def visibility_of_element_located(self, timeout=None):
        """
        Wait till the element to be visible
        """
        if timeout is None:
            timeout = Control.default_timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self)
        )


    def is_visible(self, timeout=None):
        """
        Check element is visible or not
        :param: the timeout
        :return: Boolean
        """
        try:
            self.visibility_of_element_located(timeout)
        except TimeoutException:
            return False
        return True

    def invisibility_of_element_located(self, timeout=None):
        """
        Wait till the element to be invisible
        """
        if timeout is None:
            timeout = Control.default_timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(self)
        )

    @_find_web_element
    def press_enter(self):
        """
        Press the Tab key
        :param: None
        :return: webElement
        """
        ActionChains(self.parent).send_keys(Keys.ENTER).perform()
        return self