import allure
import pytest
from Utilities.excel_reader import get_list_from_excel
from allure_commons.types import AttachmentType
from DemoWebShop.POM.homepage import HomePage
from DemoWebShop.POM.loginpage import LogIn
import openpyxl

credentials=get_list_from_excel("SeleniumProject.xlsx","login_creds")

@pytest.mark.parametrize("username,password",credentials)
def test_login_with_proper_credentials(driver,username,password):
    home=HomePage(driver)
    home.click_on_login()
    login=LogIn(driver)
    login.login_to_application(username,password)
    condition= driver.find_element("xpath",f"//a[.='{username}']").is_displayed()
    if not condition:
        allure.attach(driver.get_screenshot_as_png(),name="test_login_with_proper_credentials",attachment_type=AttachmentType.PNG)
    assert condition

@pytest.mark.skip
def test_login_with_no_password(driver):
    home = HomePage(driver)
    home.click_on_login()
    login = LogIn(driver)
    login.login_to_application("electricalex0808@gmail.com", "")
    assert driver.find_element("xpath","//span[contains(.,'Login was unsuccessful')]").is_displayed()

@pytest.mark.skip
def test_login_with_no_username(driver):
    home = HomePage(driver)
    home.click_on_login()
    login = LogIn(driver)
    login.login_to_application("", "selenium")
    assert driver.find_element("xpath","//span[contains(.,'Login was unsuccessful')]").is_displayed()

@pytest.mark.skip
def test_with_improper_credentials(driver):
    home = HomePage(driver)
    home.click_on_login()
    login = LogIn(driver)
    login.login_to_application("electricalex0808@gmail.com", "selenium@12")
    assert driver.find_element("xpath","//span[contains(.,'Login was unsuccessful')]").is_displayed()

@pytest.mark.skip
def test_with_blank(driver):
    home = HomePage(driver)
    home.click_on_login()
    login = LogIn(driver)
    login.login_to_application("", "")
    assert driver.find_element("xpath","//span[contains(.,'Login was unsuccessful')]").is_displayed()





