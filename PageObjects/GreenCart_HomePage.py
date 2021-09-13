from selenium.webdriver.common.by import By


class GreenCart_HomePage:
    product_catagloge = {"Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"}

    def __init__(self, driver):
        self.driver = driver

    searchbox = (By.XPATH, "//input[@class='search-keyword']")
    products = (By.XPATH, "//div[@class='product']")
    items = (By.XPATH, "//div[@class='cart-info']//tr[1]/td[3]/strong")
    carticon = (By.XPATH, "//a[@class='cart-icon']")
    cartitems= (By.XPATH, "//div[@class='cart-preview active']/div/div/ul/li")
    proceedtocheckout = (By.XPATH, "//div[@class='action-block']/button")

    # below method will take the productname from the user and send it to the searchbox
    def search_product(self, productname):
        self.driver.find_element(*GreenCart_HomePage.searchbox).send_keys(productname)

    def verify_products_count(self, number_of_products):
        result_product = len((self.driver.find_elements(*GreenCart_HomePage.products)))
        print(result_product)
        assert result_product == number_of_products

    def verify_products_name_and_add_them_in_cart(self):
        products = self.driver.find_elements(*GreenCart_HomePage.products)
        for product in products:
            product_name = product.find_element_by_xpath("h4").text
            assert product_name in self.product_catagloge

            addition_button = product.find_element_by_xpath("div[@class='stepper-input']/a[2]")
            addition_button.click()

            add_to_cart = product.find_element_by_xpath("div[@class='product-action']/button")
            add_to_cart.click()



    def click_on_cartitem(self):
        self.driver.find_element(*GreenCart_HomePage.carticon).click()

    def verify_products_count_in_cart(self,number_of_products):
        result_product = len((self.driver.find_elements(*GreenCart_HomePage.cartitems)))
        print(result_product)
        assert result_product == number_of_products

    def verify_products_name_in_cart(self):
        cart_items = self.driver.find_elements(*GreenCart_HomePage.cartitems)
        for cart_item in cart_items:
            item_name = cart_item.find_element_by_xpath("div[1]/p[1]").text
            assert item_name in self.product_catagloge

    def click_on_proceed_to_checkout(self):
        self.driver.find_element(*GreenCart_HomePage.proceedtocheckout).click()


