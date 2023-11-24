from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options

# ch_option = Options()
# ch_option.add_experimental_option("detach", True)
# ser_obj = Service()
# driver = webdriver.Chrome(service=ser_obj, options=ch_option)

# Chrome Browser
# ch_option = Options()
# ch_option.add_experimental_option("detach", True)
# ser_obj = Service(r"D:\Automation\PythonAutomation\chromedriver-win32\chromedriver.exe")
# driver = webdriver.Chrome(service=ser_obj, options=ch_option)

# Firefox Browser
# from selenium.webdriver.firefox.service import Service
# ser_obj = Service(r"D:\Automation\PythonAutomation\geckodriver-v0.33.0-win64\geckodriver.exe")
# driver = webdriver.Firefox(service=ser_obj)

from selenium.webdriver.ie.service import Service
ser_obj = Service(r"D:\Automation\PythonAutomation\edgedriver_win64\msedgedriver.exe")
driver = webdriver.Edge(service=ser_obj)

driver.get("https://www.saucedemo.com/")
driver.maximize_window()
title = driver.title
print(title)
url = driver.current_url
print(url)
driver.get("https://demo.opencart.com/")
driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()