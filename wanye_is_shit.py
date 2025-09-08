from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://sys.ndhu.edu.tw/SA/XSL_ApplyRWD/ActApply.aspx")
#控制每次休眠時間，以免網頁未載入完全發生錯誤
def sleep():
    time.sleep(0.5)
#取得翻頁元素
def get_page():
    page = driver.find_elements(By.CSS_SELECTOR, "[href^=\"javascript:__doPostBack('ctl00$BodyContent$gvActs','Page$\"]")
    return page
#將網頁翻至下一頁
def next_page(clicker,page):
    if clicker<page:
            click_page=get_page()
            sleep()
            click_page[clicker].click()
            sleep()
#將網頁翻回第一頁
def back_to_first_page():
    sleep()
    reset_page = driver.find_element(By.CSS_SELECTOR,  'a[href="javascript:__doPostBack(\'ctl00$BodyContent$gvActs\',\'Page$1\')"]')
    reset_page.click()
    sleep()
#取得活動名稱
def get_act_name():
    page=len(get_page())
    act_name=[]
    for clicker in range(0,page+1):
        act_names=driver.find_elements(By.CSS_SELECTOR, "[id^='BodyContent_gvActs_lblGv_act_name_']")
        for act_title in act_names:
            act_name.append(act_title.text)
        next_page(clicker,page)
    back_to_first_page()
    return act_name
#判斷能否參與(額滿/資工學生不能參與/沒時數 皆判定為無法參與，結果不會輸出該活動)
def can_wayne_join():
    page=len(get_page())
    can_join=[]
    part_index=hour_index=0
    for clicker in range(0,page+1):
        nember=driver.find_elements(By.CSS_SELECTOR, "[id^='BodyContent_gvActs_lblGv_reg_num_']")
        department=driver.find_elements(By.CSS_SELECTOR, "[id^='BodyContent_gvActs_lblGv_participant_']")
        hours=driver.find_elements(By.CSS_SELECTOR, "[id^='BodyContent_gvActs_lblGv_xsl_check_']")
        for join in nember:
            joiner=join.text[:-1].split(" / ")
            if joiner[0]=="正取":
                continue
            if int(joiner[0])>=int(joiner[1]):
                can_join.append(0)
            else:
                can_join.append(1)
        for part in department:
            if "限本系" in part.text:
               can_join[part_index]=0
            part_index+=1
        for hour in hours:
            if hour.text=="不可":
                can_join[hour_index]=0
            hour_index+=1
        next_page(clicker,page)
    back_to_first_page()
    return can_join
#取得活動時間
def act_date():   
    page=len(get_page())
    act_dates=[]
    for clicker in range(0,page+1):
        date=driver.find_elements(By.CSS_SELECTOR, "[id^='BodyContent_gvActs_lblGv_act_dt_']")
        for times in date:
            act_dates.append(times.text)
        next_page(clicker,page)
    sleep()
    back_to_first_page()
    return act_dates 
#主程式(輸出活動名稱與時間)
act_names=get_act_name()
act_dates=act_date()
can_join=can_wayne_join()
for index in range (0,len(act_names)):
    if can_join[index]:
        print(f"活動名稱:{act_names[index]}\n活動時間:{act_dates[index]}\n")