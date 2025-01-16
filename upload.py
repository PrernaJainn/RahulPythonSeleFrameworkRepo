#file downloaded in Excel format
#Double quotes " are used for the outer string, while single quotes ' are used inside the XPath expression around fruit_name.
#The square bracket notation for @id remains enclosed in double quotes within the string.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

file_path='C:\\Users\\prerna.jain\\Downloads\\download.xlsx'  #file path store in a variable
fruit_name="Mango"
driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
driver.find_element(By.ID, "downloadButton").click()

# edit the Excel with the updated values (type = file should show in css to identify)
file_input=driver.find_element(By.CSS_SELECTOR, " input[type='file']")
file_input.send_keys(file_path)

wait=WebDriverWait(driver, 5)
toast_locator=(By.CSS_SELECTOR, ".Toastify__toast-body div:nth-child(2)")
wait.until(EC.visibility_of_element_located(toast_locator))
print(driver.find_element(*toast_locator).text)

#<div id="cell-4-undefined" data-column-id="4" role="cell" class="sc-hLQSwg sc-eDLKkx sc-jTQCzO kyDEvf gfKXFa cJTPDY rdt_TableCell" data-tag="allowRowEvents" xpath="1"><div data-tag="allowRowEvents" style="">345</div></div>
#"//div[text()='Apple']/parent::div/parent::div/div[@id='cell-4-undefined']") selecting the full row using this xpath and
# If you want to use dynamic fruit name instead of apple using '" +fruit_name_+ "'  it work for any fruit
#incase value of change so capture it from table Price column text using get attribute and get the price of the fruit dynamically

priceColumn=driver.find_element(By.XPATH, "//div[text()='Price']").get_attribute("data-column-id")
actual_price=driver.find_element(By.XPATH,
                                 "//div[text()='" + fruit_name + "']/parent::div/parent::div/div[@id='cell-" + str(
                                     priceColumn) + "-undefined']").text

print(actual_price, "Price of the fruit is :")
