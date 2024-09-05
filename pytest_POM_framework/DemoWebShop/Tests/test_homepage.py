import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome.webdriver import WebDriver
from DemoWebShop.POM.homepage import HomePage

# @pytest.fixture()
# def driver():
#     driver=WebDriver()
#     driver.maximize_window()
#     driver.get("https://demowebshop.tricentis.com/")
#     yield driver
#     driver.quit()

@pytest.mark.skip
def test_check_login(driver):
    hompge_obj=HomePage(driver)
    hompge_obj.click_on_login()
    allure.attach(driver.get_screenshot_as_png(),name="test_check_login",attachment_type=AttachmentType.PNG)

@pytest.mark.skip
def test_check_register(driver):
    hompge_obj=HomePage(driver)
    hompge_obj.click_on_register()

