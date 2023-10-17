from selenium.webdriver.support.select import Select

from Pages.BasePage import BasePage
from Pages.NewCarsPage import NewCarsPage
from Utilities import configReader
from selenium import webdriver

class HomePage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    def gotoNewCars(self):
        self.moveTo("newCars_XPATH")
        self.click("findNewCars_XPATH")
        return  NewCarsPage(self.driver)

    def gottoCompareCars(self):
        pass

    def gotoUsedCars(self):
        pass

