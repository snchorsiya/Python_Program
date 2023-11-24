from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

ch_option = Options()
ch_option.add_experimental_option("detach", True)
service = ChromService(executable_path=r"D:\Automation\PythonAutomation\chromedriver-win32\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=ch_option)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

title = driver.title
print(title)

# ID, XPATH, CSSSelector, LinkText, Name, ClassName, PartialLinkText,  TagName

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("qa")
driver.find_element(By.NAME, "email").send_keys("sn@yopmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Admin@123")
driver.find_element(By.XPATH, "//input[@class='btn btn-success']").click()

message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)

assert "Success" in message

# //tagname[@attribute="value"]

# driver.quit()