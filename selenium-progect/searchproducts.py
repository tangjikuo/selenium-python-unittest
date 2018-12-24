from selenium import webdriver
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

driver.get("http://demo.magentocommerce.com/")

search_field=driver.find_element_by_name("q")
sraech_field.submit()

products = driver.find_element_by_xpath("//h2[@calss='product-name']/a")

print "Found" + str(len(products)) + "products:"

for product in products:
	print product.text

driver.quit()

