import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class TermsConditionPage:

    def __init__(self, driver):
        self.driver = driver

    selctdropdown = (By.CSS_SELECTOR ,"select")
    checkbox = (By.CSS_SELECTOR ,".chkAgree")
    proceedbutton = (By.CSS_SELECTOR,"button")
    successtext= (By.XPATH, "//*[contains(text(),'Thank')]")


    def Accept_Conditions(self,country):
        countryselect = self.driver.find_element(*TermsConditionPage.selctdropdown)
        Select(countryselect).select_by_visible_text(country)
        self.driver.find_element(*TermsConditionPage.checkbox).click()
        self.driver.find_element(*TermsConditionPage.proceedbutton).click()

    def verify_success_Text(self):
        success= self.driver.find_element(*TermsConditionPage.successtext).text
        expected ="Thank you, your order has been placed successfully"
        assert expected in success
