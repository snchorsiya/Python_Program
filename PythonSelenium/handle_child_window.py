from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement
from selenium.webdriver.support.select import Select

chr_option = Options()
chr_option.add_experimental_option("detach", True)
service = ChromeService(executable_path=r"D:\Automation\PythonAutomation\chromedriver-win32\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chr_option)

driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()

title = driver.title
print(title)

parent_window_text = driver.find_element(By.CSS_SELECTOR, "div[class='example'] h3").text
print(parent_window_text)

click_parent_window = driver.find_element(By.CSS_SELECTOR, "a[href='/windows/new']")
click_parent_window.click()

windows_open = driver.window_handles

driver.switch_to.window(windows_open[1])
child_window = driver.find_element(By.TAG_NAME, "h3").text
driver.close()
print(child_window)
driver.switch_to.window(windows_open[0])
print(driver.find_element(By.XPATH, "//a[normalize-space()='Elemental Selenium']").text)

driver.quit()