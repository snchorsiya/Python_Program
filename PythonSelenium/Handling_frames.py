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
driver.get("https://the-internet.herokuapp.com/frames")
driver.maximize_window()

title = driver.title
print(title)

driver.find_element(By.LINK_TEXT, "iFrame").click()

# iframlist = driver.find_elements(By.TAG_NAME, "iframe")
# cont = len(iframlist)
# print(cont)
name = driver.find_element(By.TAG_NAME, "h3").text
print(name)
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("I am able to automate frame")

driver.switch_to.default_content()
name = driver.find_element(By.TAG_NAME, "h3").text
print("After switch the default:", name)

driver.quit()