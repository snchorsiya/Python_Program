from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")

chrome_options.add_argument("--ignore-certificate-errors")

# chr_option = Options()
chrome_options.add_experimental_option("detach", True)
service = ChromeService(executable_path=r"D:\Python_Program-master\Python_Program-master\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

title = driver.title
print(title)

driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
driver.get_screenshot_as_file("screen1.png")