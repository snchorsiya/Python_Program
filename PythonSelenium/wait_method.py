import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chr_option = Options()
chr_option.add_experimental_option("detach", True)
service = ChromeService(executable_path=r"D:\Automation\PythonAutomation\chromedriver-win32\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chr_option)
driver.implicitly_wait(5)
# 5 Seconds in max time out 2 seconds (3 seconds save)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

title = driver.title
print(title)

driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")
time.sleep(2)

results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
print(count)
assert count > 0

for result in results:
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# time.sleep(3)
driver.find_element(By.XPATH, "//input[@placeholder='Enter promo code']").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME, "promoBtn").click()
# time.sleep(7)
verify_code = driver.find_element(By.CLASS_NAME, "promoInfo").text
print(verify_code)

driver.find_element(By.XPATH, "//button[text()='Place Order']").click()


driver.quit()