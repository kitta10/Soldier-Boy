import pytest

from DemoWebShop.POM.homepage import HomePage
from DemoWebShop.POM.loginpage import LogIn
from DemoWebShop.POM.searchfield import SearchItems

@pytest.mark.skip
def test_search_for_items(driver):
    home=HomePage(driver)
    home.click_on_login()
    login=LogIn(driver)
    login.login_to_application("electricalex0808@gmail.com","selenium")
    search=SearchItems(driver)
    search.find_items("computer")
    assert driver.find_element("xpath","//a[.='Build your own computer']").is_displayed()