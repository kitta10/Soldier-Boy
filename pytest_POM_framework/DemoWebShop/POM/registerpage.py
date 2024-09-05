from DemoWebShop.POM.homepage import HomePage
from Utilities.locators import RegisterPageLocators


class Register(HomePage):

    def register_in_application(self,fN,lN,email,pwd,cnfrmpwd):
        self.click_on_element(RegisterPageLocators.gender_locator)
        self.send_text_to_an_element(RegisterPageLocators.firstname_locator,fN)
        self.send_text_to_an_element(RegisterPageLocators.lastname_locator,lN)
        self.send_text_to_an_element(RegisterPageLocators.email_locator,email)
        self.send_text_to_an_element(RegisterPageLocators.password_locator,pwd)
        self.send_text_to_an_element(RegisterPageLocators.confirm_password_locator,cnfrmpwd)
        self.click_on_element(RegisterPageLocators.register_btn)

    def register_in_application_without_gender(self,fN,lN,email,pwd,cnfrmpwd):
        self.send_text_to_an_element(self.firstname_locator,fN)
        self.send_text_to_an_element(self.lastname_locator,lN)
        self.send_text_to_an_element(self.email_locator,email)
        self.send_text_to_an_element(self.password_locator,pwd)
        self.send_text_to_an_element(self.confirm_password_locator,cnfrmpwd)
        self.click_on_element(self.register_btn)

