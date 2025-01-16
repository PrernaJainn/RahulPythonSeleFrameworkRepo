from selenium import webdriver
import pytest
import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # Use EC for clarity
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from pageObjects.CheckoutPage import CheckOutPage
from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
from pageObjects.ConfirmPage import ConfirmPage


class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        log.info("Test execution started")
        homePage = HomePage(self.driver)
        checkoutpage = homePage.shopItems()  #self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click() (autoclicking)
        cards = checkoutpage.getCardTitles() #checkOutPage = checkoutpage(self.driver) (not required)
        log.info("getting all the card titles")
        i = -1
        for card in cards:
            i=i + 1
            cardText=card.text
            #print(cardText)
            log.info(cardText)
            if cardText == "Blackberry":
                checkoutpage.getCardFooter()[i].click()

                                       # Updated line with the correct syntax
        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
                                       #checkoutpage.checkOutItems().click()
        confirmPage = checkoutpage.checkOutItems()
        print(confirmPage, " Confirm page shows: " )
                                        #confirmPage= checkoutpage.checkOutItems()     # Assign result to confirmPage
        log.info("Entering country name as ind")
        self.driver.find_element(By.ID, "country").send_keys("ind")
        # time.sleep(5)
        self.verifyLinkPresence("India")

        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        textMatch = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        log.info("Text received from application is " + textMatch)
        assert ("Success! Thank you!" in textMatch)   #check the screenshot shows or not




