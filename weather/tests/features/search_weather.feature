Feature: search weather in your city

  @web @search
  Scenario Outline: search the weather
    Given user navigates to the open weather map page
    When verify that the search box is display
    When user search for keyword <search_key>
    Then verify that user should see the search results as <expected_result>
    Examples:
      | search_key       | expected_result           |
      | Ho Chi Minh city | Thanh pho Ho Chi Minh, VN |
