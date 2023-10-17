from selenium.webdriver.support.select import Select

from Pages.BasePage import BasePage
from Utilities import configReader
from selenium import webdriver

class HondaPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)