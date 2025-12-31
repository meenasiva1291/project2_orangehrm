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
        adduser_locator = (By.XPATH,"// button[text() = ' Add ']")
        menu_locator = (By.XPATH, "//ul/li[contains(@class,'oxd-main-menu-item-wrapper')]")
        search_username_input = (By.XPATH,"//label[text()='Username']/ancestor::div[contains(@class,'oxd-input-group')]//input")
        user_search_button = (By.XPATH,"//button[text()=' Search ']")
        RESULT_USERNAME_IN_TABLE = "//div[contains(@class,'oxd-table-body')]//a[text()='{}']"
        table_container = (By.XPATH, "//div[contains(@class,'oxd-table-body')]")
        no_records_text = (By.XPATH, "//span[text()='No Records Found']")
        record_found = (By.XPATH,"//span[text()='(1) Record Found']")
        table_verify = (By.XPATH,"(//div[@class='oxd-table']/div[contains(@class,'body')]//div[contains(@class,'padding-cell')]/div)[2]")

        #usercreation page
        admin_locator = (By.XPATH, "//span[text() = 'Admin']")
        userrole_locator = (By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[1]")
        list_locator = (By.XPATH, "//div[@role='listbox']")
        employee_name = (By.XPATH, '//input[@placeholder="Type for hints..."]')
        user_status = (By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[2]")
        admin_username = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        admin_password = (By.XPATH, "//label[text()='Password']/parent::div/parent::div/div[2]/input")
        admin_repassword = (By.XPATH, "//label[text()='Confirm Password']/parent::div/parent::div/div[2]/input")
        submit = (By.XPATH, "//button[@type='submit']")
        user_verify_record = (By.XPATH,"(//div[@class='oxd-table']/div[contains(@class,'body')]//div[contains(@class,'padding-cell')]/div)[2]")

        #my info page
        myinfo_locator = (By.XPATH,"//span[text()='My Info']")
        myinfo_menu = (By.XPATH,"//div[contains(@class,'orangehrm-tabs')]/div")

        #leave page
        leave_option = (By.XPATH,"//span[text()='Leave']")
        assign_leaves = (By.XPATH,"//a[text()='Assign Leave']")
        leave_type = (By.CSS_SELECTOR,".oxd-select-text--arrow")
        from_date = (By.XPATH,"(//div[@class='oxd-date-input']/input)[1]")
        to_date = (By.XPATH,"//label[text()='To Date']/parent::div/parent::div//input")
        comments = (By.XPATH,"//textarea[contains(@class, 'oxd-textarea')]")
        assign_button = (By.XPATH,"//button[text()=' Assign ']")
        confirm_button = (By.XPATH,"//button[text()=' Ok ']")
        success_toaster = (By.XPATH,"//p[text()='Success']")

        #claims page
        claim_option = (By.XPATH,"//span[text()='Claim']")
        submit_claim = (By.XPATH,"//a[text()='Submit Claim']")
        event_dropdown=(By.XPATH,"//label[text()='Event']/parent::div/parent::div//div[contains(text(),'Select')]")
        currency_dropdown=(By.XPATH,"//label[text()='Currency']/parent::div/parent::div//div[contains(text(),'Select')]")
        create_button = (By.XPATH,"//button[text()=' Create ']")
        reference_id = (By.XPATH,"//label[text()='Reference Id']/parent::div/parent::div//input[contains(@class,'oxd-input--active')]")
        submit_button = (By.XPATH,"//button[text()=' Submit ']")
        my_claims = (By.XPATH,"//a[text()='My Claims']")
        claim_verify_record = (By.XPATH,"(//div[@class='oxd-table']/div[contains(@class,'body')]//div[contains(@class,'padding-cell')]/div)[1]")







