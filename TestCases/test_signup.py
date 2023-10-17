from TestCases.BaseTest import BaseTest
from Utilities import dataProvider
import pytest
from Pages.RegistrationPage import RegistrationPage
import logging
from Utilities.LogUtil import Logger
log=Logger(__name__,logging.INFO)


class Test_SignUpTest(BaseTest):

    @pytest.mark.parametrize("name,phoneNum,email,country,city,username,password",dataProvider.getData("LoginTest"))
    def test_doSignUp(self,name,phoneNum,email,country,city,username,password):
        log.logger.info("Test do signup started")
        regPage=RegistrationPage(self.driver)
        regPage.fillForm(name,phoneNum,email,country,city,username,password)
        log.logger.info("Test do signup successfully verified")
