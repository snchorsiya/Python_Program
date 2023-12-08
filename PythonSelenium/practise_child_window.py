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
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.find_element(By.XPATH, "//a[@class= 'blinkingText']").click()

window_open = driver.window_handles
driver.switch_to.window(window_open[1])

mes = driver.find_element(By.CSS_SELECTOR, ".red").text
print(mes)
var = mes.split("at")[1].strip().split(" ")[0]
print(var)
driver.close()

driver.switch_to.window(window_open[0])

driver.find_element(By.NAME, "username").send_keys(var)
driver.find_element(By.NAME, "password").send_keys(var)
driver.find_element(By.ID, "signInBtn").click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)

driver.quit()