from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chr_option = Options()
chr_option.add_experimental_option("detach", True)
service = ChromeService(executable_path=r"D:\Python_Program-master\Python_Program-master\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chr_option)


driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()
title = driver.title
print(title)

# click on column header

driver.find_element(By.XPATH, "//th[@aria-label='Veg/fruit name: activate to sort column ascending']").click()

# collect all veggie names -> BrowserSortedveggieList (B, A, C)
browserSortedVeggies = []
list_veg = driver.find_elements(By.XPATH, "//table/tbody/tr/td[1]")
for veg in list_veg:
    browserSortedVeggies.append(veg.text)

originalbrowserSortedList = browserSortedVeggies.copy()

# Sort this veggieList => newSortedList -> (A, B, C)
browserSortedVeggies.sort()
# veggieList == newSortedList

assert browserSortedVeggies == originalbrowserSortedList

