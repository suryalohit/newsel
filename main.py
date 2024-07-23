import time



from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options




options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-extensions')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=options)
veg_dict = {}
veg_dict["width"] = 430
veg_dict["height"] = 932
veg_dict["deviceScaleFactor"] = 0
veg_dict["mobile"] = True
driver.execute_cdp_cmd("Emulation.setDeviceMetricsOverride",veg_dict)
driver.maximize_window()
driver.set_page_load_timeout(90)

# Load the URL and get the page source
driver.implicitly_wait(6)
driver.get("https://www.cricbuzz.com/")
time.sleep(5)
print(driver.get_screenshot_as_png())
for i in range(5):
  print(i)
  print(driver.title)
  time.sleep(2)
  

# ...
