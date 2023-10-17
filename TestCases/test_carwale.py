import time

from Pages.CarBase import CarBase
from Pages.HomePage import HomePage
from TestCases.BaseTest import BaseTest
from Utilities import dataProvider
import pytest
from Pages.RegistrationPage import RegistrationPage
import logging
from Utilities.LogUtil import Logger
log=Logger(__name__,logging.INFO)


class Test_Carewale(BaseTest):
    @pytest.mark.skip
    def test_goToNewCar(self):

        log.logger.info("******Inside new car*******")
        home=HomePage(self.driver)
        home.gotoNewCars()
        time.sleep(3)

    @pytest.mark.skip
    @pytest.mark.parametrize("carBrand,carTitle",dataProvider.getData("NewCarTest"))
    def test_selectCar(self,carBrand,carTitle):
        log.logger.info("******Inside select car*******")
        home = HomePage(self.driver)

        car=CarBase(self.driver)
        if carBrand=='BMW':
            home.gotoNewCars().selectBMW()
            title=car.getCarTitle()
            print(("Car title is : "+title).encode('utf8'))
            assert title==carTitle,"Not on the correct page as the title is not matching"
        elif carBrand=='Hyundai':
            home.gotoNewCars().selectHyundai()
            title = car.getCarTitle()
            print(("Car title is : " + title).encode('utf8'))
            assert title == carTitle, "Not on the correct page as the title is not matching"
        elif carBrand=='Honda':
            home.gotoNewCars().selectHonda()
            title = car.getCarTitle()
            print(("Car title is : " + title).encode('utf8'))
            assert title == carTitle, "Not on the correct page as the title is not matching"
        elif carBrand=='Toyota':
            home.gotoNewCars().selectToyota()
            title = car.getCarTitle()
            print(("Car title is : " + title).encode('utf8'))
            assert title == carTitle, "Not on the correct page as the title is not matching"


    @pytest.mark.parametrize("carBrand,carTitle", dataProvider.getData("NewCarTest"))
    def test_printCarNamesandPrices(self, carBrand, carTitle):
        log.logger.info("******Inside car Names and Prices Test*******")
        home = HomePage(self.driver)

        car = CarBase(self.driver)
        if carBrand == 'BMW':
            home.gotoNewCars().selectBMW()
            title = car.getCarTitle()
            print(("Car title is : " + title).encode('utf8'))
            assert title == carTitle, "Not on the correct page as the title is not matching"
            car.getCarNameAndPrices()
        elif carBrand == 'Hyundai':
            home.gotoNewCars().selectHyundai()
            title = car.getCarTitle()
            print(("Car title is : " + title).encode('utf8'))
            assert title == carTitle, "Not on the correct page as the title is not matching"
            car.getCarNameAndPrices()
        elif carBrand == 'Honda':
            home.gotoNewCars().selectHonda()
            title = car.getCarTitle()
            print(("Car title is : " + title).encode('utf8'))
            assert title == carTitle, "Not on the correct page as the title is not matching"
            car.getCarNameAndPrices()
        elif carBrand == 'Toyota':
            home.gotoNewCars().selectToyota()
            title = car.getCarTitle()
            print(("Car title is : " + title).encode('utf8'))
            assert title == carTitle, "Not on the correct page as the title is not matching"
            car.getCarNameAndPrices()



