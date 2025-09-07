from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://sys.ndhu.edu.tw/SA/XSL_ApplyRWD/ActApply.aspx")

def get_page():
    page = driver.find_elements(By.CSS_SELECTOR, "[href^=\"javascript:__doPostBack('ctl00$BodyContent$gvActs','Page$\"]")
    return page

def get_act_name():
    page=len(get_page())
    act_name=[]
    for clicker in range(0,page+1):
        act_names=driver.find_elements(By.CSS_SELECTOR, "[id^='BodyContent_gvActs_lblGv_act_name_']")
        for act_title in act_names:
            act_name.append(act_title.text)
        if clicker<page:
            click_page=get_page()
            time.sleep(1.5)
            click_page[clicker].click()
            time.sleep(1.5)
    time.sleep(1.5)
    reset_page = driver.find_element(By.CSS_SELECTOR,  'a[href="javascript:__doPostBack(\'ctl00$BodyContent$gvActs\',\'Page$1\')"]')
    reset_page.click()
    return act_name

def can_wayne_join():
    page=len(get_page())
    can_join=[]
    for clicker in range(0,page+1):
        nember=driver.find_elements(By.CSS_SELECTOR, "[id^='BodyContent_gvActs_lblGv_reg_num_']")
        for join in nember:
            joiner=join.text[:-1].split(" / ")
            if joiner[0]=="正取":
                continue
            if int(joiner[0])>=int(joiner[1]):
                can_join.append(0)
            else:
                can_join.append(1)
        if clicker<page:
            click_page=get_page()
            time.sleep(1.5)
            click_page[clicker].click()
            time.sleep(1.5)
    time.sleep(1.5)
    reset_page = driver.find_element(By.CSS_SELECTOR,  'a[href="javascript:__doPostBack(\'ctl00$BodyContent$gvActs\',\'Page$1\')"]')
    reset_page.click()
    index=0
    for clicker in range(0,page+1):
        department=driver.find_elements(By.CSS_SELECTOR, "[id^='BodyContent_gvActs_lblGv_participant_']")
        for part in department:
            if_only_department=part.text
            if "限本系" in if_only_department:
               can_join[index]=0
            index+=1
        if clicker<page:
            click_page=get_page()
            time.sleep(1.5)
            click_page[clicker].click()
            time.sleep(1.5)
    return can_join

def act_date():   
    page=len(get_page())
    act_dates=[]
    for clicker in range(0,page+1):
        date=driver.find_elements(By.CSS_SELECTOR, "[id^='BodyContent_gvActs_lblGv_act_dt_']")
        for times in date:
            act_dates.append(times.text)
        if clicker<page:
            click_page=get_page()
            time.sleep(1.5)
            click_page[clicker].click()
            time.sleep(1.5)
    time.sleep(1.5)
    reset_page = driver.find_element(By.CSS_SELECTOR,  'a[href="javascript:__doPostBack(\'ctl00$BodyContent$gvActs\',\'Page$1\')"]')
    reset_page.click()
    return act_dates 

act_names=get_act_name()
act_dates=act_date()
can_join=can_wayne_join()
for index in range (0,len(act_names)):
    if can_join[index]:
        print(f"活動名稱:{act_names[index]}\n活動時間:{act_dates[index]}\n")