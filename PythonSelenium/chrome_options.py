from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#
# chr_option = Options()
# chr_option.add_experimental_option("detach", True)

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("--start-maximized")
chrome_option.add_argument("headless")
chrome_option.add_argument("--ignore-certificate-errors")
chrome_option.add_experimental_option("detach", True)
service = ChromeService(executable_path=r"D:\Python_Program-master\Python_Program-master\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_option)


driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
# driver.maximize_window()
title = driver.title
print(title)