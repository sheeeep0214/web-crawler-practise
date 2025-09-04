from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
driver.get("https://sys.ndhu.edu.tw/gc/sportcenter/SportsFields/login.aspx")
user_name=driver.find_element("name","ctl00$MainContent$TxtUSERNO")
user_name.send_keys("411321218")
user_password=driver.find_element("name","ctl00$MainContent$TxtPWD")
user_password.send_keys("30118ddgg")
user_password.send_keys(Keys.RETURN)
time.sleep(3)
driver.quit()