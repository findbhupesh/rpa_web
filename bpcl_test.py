from selenium import webdriver
from selenium.webdriver.chrome.service  import Service
from selenium.webdriver.common.keys     import Keys
from selenium.webdriver.common.by       import By
from webdriver_manager.chrome           import ChromeDriverManager
servic = Service("drivers/chromedriver.exe")
option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=servic,options=option)
driver.get("https://ebiz.bpc.co.in/VendorRegistration/Account")
driver.find_element(By.NAME,"UserName").send_keys("188373")
driver.find_element(By.NAME,"Password").send_keys("Test@123")
#driver.find_element(By.NAME,"submit1").click()