import pytest

from pages.buy_item_locators import BuyItemLocators
from pages.checout_locators import CheckOutLocators
from pages.login_locators import LoginLocators
from pages.registrationLocators import RegistrationLocators
from packageutilities.BaseClass import BaseClass

class TestCompleteFlow(BaseClass):

    @pytest.mark.skip
    def test_valid_reg(self):
        rg = RegistrationLocators(self.driver)
        rg.registration("ankit", "jain", "ankits121239@example.com", "Ankit@123", "Ankit@123")

    def test_log_in(self):
        lg = LoginLocators(self.driver)
        lg.log_in("ankits121239@example.com", "Ankit@123")

    def test_item_buy(self):
        bi = BuyItemLocators(self.driver)
        bi.buy_item("Build your own cheap computer")

    def test_checkout(self):
        co = CheckOutLocators(self.driver)
        co.check_out("India", "Indore","Test001", "Test002","452002","989898989")



