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

# driver.find_element(By.NAME, "checkBoxOption2").click()

click_checkbox_btn = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(click_checkbox_btn))

for checkbox_btn in click_checkbox_btn:
    if checkbox_btn.get_attribute("value") == "option3":
        checkbox_btn.click()
        checkbox_btn.is_selected()
        print("The checkbox selected or not?...", checkbox_btn.is_selected())
        break


print("===================Handling the radio button===================")

# click_radio_btn = driver.find_elements(By.XPATH, "//input[@type='radio']")
# print(len(click_radio_btn))
#
# for radio_btn in click_radio_btn:
#     if radio_btn.get_attribute("value") == "radio2":
#         radio_btn.click()
#         radio_btn.is_selected()
#         print("The checkbox selected or not?...", radio_btn.is_selected())
#         radio_btn.clear()
#         break

radioButton = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radioButton[2].click()
assert radioButton[2].is_selected()

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
# assert driver.find_element(By.ID, "displayed-text").is_displayed()
time.sleep(2)
driver.find_element(By.ID, "show-textbox").click()
assert driver.find_element(By.ID, "displayed-text").is_displayed()