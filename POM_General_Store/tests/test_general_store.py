import time
from appium.webdriver.common.appiumby import AppiumBy
from base_test import BaseTest
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


class TestGeneralStore(BaseTest):
    def test_shopping_process(self):
        home_page = HomePage(self.driver)
        product_page = ProductPage(self.driver)
        cart_page = CartPage(self.driver)

        username = 'Test Name'
        country = 'India'

        time.sleep(10)
        home_page.enter_username(username)
        home_page.select_gender()
        home_page.select_country(country)
        home_page.click_lets_shop()

        time.sleep(5)
        product_page.add_product_to_cart('PG 3')
        product_page.add_product_to_cart('Nike SFB Jungle')
        product_page.go_to_cart()

        time.sleep(5)
        self.assertTrue(cart_page.validate_cart_page(), "User is NOT on cart page")

        time.sleep(3)
        shoe1_price = cart_page.get_product_price_PG3()
        shoe2_price = cart_page.get_product_price_Nike_Jungle()
        total_price = cart_page.get_total_price()

        self.assertEqual(total_price, shoe1_price + shoe2_price,
                         "Total Purchase Amount Is Not Equal To Cart Items' Amount")

        cart_page.apply_discount_checkbox()
        cart_page.proceed_to_website()

        time.sleep(10)
        textfield_google = self.driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
        textfield_google.click()
        textfield_google.clear()
        textfield_google.send_keys('General Store')
        time.sleep(8)

        self.driver.execute_script('mobile: pressKey', {"keycode": 4})  # To Close The Keyboard
        self.driver.execute_script('mobile: pressKey', {"keycode": 4})  # Action To Go Back To Main Page
        time.sleep(8)

        gs_title = self.driver.find_element(by=AppiumBy.XPATH,
                                            value="//android.widget.TextView[@resource-id='com.androidsample.generalstore:id/toolbar_title' and @text='General Store']")
        self.assertTrue(gs_title.is_displayed(), "User is NOT on homepage")
