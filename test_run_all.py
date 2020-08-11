from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com")
time.sleep(2)
driver.find_element_by_id("kw").send_keys("python自动化")
time.sleep(5)
driver.find_element_by_id("su").click()
time.sleep(5)

result = driver.find_element_by_id("su")
result_data = result.get_attribute('value')
print(result_data)
assert result_data == "百度一下"
print("success")
time.sleep(5)
driver.quit()

    

