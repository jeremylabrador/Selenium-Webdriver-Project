# Selenium-Webdriver-Project
This Selenium Webdriver Project tests an e-commerce website: http://automationpractice.com/index.php

Download and unzip the directories and files to your computer. Follow below to run!

#### Tested using:
* System: Windows 10
* Browsers: Firefox Version 71.0 (64-bit), Chrome Version 79.0.3945.79 (64-bit)
* Drivers: ChromeDriver, GeckoDriver
* Selenium WebDriver: Version 3.14.0
* Python: Version 3.6.6
* Pytest: Version 5.0.1

#### Three sections of the website are tested:
1) Login Page
2) Product Detail Page
3) Shopping Cart

#### To run one test at a time, from the command-line, go to the tests folder and run any of these commands:
```
$ pytest -s -v test_login.py
$ pytest -s -v test_product_detail_page.py
$ pytest -s -v test_shopping_cart.py
```

#### To run all tests at once, from the command-line, go to the tests folder and run:
```
$ pytest -s -v
```

#### To run any test using Firefox, use the --browser command-line option:
```
$ pytest -s -v test_login.py --browser firefox
```
