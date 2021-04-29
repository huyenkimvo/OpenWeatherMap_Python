from weather.tests.step_defs.search_step_def import SearchStepDef
from weather.tests.step_defs.dashboard_step_def import DashboardStepDef
from weather.utils.get_appsettings import get_base_url
from pytest_bdd import scenarios, given, when, then, parsers

scenarios('../features/search_weather.feature')

@given('user navigates to the open weather map page')
def user_logs_into_lg(driver):
    base_url = get_base_url()
    dashboard_step_def = DashboardStepDef(driver)
    dashboard_step_def.navigate_to_the_url(base_url)

@when('verify that the search box is display')
def verify_search_box_displayed(driver):
    dashboard_step_def = DashboardStepDef(driver)
    dashboard_step_def.wait_for_loading_to_disappear()
    dashboard_step_def.verify_search_box_is_display()

@when(parsers.parse('user search for keyword <search_key>'))
def search_weather(driver, search_key):
    dashboard_step_def = DashboardStepDef(driver)
    dashboard_step_def.enter_search_key(search_key)

@then(parsers.parse('verify that user should see the search results as <expected_result>'))
def verify_results_display_as_expected(driver, expected_result):
    search_step_def = SearchStepDef(driver)
    search_step_def.verify_search_results_display_correctly(expected_result)

