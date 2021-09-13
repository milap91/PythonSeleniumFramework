import time

import pytest
from selenium import webdriver

from PageObjects.GreenCart_HomePage import GreenCart_HomePage
from PageObjects.PromoCodePage import PromoCodePage
from PageObjects.TermsConditionPage import TermsConditionPage
from Tests.conftest import setup


@pytest.mark.usefixtures("setup")
class Test_endtoend:
    def test_e2e1(self):

        Homepage = GreenCart_HomePage(self.driver)
        Homepage.search_product("berry")
        Homepage.verify_products_count(2)
        Homepage.verify_products_name_and_add_them_in_cart()
        Homepage.click_on_cartitem()
        Homepage.verify_products_count_in_cart(2)
        Homepage.verify_products_name_in_cart()
        Homepage.click_on_proceed_to_checkout()
        BillingPage = PromoCodePage(self.driver)
        BillingPage.verify_products_count_in_product_table(2)
        BillingPage.verify_products_name_in_product_table()
        BillingPage.enter_promocode("rahulshettyacademy")
        BillingPage.verify_discount("10%")
        BillingPage.click_on_place_order()
        time.sleep(3)
        Termspage = TermsConditionPage(self.driver)
        Termspage.Accept_Conditions("India")
        Termspage.verify_success_Text()
        time.sleep(3)
