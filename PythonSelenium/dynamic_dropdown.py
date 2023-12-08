import time

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
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()

title = driver.title
print(title)

driver.find_element(By.ID, "autosuggest").send_keys("ind")

country_list=driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item']")
count=len(country_list)
print("Number of country list display:", count)

for country in country_list:
    if country.text == "India":
        country.click()
        break

print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))

radio_button=driver.find_elements(By.XPATH, "//input[@type='radio']")
print("Number of radio button:", len(radio_button))

for radio_btn in radio_button:
    if radio_btn.get_attribute("value") == "RoundTrip":
        radio_btn.click()
        print("Radio button click or not?", radio_btn.is_selected())
        break

driver.find_element(By.NAME, "ctl00_mainContent_ddl_originStation1_CTXT").send_keys("AMD")
to_address = driver.find_element(By.NAME, "ctl00_mainContent_ddl_destinationStation1_CTXT")
to_address.click()
# send_keys("GOI")

list_address = driver.find_elements(By.XPATH, "//div[@id='ctl00_mainContent_ddl_destinationStation1_CTNR']//ul//li//a")
count = len(list_address)
print("Number of city display:", count)

for address in list_address:
    if address.text == "Surat (STV)":
        address.click()
        break

print("Selected To address:", driver.find_element(By.NAME, "ctl00_mainContent_ddl_destinationStation1_CTXT").get_attribute("value"))

driver.find_element(By.NAME, "ctl00$mainContent$view_date1").click()

cale_date = driver.find_elements(By.XPATH, "//div[contains(@class,'ui-datepicker-group ui-datepicker-group-first')]")
# cale_date = driver.find_elements(By.XPATH, "//td[@data-handler='selectDay']")
print(len(cale_date))

fromYear = "December"
fromMonth = 2023
fromDate = 23

for cal in cale_date:
    if cal.text == fromYear:
        if cal.text == fromMonth:
            if cal.text == fromDate:
                cal.click()
                break
        else:
            driver.find_element(By.XPATH, "//a[@title='Next']").click()


# driver.quit()
