from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Chrome Options
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


# test case 1 login for admin
driver.get('http://13.233.247.58/admin/index.php')
driver.maximize_window()

driver.find_element(By.XPATH, '//input[@name="email"]').send_keys('admin@gmail.com')

driver.find_element(By.XPATH, '//input[@name="pwd"]').send_keys('Admin123')
driver.find_element(By.XPATH, '//input[@value="Login"]').click()
time.sleep(2)
#test case 2 add employee
driver.find_element(By.XPATH, '//i[@class="fa fa-user"]').click()
driver.find_element(By.XPATH, '//a[@href="add-employee.php"]').click()
driver.find_element(By.XPATH, '//input[@name="firstname"]').send_keys('hammad')
driver.find_element(By.XPATH, '//input[@name="lastname"]').send_keys('idrees')
driver.find_element(By.XPATH, '//input[@name="emailid"]').send_keys('hammad@gmail.com')
driver.find_element(By.XPATH, '//input[@name="pwd"]').send_keys('abc12345')
driver.find_element(By.XPATH, '//select[@name="department"]').click()
driver.find_element(By.XPATH, '//select[@name="department"]').send_keys(Keys.DOWN,Keys.RETURN)

driver.find_element(By.XPATH, '//button[@type="submit"]').click()





