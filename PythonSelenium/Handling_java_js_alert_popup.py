import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chr_option = Options()
chr_option.add_experimental_option("detach", True)
service = ChromeService(executable_path=r"D:\Automation\PythonAutomation\chromedriver-win32\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chr_option)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()
name = "Sheetal"
driver.find_element(By.ID, "name").send_keys(name)
time.sleep(2)
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert name in alertText
alert.accept()
time.sleep(3)
driver.find_element(By.ID, "name").send_keys(name)
time.sleep(2)
driver.find_element(By.ID, "confirmbtn").click()
confirm_alert = driver.switch_to.alert
confirm_alert_text = confirm_alert.text
print(confirm_alert_text)
time.sleep(2)
confirm_alert.dismiss()
# confirm_alert.accept()
driver.quit()



