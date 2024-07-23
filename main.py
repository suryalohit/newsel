import time



from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument("start-maximized")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-extensions')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=options)

driver.set_window_size(1150, 780)
driver.set_page_load_timeout(90)

# Load the URL and get the page source
driver.implicitly_wait(6)
driver.get("https://x.com/i/flow/login")
time.sleep(5)

print("1")
print(driver.get_screenshot_as_base64())
username = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "text")))
username.click()
username.send_keys('devikagoud245@gmail.com')
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/button[2]'))).click()
time.sleep(7)

try:
     
      print("2")
      print(driver.get_screenshot_as_base64())
      check = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "text")))
      print("2.0")
      check.click()
      check.send_keys('retiredHippo')
      print("2.22")
      st=driver.find_element("xpath",'//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/button')
      st.click()
      time.sleep(7)
      print("2.1")
    

except:
      print("except")


print("3")
print(driver.get_screenshot_as_base64())
password =WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "password")))
password.click()
password.send_keys('Asailohit30@')
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div/button'))).click()
time.sleep(5)

print("15")
print(driver.get_screenshot_as_base64())
print("login done")
  

# ...
