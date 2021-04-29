
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def get_driver(webdriver_string):
    def get_driver_name(driver):
        return driver.__name__.upper()

    drivers = [Chrome, Firefox]
    driver_map = {get_driver_name(d): d for d in drivers}
    driver_map["CHROME.HEADLESS"] = Chrome.headless
    driver_map["FIREFOX.HEADLESS"] = Firefox.headless
    driver = driver_map.get(webdriver_string.upper(), None)
    if driver is None:
        raise ValueError(
            'No such driver "{}". Valid options are: {}'.format(
                webdriver_string, ", ".join(driver_map.keys())
            )
        )
    return driver


class Chrome(webdriver.Chrome):
    """
    Chrome driver class. Alternate constructors and browser-specific logic is implemented here.
    """

    def __init__(self, *args, **kwargs):
        chrome_options = kwargs.pop("options", None)
        if chrome_options is None:
            chrome_options = ChromeOptions()
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
        kwargs["options"] = chrome_options
        super(Chrome, self).__init__(
            executable_path=ChromeDriverManager().install(), *args, **kwargs
        )

    @classmethod
    def headless(cls, *args, **kwargs):
        chrome_options = kwargs.pop("options", None)
        if chrome_options is None:
            chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("window-size=1920,1080")
        kwargs["options"] = chrome_options
        return cls(*args, **kwargs)


class Firefox(webdriver.Firefox):
    """
    Firefox driver class. Alternate constructors and browser-specific logic is implemented here.
    """

    def __init__(self, *args, **kwargs):
        super(Firefox, self).__init__(
            executable_path=GeckoDriverManager().install(), *args, **kwargs
        )

    @classmethod
    def headless(cls, *args, **kwargs):
        firefox_options = kwargs.pop("options", None)
        if firefox_options is None:
            firefox_options = FirefoxOptions()
        firefox_options.add_argument("--headless")
        firefox_options.add_argument("window-size=1920,1080")
        kwargs["options"] = firefox_options
        return cls(*args, **kwargs)

