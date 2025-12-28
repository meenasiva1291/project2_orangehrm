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
        logoutmenu_locator = (By.CLASS_NAME,"oxd-userdropdown-name")
        logout_locator = (By.XPATH, "//a[text()='Logout']")
        # adduser_locator = (By.CSS_SELECTOR, "oxd-button oxd-button--medium oxd-button--secondary")
        adduser_locator = (By.XPATH,"// button[text() = ' Add ']")
        menu_locator = (By.XPATH, "//ul/li[contains(@class,'oxd-main-menu-item-wrapper')]")

        #usercreation page
        admin_locator = (By.XPATH, "// span[text() = 'Admin']")
        userrole_locator = (By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[1]")
        list_locator = (By.XPATH, "//div[@role='listbox']")
        employee_name = (By.XPATH, '//input[@placeholder="Type for hints..."]')
        user_status = (By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[2]")
        admin_username = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        admin_password = (By.XPATH, "//label[text()='Password']/parent::div/parent::div/div[2]/input")
        admin_repassword = (By.XPATH, "//label[text()='Confirm Password']/parent::div/parent::div/div[2]/input")
        submit = (By.XPATH, "//button[@type='submit']")

        #my info page
        myinfo_locator = (By.XPATH,"//span[text()='My Info']")
        myinfo_menu = (By.XPATH,"//div[contains(@class,'orangehrm-tabs')]/div")

        #leave page
        leave_option = (By.XPATH,"//span[text()='Leave']")
        assign_leaves = (By.XPATH,"//a[text()='Assign Leave']")
        # leave_type = (By.XPATH,"//label[text()='Leave Type']/following::i[contains(@class,'oxd-select-text--arrow')]")
        leave_type = (By.CSS_SELECTOR,".oxd-select-text--arrow")
        from_date = (By.XPATH,"(//div[@class='oxd-date-input']/input)[1]")
        # from_date = (By.XPATH, "(//label[text() = 'From Date']/parent::div/parent::div//input")
        to_date = (By.XPATH,"//label[text()='To Date']/parent::div/parent::div//input")
        # to_date = (By.XPATH,"(//input[@placeholder='yyyy-dd-mm'])[2]")
        comments = (By.XPATH,"//textarea[contains(@class, 'oxd-textarea')]")
        assign_button = (By.XPATH,"//button[text()=' Assign ']")
        confirm_button = (By.XPATH,"//button[text()=' Ok ']")
        success_message= (By.ID,"oxd-toaster_1")





