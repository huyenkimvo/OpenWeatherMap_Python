from helpers.screen_shot import take_screen_shot
import pytest
from helpers.drivers import get_driver
from helpers.custom_log import CustomLog
from weather.utils.get_appsettings import get_browser, get_headless

logger = CustomLog()


@pytest.fixture
def driver():
    web_driver_name = get_browser()
    is_headless = get_headless()
    if type(is_headless) is bool and is_headless is True:
        web_driver_name = f"{web_driver_name}.headless"
    driver = get_driver(web_driver_name)
    driver = driver()
    yield driver
    driver.quit()
    logger.close_log()


def pytest_bdd_step_error(request):
    driver = request.getfixturevalue('driver')
    screen_shot_path = take_screen_shot(driver)
    logger.info(f'The screenshot path is {screen_shot_path}')



