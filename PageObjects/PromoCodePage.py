import time

from selenium.webdriver.common.by import By


class PromoCodePage:
    product_catagloge = {"Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"}
    Code_applied_text = "Code applied ..!"

    def __init__(self, driver):
        self.driver = driver

    Product_Table = (By.XPATH, "//table[@class='cartTable']/tbody/tr")
    Promo_code = (By.CSS_SELECTOR, ".promoCode")
    Apply = (By.CSS_SELECTOR, ".promoBtn")
    Codesuccesstext = (By.CSS_SELECTOR, ".promoInfo")
    DiscountPercentage = (By.CSS_SELECTOR, ".discountPerc")
    PlaceOrderButton= (By.XPATH,"//button[text()='Place Order']")

    def verify_products_count_in_product_table(self, number_of_products):
        time.sleep(2)
        result_product = len((self.driver.find_elements(*PromoCodePage.Product_Table)))
        assert result_product == number_of_products

    def verify_products_name_in_product_table(self):
        products = self.driver.find_elements(*PromoCodePage.Product_Table)
        for product in products:
            product_name = product.find_element_by_xpath("td[2]/p").text
            assert product_name in self.product_catagloge

    def enter_promocode(self, promo):
        self.driver.find_element(*PromoCodePage.Promo_code).send_keys(promo)
        self.driver.find_element(*PromoCodePage.Apply).click()

    def verify_discount(self, percentage):
        time.sleep(7)
        actual_text = self.driver.find_element(*PromoCodePage.Codesuccesstext).text
        print(actual_text)
        assert self.Code_applied_text == actual_text
        actual_percentage= self.driver.find_element(*PromoCodePage.DiscountPercentage).text
        print(actual_percentage)
        assert percentage == actual_percentage

    def click_on_place_order(self):
        self.driver.find_element(*PromoCodePage.PlaceOrderButton).click()

