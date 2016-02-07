from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
driver.implicitly_wait(2) # seconds
driver.get('https://ipn.paymentus.com/epd/stde/tcnc')


# landing page
driver.find_element_by_name("loginId").send_keys("PUT YOUR LOGIN HERE")
driver.find_element_by_name("password").send_keys("PUT YOUR PASSWORD HERE") # warning! raw password

driver.find_element_by_name("continue").submit()


# logged-in
bill_amount = driver.find_element_by_css_selector("tr.search_cell_1:nth-child(4) > td:nth-child(3)").text
driver.find_element_by_link_text("Pay").click() # click Pay link
Select(driver.find_element_by_name("paymentMethodCategory")).select_by_index(1) # select credit card not debt
Select(driver.find_element_by_name("paymentMethod.type")).select_by_index(1) # select credit card type
driver.find_element_by_name("paymentMethod.accountNumber").send_keys("PUT YOUR CC HERE") # warning! raw credit card number
driver.find_element_by_name("paymentMethod.cvv").send_keys("PUT YOUR CVV HERE") # warning! raw cvv
Select(driver.find_element_by_name("paymentMethod.creditCardExpiryDate.month")).select_by_index(0) # PUT EXPIRATION MONTH HERE
Select(driver.find_element_by_name("paymentMethod.creditCardExpiryDate.year")).select_by_index(0) # PUT EXPIRATION YEAR HERE

paymentAmount = driver.find_element_by_name("header.paymentAmount")
paymentAmount.clear()
paymentAmount.send_keys(bill_amount[1:])
paymentAmount.submit()


# payment confirmation
driver.find_element_by_name("header.acceptTermsAndConditions").click()
# driver.find_element_by_name("submitBtn").submit() # uncomment to auto submit final step. leave if you would like to click it yourself


print("End. \nPaid: ")
print(bill_amount)
