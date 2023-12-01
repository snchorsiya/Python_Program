import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

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

expected_list = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
actual_list = []

# product_name = driver.find_elements(By.XPATH, "//h4[@class='product-name']")
# for product in product_name:
#     print("The product name is:", product.text)
#
# assert product_name == expected_list

results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
print(count)
assert count > 0

for result in results:
    actual_list.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH, "div/button").click()
print(actual_list)
assert expected_list == actual_list

driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# Some validation
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
add = 0
for price in prices:
    add = add + int(price.text)
print("The total amount of:", add)

totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

assert add == totalAmount

# time.sleep(3)

driver.find_element(By.XPATH, "//input[@placeholder='Enter promo code']").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME, "promoBtn").click()
# time.sleep(7)
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
verify_code = driver.find_element(By.CLASS_NAME, "promoInfo").text
print(verify_code)

discount_amount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)

assert totalAmount > discount_amount

driver.find_element(By.XPATH, "//button[text()='Place Order']").click()


driver.quit()