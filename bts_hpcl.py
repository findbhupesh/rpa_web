from selenium import webdriver
from selenium.webdriver.chrome.service  import Service
from selenium.webdriver.common.keys     import Keys
from selenium.webdriver.common.by       import By
from webdriver_manager.chrome           import ChromeDriverManager
servic = Service("chromedriver.exe")
option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=servic,options=option)
driver.get("https://bills.hpcl.co.in/Vendor/index.jsp")
driver.find_element(By.NAME,"username").send_keys("188373")
driver.find_element(By.NAME,"password").send_keys("Test@123")
#driver.find_element(By.NAME,"submit1").click()
