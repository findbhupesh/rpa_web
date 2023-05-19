import sys
from selenium import webdriver
from selenium.webdriver.chrome.service  import Service
from selenium.webdriver.common.keys     import Keys
from selenium.webdriver.common.by       import By
from webdriver_manager.chrome           import ChromeDriverManager

def open_browser():
    servic = Service("drivers/chromedriver.exe")
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach",True)
    driver = webdriver.Chrome(service=servic,options=option)
    return driver

def bpcl_url():
    driver.get("https://ebiz.bpc.co.in/VendorRegistration/Account")
    driver.find_element(By.NAME,"UserName").send_keys("188373")
    driver.find_element(By.NAME,"Password").send_keys("Test@123")
    #driver.find_element(By.NAME,"submit1").click()

def iocl_url():
    driver.get("https://associates.indianoil.co.in/BTS/vendor_login")
    driver.find_element(By.NAME,"txtuserid").send_keys("188373")
    driver.find_element(By.NAME,"txtpwd").send_keys("Test@123")

def hpcl_url():
    driver.get("https://bills.hpcl.co.in/Vendor/index.jsp")
    driver.find_element(By.NAME,"username").send_keys("188373")
    driver.find_element(By.NAME,"password").send_keys("Test@123")
    #driver.find_element(By.NAME,"submit1").click()

url = sys.argv[1]

driver = open_browser()
match url:
    case 'BPCL':
        bpcl_url()
    case 'HPCL':
        hpcl_url()
    case 'IOCL':
        iocl_url()

