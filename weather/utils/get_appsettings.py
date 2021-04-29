import json
with open('weather/weather_appsettings.json') as config_file:
    config = json.load(config_file)


def get_browser():
    return config["Browser"]


def get_headless():
    return config["headless"]


def get_base_url():
    return config["appURL"]


