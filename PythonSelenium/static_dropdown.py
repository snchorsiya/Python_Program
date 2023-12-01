from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chr_option = Options()
chr_option.add_experimental_option("detach", True)

service = ChromeService(executable_path=r"D:\Automation\PythonAutomation\chromedriver-win32\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chr_option)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

genderDrp = Select(driver.find_element(By.XPATH, "//select[@id='exampleFormControlSelect1']"))
genderDrp.select_by_visible_text("Female")

driver.quit()
