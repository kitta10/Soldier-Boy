from DemoWebShop.POM.homepage import HomePage
from Utilities.locators import SearchFieldLocators


class SearchItems(HomePage):
    def find_items(self,items):
        self.send_text_to_an_element(SearchFieldLocators.text_field,items)
        self.click_on_element(self.search_btn)


