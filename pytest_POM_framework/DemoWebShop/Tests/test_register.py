import allure
import pytest
from allure_commons.types import AttachmentType

from DemoWebShop.POM.homepage import HomePage
from DemoWebShop.POM.registerpage import Register

def test_register_with_all_credentials(driver):
    home=HomePage(driver)
    home.click_on_register()
    register=Register(driver)
    register.register_in_application("Chota","Bheem","chota.bheem620@gmail.com","chintapakdum","chintapakdum")
    condition = driver.find_element("xpath","//li[contains(.,'The specified')]").is_displayed()
    if condition==True:
        allure.attach(driver.get_screenshot_as_png(),name="test_register_with_all_credentials",attachment_type=AttachmentType.PNG)
    assert condition

@pytest.mark.skip
def test_register_without_firstname(driver):
    home = HomePage(driver)
    home.click_on_register()
    register = Register(driver)
    register.register_in_application("", "Bheem", "chotabheem69@gmail.com", "chintapakdum", "chintapakdum")
    assert driver.find_element("xpath","//span[contains(@for,'FirstName')]").is_displayed()

@pytest.mark.skip
def test_register_without_lastname(driver):
    home = HomePage(driver)
    home.click_on_register()
    register = Register(driver)
    register.register_in_application("Chota", "", "chotabheem69@gmail.com", "chintapakdum", "chintapakdum")
    assert driver.find_element("xpath","//span[contains(@for,'LastName')]").is_displayed()

@pytest.mark.skip
def test_register_without_email(driver):
    home = HomePage(driver)
    home.click_on_register()
    register = Register(driver)
    register.register_in_application("Chota", "Bheem", "", "chintapakdum", "chintapakdum")
    assert driver.find_element("xpath", "//span[contains(@for,'Email')]").is_displayed()

@pytest.mark.skip
def test_register_without_password(driver):
    home = HomePage(driver)
    home.click_on_register()
    register = Register(driver)
    register.register_in_application("Chota", "Bheem", "chotabheem69@gmail.com", "", "chintapakdum")
    assert driver.find_element("xpath", "//span[contains(text(),'Password')]").is_displayed()

@pytest.mark.skip
def test_register_without_confirm_password(driver):
    home = HomePage(driver)
    home.click_on_register()
    register = Register(driver)
    register.register_in_application("Chota", "Bheem", "chotabheem69@gmail.com", "chintapakdum", "")
    assert driver.find_element("xpath", "//span[contains(text(),'Password is required.')]").is_displayed()

@pytest.mark.skip
def test_register_without_credentials(driver):
    home = HomePage(driver)
    home.click_on_register()
    register = Register(driver)
    register.register_in_application("", "", "", "", "")
    assert driver.find_element("xpath", "//span[contains(@for,'FirstName')]").is_displayed()

@pytest.mark.skip
def test_register_without_gender(driver):
    home = HomePage(driver)
    home.click_on_register()
    register = Register(driver)
    register.register_in_application_without_gender("Chota", "Bheem", "chota.bheem7320@gmail.com", "chintapakdum", "chintapakdum")
    assert driver.find_element("xpath", "//input[@value='Continue']").is_displayed()
