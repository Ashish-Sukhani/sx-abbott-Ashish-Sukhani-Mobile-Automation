from appium import webdriver
from appium.options.android import UiAutomator2Options


def init_driver():
    capabilities = dict(
        platformName='Android',
        automationName='uiautomator2',
        deviceName='Android',
        appPackage='com.androidsample.generalstore',
        appActivity='com.androidsample.generalstore.SplashActivity',
        language='en',
        locale='US'
    )

    appium_server_url = 'http://localhost:4723'
    option = UiAutomator2Options()
    option.load_capabilities(capabilities)
    driver = webdriver.Remote(appium_server_url, options=option)
    return driver
