from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chr_option = Options()
chr_option.add_experimental_option("detach", True)
service = ChromeService(executable_path=r"D:\Python_Program-master\Python_Program-master\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chr_option)

driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
title = driver.title
print(title)

driver.find_element(By.LINK_TEXT, "Shop").click()

title = driver.title
print("Click on After Shop link", title)

all_phone = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
for phone in all_phone:
    product_name = phone.find_element(By.XPATH, "div/h4/a").text
    if product_name == "Blackberry":
        phone.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

driver.find_element(By.XPATH, "//button[normalize-space()='Checkout']").click()

driver.find_element(By.ID, "country").send_keys("Ind")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()

driver.find_element(By.XPATH, "//input[@value='Purchase']").click()

sueessText = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text

assert "Success! Thank you!" in sueessText

driver.quit()