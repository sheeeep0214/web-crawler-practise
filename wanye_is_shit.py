from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver=webdriver.Chrome()
driver.get("https://sys.ndhu.edu.tw/SA/XSL_ApplyRWD/ActApply.aspx")
def get_page():
    page = driver.find_elements(By.CSS_SELECTOR, "[href^=\"javascript:__doPostBack('ctl00$BodyContent$gvActs','Page$\"]")
    return page

def get_act_name():
    page=len(get_page())
    act_name=[]
    for clicker in range(0,page):
        act_names=driver.find_elements(By.CSS_SELECTOR, "[id^='BodyContent_gvActs_lblGv_act_name_']")
        for act_title in act_names:
            act_name.append(act_title.text)
        click_page=get_page()
        time.sleep(0.001)
        click_page[clicker].click()
        time.sleep(0.001)
    return act_name

act_name=get_act_name()
for act_title in act_name:
    print(act_title)
