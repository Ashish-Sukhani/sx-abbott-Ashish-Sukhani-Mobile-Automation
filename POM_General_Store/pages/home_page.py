import selenium
from appium.webdriver.common.appiumby import AppiumBy


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        element = self.driver.find_element(by=AppiumBy.XPATH,
                                           value="//android.widget.EditText[@resource-id='com.androidsample.generalstore:id/nameField']")
        element.click()
        element.clear()
        element.send_keys(username)

    def select_gender(self):
        gender = self.driver.find_element(by=AppiumBy.XPATH,
                                          value="//android.widget.RadioButton[@resource-id='com.androidsample.generalstore:id/radioFemale']")
        gender.click()

    def select_country(self, country):
        country_dd = self.driver.find_element(by=AppiumBy.XPATH,
                                              value="//android.widget.Spinner[@resource-id='com.androidsample.generalstore:id/spinnerCountry']")
        country_dd.click()
        ele = f'//android.widget.TextView[@resource-id="android:id/text1" and @text="{country}"]'
        while True:
            try:
                country_element = self.driver.find_element(by=AppiumBy.XPATH, value=ele)
                break
            except selenium.common.exceptions.NoSuchElementException:
                self.driver.swipe(700, 1700, 700, 900)
        country_element.click()

    def click_lets_shop(self):
        btn = self.driver.find_element(by=AppiumBy.XPATH,
                                       value="//android.widget.Button[@resource-id='com.androidsample.generalstore:id/btnLetsShop']")
        btn.click()
