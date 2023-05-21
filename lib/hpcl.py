import time
from easygui import msgbox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support    import expected_conditions as EC
from lib                           import auto

def upld_inv(web):
    wait = WebDriverWait(web, 10)
    web.get("https://bills.hpcl.co.in/Vendor/index.jsp")
    auto.send_keys(web,"//input[@id='username']","28084998")
    auto.send_keys(web,"//input[@id='password']","balhpcl@18")
    time.sleep(15)
    auto.click_btn(web,"//input[@id='submit1']")

    auto.click_btn(web,"//button[contains(text(),'Continue')]")
    auto.click_btn(web,"//button[contains(text(),'Continue')]")
    win1 = web.current_window_handle
    auto.click_btn(web,"//a[contains(text(),'e-Invoice')]")
    auto.click_btn(web,"//a[@href='create_tx.jsp']")
    
    wait.until(EC.number_of_windows_to_be(2))
    for window_handle in web.window_handles:
        if window_handle != win1:
            web.switch_to.window(window_handle)
            break
  
    auto.click_btn(web,"//span[contains(@title,'Select Purchase Order')]")
    auto.send_keys(web,"//input[@class='select2-search__field']",'22000197-OP-11350')
    auto.click_btn(web,"//li[contains(@id,'22000197-OP-11350')]")
    auto.send_keys(web,"//input[@id='bill_no']",'F22331337172')
    auto.click_btn(web,"//input[@id='bill_dt']")
    auto.click_btn(web,"//a[contains(text(),'20')]")
    auto.send_keys(web,"//input[@id='taxable_amt']",'2651400.00')
    auto.send_keys(web,"//input[@id='tax_amt']",'132570.00')
    auto.send_keys(web,"//input[@id='bill_amt']",'2783970.00')
    auto.click_btn(web,"//span[@id='select2-locnnm-container']")
    auto.send_keys(web,"//input[@class='select2-search__field']","11588")
    auto.click_btn(web,"//li[contains(text(),'11588')]")
    auto.click_btn(web,"//span[@id='select2-creator_mail-container']")
    auto.click_btn(web,"//li[contains(@id,'30076000')]")
    auto.send_keys(web,"//input[@id='scan_page']",'4')
    auto.send_keys(web,"//input[@id='challan_no']",'0092741240')
    auto.send_keys(web,"//input[@id='digitalInvoiceFile']","C://temp/inv_0091908544.pdf")
    auto.send_keys(web,"//textarea[@id='creator_rem']","This is test remark")
    auto.click_btn(web,"//input[@id='chkk']")
    auto.click_btn(web,"//input[@value='check']")
    #auto.click_btn(web,"//input[@id='submit2']")