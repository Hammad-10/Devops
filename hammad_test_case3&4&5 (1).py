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
driver.get('http://13.233.247.58/')
driver.maximize_window()

driver.find_element(By.XPATH, '//input[@name="email"]').send_keys('hammad@gmail.com')

driver.find_element(By.XPATH, '//input[@name="pwd"]').send_keys('abc12345')
driver.find_element(By.XPATH, '//input[@value="Login"]').click()
time.sleep(2)
#test case 4
# driver.find_element(By.XPATH, '//input[@name="dates"]').send_keys('11112001')
# time.sleep(2)

\
#test case 5
driver.find_element(By.XPATH, '//i[@class="fas fa-user"]').click
driver.find_element(By.XPATH, '//a[@href="logout.php"]').click




