from selenium.webdriver.common.by import By


class locators:
        #login page
        username_input = (By.NAME, "username")
        password_input = (By.NAME, "password")
        loginbutton_click = (By.XPATH, "//button[text()=' Login ']")
        errormessage_text = (By.XPATH, "//p[text()='Invalid credentials']")
        forgotpassword_locator = (By.XPATH, "//p[text()='Forgot your password? ']")
        resetlink_locator = (By.XPATH, "//button[text()=' Reset Password ']")
        resetpasswordtext_locator = (By.XPATH, '//div[@class="orangehrm-card-container"]')

        #Dashboard page
        logoutmenu_locator = (By.CLASS_NAME, "oxd-userdropdown")
        logout_locator = (By.XPATH, "//a[text()='Logout']")


