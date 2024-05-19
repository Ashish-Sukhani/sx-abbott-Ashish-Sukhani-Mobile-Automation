import time

from appium.webdriver.common.appiumby import AppiumBy


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def validate_cart_page(self):
        cart_heading = self.driver.find_element(by=AppiumBy.XPATH,
                                                value="//android.widget.TextView[@resource-id='com.androidsample.generalstore:id/toolbar_title' and @text='Cart']")
        return cart_heading.is_displayed()

    def get_product_price_PG3(self):
        price_xpath = f"//android.widget.TextView[@resource-id='com.androidsample.generalstore:id/productPrice' and @text='$110.0']"
        price_element = self.driver.find_element(by=AppiumBy.XPATH, value=price_xpath)
        price_text = price_element.text
        time.sleep(3)
        pt = price_text.replace("$", "")
        return float(pt)

    def get_product_price_Nike_Jungle(self):
        price_xpath = f"//android.widget.TextView[@resource-id='com.androidsample.generalstore:id/productPrice' and @text='$116.97']"
        price_element = self.driver.find_element(by=AppiumBy.XPATH, value=price_xpath)
        price_text = price_element.text
        time.sleep(3)
        pt = price_text.replace("$", "")
        return float(pt)
    def get_total_price(self):
        totalprice = self.driver.find_element(by=AppiumBy.ID, value="com.androidsample.generalstore:id/totalAmountLbl")
        total_text = totalprice.text
        tp = total_text.replace("$", "")
        time.sleep(3)
        return float(tp)

    def apply_discount_checkbox(self):
        discount_cb = self.driver.find_element(by=AppiumBy.XPATH,
                                               value="//android.widget.CheckBox[@text='Send me e-mails on discounts related to selected products in future']")
        discount_cb.click()

    def proceed_to_website(self):
        visitweb_btn = self.driver.find_element(by=AppiumBy.XPATH,
                                                value="//android.widget.Button[@resource-id='com.androidsample.generalstore:id/btnProceed']")
        visitweb_btn.click()
