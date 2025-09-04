from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.google.com/?hl=zh_TW")
print(driver.title)
driver.quit()