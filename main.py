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
time.sleep(10)

print("1")
print(driver.get_screenshot_as_base64())
username = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "text")))
username.click()
username.send_keys('devikagoud245@gmail.com')
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]'))).click()
time.sleep(7)

try:
     
      print("2")
      print(driver.get_screenshot_as_base64())
      check = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "text")))
      print("2.0")
      check.click()
      check.send_keys('retiredHippo')
      print("2.22")
      st=driver.find_element("xpath",'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button')
      st.click()
      time.sleep(10)
      print("2.1")
    

except:
      print("except")


print("3")
print(driver.get_screenshot_as_base64())
password =WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "password")))
password.click()
password.send_keys('Asailohit30@')
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button'))).click()
time.sleep(15)
print("15")
print(driver.get_screenshot_as_base64())
print("login done")

veg_dict = {}
veg_dict["width"] = 430
veg_dict["height"] = 932
veg_dict["deviceScaleFactor"] = 0
veg_dict["mobile"] = True
driver.execute_cdp_cmd("Emulation.setDeviceMetricsOverride",veg_dict)

time.sleep(15)
print("16")
print(driver.get_screenshot_as_base64())
print("login done1")
  

# ...
