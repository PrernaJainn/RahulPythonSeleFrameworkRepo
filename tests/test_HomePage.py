from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
from TestData.HomePageData import HomePageData  #packagename.filename import class name


# self.selectOptionByText(homepage.getGender(), "Male") dropdown selection and handling it by using select option
# self.selectOptionByText(homepage.getGender(), "Female")
# homepage.getName().send_keys("Prerna")
# homepage.getName().send_keys(getData[0])
# homepage.getName().send_keys(getData[1])
#implementing data driven (not using hardcode using multiple times runs from the external or multiple data set in tuples)
#DICTONARY DATA TYPE  KEY : VALUE pair

# This is and test data is depended on Excel so it is a "Data driver framework or excel driven framework"

class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homepage=HomePage(self.driver)

        log.info("First name is " + getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.getCheckBox().click()

        self.selectOptionByText(homepage.getGender(), getData["gender"])
        homepage.submitForm().click()
        alertText=homepage.getSuccessMessage().text
        assert ("Success" in alertText)
        self.driver.refresh()  # need to refresh

    #this can be written here because this fixture is specifically use in home page if it is use in other pages then write in conftest.py file)
    #using key value pair in dictionary data type {} show in a separate file testdata
    #@pytest.fixture(params=[{"firstname" : "Prerna" , "lastname": "Jain" , "gender" : "Female"},{"firstname" :"Samay","lastname": "Jain","gender" : "Male"}])
    #@pytest.fixture(params=[("Prerna", "Jain", "Female"), ("Samay", "Jain", "Male")])

    #TUPLE using []
    @pytest.fixture(params=HomePageData.test_HomePage_data)
    #@pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):  # inside the class so using self keyword
        return request.param
