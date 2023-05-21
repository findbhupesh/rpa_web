import time

from selenium.webdriver.support.ui      import WebDriverWait
from selenium.webdriver.support         import expected_conditions as EC
from lib                                import auto

def upld_inv(web):
    wait = WebDriverWait(web, 10)
    web.get("https://econnect.bpcl.in/selfservice-ext/pub/login.html")
    auto.send_keys(web,"//input[@id='principal']","VC157213")
    auto.send_keys(web,"//input[@id='input_password']","Baldist@2223")
    time.sleep(15)
    auto.click_btn(web,"//input[@value='Login']")
    win1 = web.current_window_handle
    time.sleep(5)
    auto.click_btn(web,"//div[text()='My Applications']")
    auto.click_btn(web,"//a[text()='Digital Invoice Management']")
    wait.until(EC.number_of_windows_to_be(2))
    for window_handle in web.window_handles:
        if window_handle != win1:
            web.switch_to.window(window_handle)
            break
    auto.send_keys(web,"//input[@id='PONumber']","4509584482")
    auto.send_keys(web,"//input[@id='InvoiceRefNo']","F22331336854")
    auto.click_btn(web,"//input[@id='InvoiceDate']")
    auto.click_btn(web,"//a[contains(text(),'20')]")
    auto.send_keys(web,"//input[@id='InvoiceAmount']","2018378.26")
    auto.click_btn(web,"//input[@id='PONumber']")
    auto.click_btn(web,"//button[contains(text(),'Proceed')]")
    auto.send_keys(web,"//input[@id='chooseFile']","C:\\temp\\inv_0091908544.pdf")
    auto.click_btn(web,"//input[@id='deliveryCheckBox']")