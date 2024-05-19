from appium.webdriver.common.appiumby import AppiumBy
import selenium


class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def add_product_to_cart(self, product_name):
        product_xpath = f"//android.widget.TextView[@resource-id='com.androidsample.generalstore:id/productName' and @text='{product_name}']"
        while True:
            try:
                product_element = self.driver.find_element(by=AppiumBy.XPATH, value=product_xpath)
                break
            except selenium.common.exceptions.NoSuchElementException:
                self.driver.swipe(690, 1710, 690, 900)
        add_to_cart_xpath = "(//android.widget.TextView[@resource-id='com.androidsample.generalstore:id/productAddCart'])[3]"
        add_to_cart_element = self.driver.find_element(by=AppiumBy.XPATH, value=add_to_cart_xpath)
        add_to_cart_element.click()

    def go_to_cart(self):
        cart_btn = self.driver.find_element(by=AppiumBy.XPATH,
                                            value="//android.widget.ImageButton[@resource-id='com.androidsample.generalstore:id/appbar_btn_cart']")
        cart_btn.click()
