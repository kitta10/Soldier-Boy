from DemoWebShop.Library.libraries import Base
from Utilities.locators import HomePageLocators

class HomePage(Base):
   def click_on_login(self):
      self.click_on_element(HomePageLocators.login_link)

   def click_on_register(self):
      self.click_on_element(HomePageLocators.register_link)