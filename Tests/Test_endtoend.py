import time

import pytest
from selenium import webdriver

from PageObjects.GreenCart_HomePage import GreenCart_HomePage
from PageObjects.PromoCodePage import PromoCodePage
from PageObjects.TermsConditionPage import TermsConditionPage
from Tests.conftest import setup
from Utilities.BaseClass import BaseClass


class Test_endtoend(BaseClass):
    def test_e2e1(self):
        log = self.getLogger()
        Homepage = GreenCart_HomePage(self.driver)
        log.info("searching the product name")
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
        log.info("Test completed successfully")
        time.sleep(3)
