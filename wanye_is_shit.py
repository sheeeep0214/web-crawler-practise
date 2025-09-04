from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://sys.ndhu.edu.tw/SA/XSL_ApplyRWD/ActApply.aspx")
act_name=driver.find_elements(By.TAG_NAME,"span")
for i in act_name:
    print(i.text)