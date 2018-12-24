from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://mail.sina.com.cn/register/regmail.php")
driver.find_element_by_class_name("inputStyle").send_keys("tangjikuo123")

