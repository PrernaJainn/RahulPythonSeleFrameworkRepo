#resuable methods
# utilities/BaseClass.py
import pytest
import logging
import inspect
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from logging import FileHandler, Formatter, DEBUG  # Ensure these are imported


@pytest.mark.usefixtures("setup")  # Corrected to use `use fixtures`
class BaseClass:
    def getLogger(self):
        loggerName=inspect.stack()[1][3]
        logger=logging.getLogger(loggerName)
        fileHandler=FileHandler("logfile.log")
        formatter=Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        if logger.hasHandlers():
            logger.handlers.clear()  # ADDITIONALLY ADDED Avoid duplicate logs

        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(DEBUG)
        return logger

    def verifyLinkPresence(self, text):
        wait=WebDriverWait(self.driver, 10)  # Use `self.driver` instead of `driver`
        wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, text)))  # runtime text added and use this in multiple times

    def selectOptionByText(self, locator, text):  #dropdown
        sel=Select(locator)
        sel.select_by_visible_text(text)
