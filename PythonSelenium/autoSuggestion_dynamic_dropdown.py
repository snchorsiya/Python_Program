import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chr_option = Options()
chr_option.add_experimental_option("detach", True)

service = ChromeService(executable_path=r"D:\Automation\PythonAutomation\chromedriver-win32\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chr_option)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()

title = driver.title
print(title)

# Autosuggestion dropdown
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break

# get dynamic value in text
# assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"
print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))

# driver.quit()