import sys
from selenium import webdriver
from selenium.webdriver.common.keys     import Keys
from selenium.webdriver.common.by       import By
from webdriver_manager.chrome           import ChromeDriverManager

def open_browser():
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach",True)
    option.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=option)
    return driver

def bpcl_url(driver):
    driver.get("https://ebiz.bpc.co.in/VendorRegistration/Account")
    driver.find_element(By.NAME,"UserName").send_keys("188373")
    driver.find_element(By.NAME,"Password").send_keys("Test@123")
    #driver.find_element(By.NAME,"submit1").click()

def iocl_url(driver):
    driver.get("https://associates.indianoil.co.in/BTS/vendor_login")
    driver.find_element(By.NAME,"txtuserid").send_keys("188373")
    driver.find_element(By.NAME,"txtpwd").send_keys("Test@123")

def hpcl_url(driver):
    driver.get("https://bills.hpcl.co.in/Vendor/index.jsp")
    driver.find_element(By.NAME,"username").send_keys("188373")
    driver.find_element(By.NAME,"password").send_keys("Test@123")
    #driver.find_element(By.NAME,"submit1").click()


driver = open_browser()

if  len(sys.argv) > 1:
    url = sys.argv[1]
else:
    url = 'HPCL'

match url:
    case 'BPCL':
        bpcl_url(driver)
    case 'HPCL':
        hpcl_url(driver)
    case 'IOCL':
        iocl_url(driver)

