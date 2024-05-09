import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
import time
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.extensions.keyboard import Keyboard
import selenium
import re


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
country = 'India'
username = 'Test Name'

option = UiAutomator2Options()
option.load_capabilities(capabilities)
driver = webdriver.Remote(appium_server_url, options=option)
time.sleep(10)

element = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@resource-id='com.androidsample.generalstore:id/nameField']")
element.click()
element.clear()
element.send_keys(username)

gender = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.RadioButton[@resource-id='com.androidsample.generalstore:id/radioFemale']")
gender.click()

country_dd = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Spinner[@resource-id='com.androidsample.generalstore:id/spinnerCountry']")
country_dd.click()
ele = f'//android.widget.TextView[@resource-id="android:id/text1" and @text="{country}"]'
time.sleep(2)
while True:
    try:
        country_element = driver.find_element(by=AppiumBy.XPATH, value=ele)
        break
    except selenium.common.exceptions.NoSuchElementException:
        driver.swipe(700, 1700, 700, 900)

country_element.click()

btn = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@resource-id='com.androidsample.generalstore:id/btnLetsShop']")
btn.click()
time.sleep(3)

shoe1 = "//android.widget.TextView[@resource-id='com.androidsample.generalstore:id/productName' and @text='PG 3']"
while True:
    try:
        find_shoe1 = driver.find_element(by=AppiumBy.XPATH, value=shoe1)
        break
    except selenium.common.exceptions.NoSuchElementException:
        driver.swipe(700, 1700, 700, 900)

shoe1_atc = driver.find_element(by=AppiumBy.XPATH, value="(//android.widget.TextView[@resource-id='com.androidsample.generalstore:id/productAddCart'])[3]")
shoe1_atc.click()

shoe2 = "//android.widget.TextView[@resource-id='com.androidsample.generalstore:id/productName' and @text='Nike SFB Jungle']"
while True:
    try:
        find_shoe2 = driver.find_element(by=AppiumBy.XPATH, value=shoe2)
        break
    except selenium.common.exceptions.NoSuchElementException:
        driver.swipe(700, 1700, 700, 800)

shoe2_atc = driver.find_element(by=AppiumBy.XPATH, value="(//android.widget.TextView[@resource-id='com.androidsample.generalstore:id/productAddCart'])[3]")
shoe2_atc.click()

cart_btn = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.ImageButton[@resource-id='com.androidsample.generalstore:id/appbar_btn_cart']")
cart_btn.click()
time.sleep(2)
cart_heading = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id='com.androidsample.generalstore:id/toolbar_title' and @text='Cart']")
if cart_heading.is_displayed():
    print("Validation Successful: User is on cart page")
else:
    print("User is NOT on cart page")

shoe1_price = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id='com.androidsample.generalstore:id/productPrice' and @text='$110.0']")
p1 = shoe1_price.text
s1 = p1.replace("$", "")

shoe2_price = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id='com.androidsample.generalstore:id/productPrice' and @text='$116.97']")
p2 = shoe2_price.text
s2 = p2.replace("$", "")

sum = float(s1) + float(s2)

totalprice = driver.find_element(by=AppiumBy.ID, value="com.androidsample.generalstore:id/totalAmountLbl")
print("Total price: " + totalprice.text)
t = totalprice.text
totalp = t.replace("$", "")
totalp = float(totalp)

if totalp == sum:
    print("Validation Successful: Total Purchase Amount Is Equal To Cart Items' Amount")

discount_cb = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.CheckBox[@text='Send me e-mails on discounts related to selected products in future']")
discount_cb.click()

visitweb_btn = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@resource-id='com.androidsample.generalstore:id/btnProceed']")
visitweb_btn.click()
time.sleep(10)
textfield_google = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
textfield_google.click()
textfield_google.clear()
textfield_google.send_keys('General Store')
time.sleep(8)

driver.execute_script('mobile: pressKey', {"keycode": 4})  # To Close The Keyboard
driver.execute_script('mobile: pressKey', {"keycode": 4})  # Action To Go Back To Main Page
time.sleep(8)

gs_title = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id='com.androidsample.generalstore:id/toolbar_title' and @text='General Store']")
if gs_title.is_displayed():
    print("Validation Successful: User is on homepage")
else:
    print("User is NOT on homepage")



