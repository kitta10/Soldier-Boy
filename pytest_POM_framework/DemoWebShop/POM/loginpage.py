from DemoWebShop.POM.homepage import HomePage
from Utilities.locators import LoginPageLocators

class LogIn(HomePage):
    def login_to_application(self,username,password):
        self.send_text_to_an_element(LoginPageLocators.email_locator,username)
        self.send_text_to_an_element(LoginPageLocators.password_locator,password)
        self.click_on_element(LoginPageLocators.login_btn)

    