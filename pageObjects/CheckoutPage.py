# Locators for card title, footer button, and checkout button
# xpath = // button[ @class ='btn btn-info'][1] and css selector = .card-footer button
# products=self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
# self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

from selenium.webdriver.common.by import By
from pageObjects.ConfirmPage import ConfirmPage

class CheckOutPage:

    def __init__(self, driver):
         self.driver = driver

    cardTitle=(By.CSS_SELECTOR, ".card-title a")
    cardFooter=(By.CSS_SELECTOR, ".card-footer button")
    checkOut=(By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitles(self):               # Return a list of all card titles
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):              # Return a list of all footer buttons (if needed for further actions)
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def checkOutItems(self):               # Click the checkout button
        self.driver.find_element(*CheckOutPage.checkOut).click()
        #confirmPage = ConfirmPage(self.driver)
        #return confirmPage
        return ConfirmPage(self.driver) # Return an instance of ConfirmPage