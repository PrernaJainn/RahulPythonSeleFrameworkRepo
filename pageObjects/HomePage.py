from pageObjects.CheckoutPage import CheckOutPage
from selenium.webdriver.common.by import By

#from selenium import webdriver (alt+shift+enter shows the import option)

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop=(By.CSS_SELECTOR, "a[href*='shop']") # Locator for the 'Shop' link
    name=(By.CSS_SELECTOR, "[name='name']")
    email=(By.NAME, "email")
    check=(By.ID, "exampleCheck1")
    gender=(By.ID, "exampleFormControlSelect1")
    submit=(By.XPATH, "//input[@value='Submit']")
    successMessage=(By.CSS_SELECTOR, "[class*='alert-success']")


    def shopItems(self): # Click on the 'Shop' link
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage=CheckOutPage(self.driver)# Return the CheckOutPage instance after clicking the 'Shop' link
        return checkOutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage.check)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage)

