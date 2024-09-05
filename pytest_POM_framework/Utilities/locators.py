class HomePageLocators:
    login_link = ("xpath", "//a[.='Log in']")
    register_link = ("xpath", "//a[.='Register']")

class LoginPageLocators:
    email_locator = ("id", "Email")
    password_locator = ("id", "Password")
    login_btn = ("xpath", "//input[@value='Log in']")

class RegisterPageLocators:
    gender_locator = ("id", "gender-male")
    firstname_locator = ("id", "FirstName")
    lastname_locator = ("id", "LastName")
    email_locator = ("id", "Email")
    password_locator = ("id", "Password")
    confirm_password_locator = ("id", "ConfirmPassword")
    register_btn = ("id", "register-button")

class SearchFieldLocators:
    text_field = ("id", "small-searchterms")
    search_btn = ("xpath", "(//input[@value='Search'])[1]")
