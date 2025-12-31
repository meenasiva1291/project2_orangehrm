# OrangeHRM Selenium Automation Framework

## Project Overview

This project is a **Selenium + PyTest automation framework** built using the **Page Object Model (POM)** to automate the OrangeHRM demo application. It supports **data-driven testing using Excel**, **Allure reporting**, and clean separation of test logic, pages, and locators.



---

##  Tech Stack

* **Language:** Python 3.x
* **Automation Tool:** Selenium WebDriver
* **Test Framework:** PyTest
* **Design Pattern:** Page Object Model (POM)
* **Reporting:** Allure Reports
* **Data Source:** Excel (.xlsx)

---

## 📂 Project Structure

```
project2_orangehrm/
│
├── allure/                  # Allure config & static assets
├── allure-report/           # Generated Allure HTML report
├── allure-results/          # Raw Allure result files
│
├── assets/
│   └── style.css
│
├── locators/
│   ├── __init__.py
│   └── locators.py           # All element locators
│
├── pages/
│   ├── __init__.py
│   ├── basepage.py           # Common Selenium actions
│   ├── loginpage.py          # Login page actions
│   ├── dashboardpage.py      # Dashboard actions
│   ├── claimpage.py
│   ├── leavepage.py
│   ├── myinfopage.py
│   └── usercreationpage.py
│
├── test_data/
│   ├── __init__.py
│   └── test_data.xlsx        # Test data for data-driven tests
│
├── tests/
│   ├── allure-results/
│   ├── __init__.py
│   ├── conftest.py            # PyTest fixtures (driver setup)
│   ├── test_project.py       # Test cases
│   └── read_data_from_xl.py  # Excel read/write utilities
│
├── config.ini                # Environment & browser configuration
└── README.md
```

---

##  Features Implemented

* ✔ Valid login test with admin credentials
* ✔ Multiple login validation using Excel (data-driven)
* ✔ Login success/failure written back to Excel
* ✔ Logout after successful login
* ✔ Modular and reusable page classes
* ✔ Allure HTML reporting

---

##  How to Set Up & Run

### 1️⃣ Install Dependencies

```bash
pip install selenium pytest allure-pytest openpyxl
```

Ensure **ChromeDriver** (or relevant driver) is available in PATH.

---

### 2️⃣ Run Tests

```bash
pytest -v --alluredir=allure-results
```

---

### 3️⃣ Generate Allure Report

```bash
allure serve allure-results
```

OR

```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```

---

## 📊 Data-Driven Testing (Excel)

* Test data is stored in:

  ```
  test_data/test_data.xlsx
  ```
* Utility functions:

  * `read_data()` → Reads username, password, row number
  * `write_result(row, result)` → Writes **Login Success / Failure** back to Excel

---


## ⚙ Configuration

* Browser, URL, and other settings can be managed in:

```
config.ini
```

---



