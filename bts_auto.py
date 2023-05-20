import sys,time
from selenium                       import webdriver
from selenium.webdriver.support.ui  import WebDriverWait
from lib                            import bpcl,hpcl,iocl

def open_browser():
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach",True)
    option.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=option)
    return driver

driver = open_browser()
driver.implicitly_wait(10)


if  len(sys.argv) > 1:
    url = sys.argv[1]
else:
    url = 'HPCL'

match url:
    case 'BPCL':
        bpcl.upld_inv(driver)
    case 'HPCL':
        hpcl.upld_inv(driver)
    case 'IOCL':
        iocl.upld_inv(driver)

