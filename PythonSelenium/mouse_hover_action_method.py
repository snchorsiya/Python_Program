from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chr_option = Options()
chr_option.add_experimental_option("detach", True)
service = ChromeService(executable_path=r"D:\Automation\PythonAutomation\chromedriver-win32\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chr_option)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

title = driver.title
print(title)

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
# action.double_click()
action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
# action.drag_and_drop()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
