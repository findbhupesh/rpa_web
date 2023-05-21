import sys,time
from selenium                       import webdriver
from selenium.webdriver.support.ui  import WebDriverWait
from lib                            import bpcl,hpcl,iocl,auto

web = auto.open_browser()
web.implicitly_wait(15)

if  len(sys.argv) > 1:
    url = sys.argv[1]
else:
    url = 'HPCL'

match url:
    case 'BPCL':
        bpcl.upld_inv(web)
    case 'HPCL':
        hpcl.upld_inv(web)
    case 'IOCL':
        iocl.upld_inv(web)

