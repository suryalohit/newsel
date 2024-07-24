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

print("3.1")
password.click()
print("3.2")
password.send_keys('Asailohit30@')
print("3,5")
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button'))).click()
time.sleep(10)


driver.get("https://x.com/home")

results={}
      #for i in range(1,10):
for i in range(1):
      veg_dict = {}
      veg_dict["width"] = 430
      veg_dict["height"] = 932
      veg_dict["deviceScaleFactor"] = 0
      veg_dict["mobile"] = True
      driver.execute_cdp_cmd("Emulation.setDeviceMetricsOverride",veg_dict)
      
      print(f"running round:{i}")
      try:
            driver.get("https://x.com/home")
            print("11")
            time.sleep(15)
            for space in list(results.keys()):
                  #unchecked
                  print(f"space name is : {space}")
                  print("5")
                  try:
                        print("6")
                        
                        driver.get(f'https://x.com/i/spaces/{space}/peek')
                        time.sleep(20)
                        print("7")
                        pf=driver.find_elements(By.CSS_SELECTOR, 'span.css-1jxf684.r-dnmrzs.r-1udh08x.r-3s2u2q.r-bcqeeo.r-1ttztb7.r-qvutc0.r-poiln3.r-1wvb978.r-1vr29t4')
                        print("8")
                        for p in range(1,len(pf)):
                              print("9")
                              results[space]["speaker"].add(pf[p].text)
                              print(pf[p].text)


                  except:
                        print("except")  
                        print(results[space])
                        del results[space]
            
            print("10")

            print(driver.get_screenshot_as_base64())
          
           
            print("login done1")
          
            available_spaces = driver.find_elements(By.CSS_SELECTOR, 'div.css-175oi2r.r-14tvyh0.r-cpa5s6.r-1gs4q39.r-11f147o.r-1akxima')
            print("2")
            print(f"total spaces available : {len(available_spaces)}")

            for spaces in available_spaces:
                  
                  print("3")
                  spaces.click()
                  print("4")
                  time.sleep(20)
                  print("5")
                  print("open the space")
                  
                  parts = driver.current_url.split('/')
                  spaceid = parts[5]
                  print(spaceid)
                  print("6")
                  if spaceid not in  list(results.keys()):
                        print("13")
                        ##
                        print(driver.get_screenshot_as_base64())
                        pf= driver.find_elements(By.CSS_SELECTOR, 'span.css-1jxf684.r-dnmrzs.r-1udh08x.r-3s2u2q.r-bcqeeo.r-1ttztb7.r-qvutc0.r-poiln3.r-1wvb978.r-1vr29t4')
                        print("7")
                        print(f"profiles nummber is : {len(pf)}")
                        print("8")
                        
                        
                        results[spaceid]={'host': "ajhgfd", 'speaker': set(), 'url': "z"}
                        print("1.2")
                        
                        
                        host=pf[0].text
                        results[spaceid]['host']=host
                        print(results[spaceid]['host'])
                        print("1.2.1")
                        
                        results[spaceid]['host']=str(pf[0].text)
                        print("1.3")
                        
                        
                        for p in range(1,len(pf)):
                              results[spaceid]['speaker'].add(pf[p].text)
                              print(pf[p].text)
                              
                        print("1.5.0")   
                        #annaon
                        print(driver.get_screenshot_as_base64())
                        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.r-30o5oe.r-1p0dtai.r-1pi2tsx.r-1d2f490.r-crgep1.r-t60dpp.r-u8s1d.r-zchlnj.r-ipm5af.r-13qz1uu.r-1ei5mc7'))).click()
                        #listen
                        time.sleep(2)
                        print("1.5.1")  
                        print(driver.get_screenshot_as_base64())
                        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.css-175oi2r.r-1udnf30.r-1uusn97.r-h3s6tt.r-1udh08x.r-13qz1uu.r-1loqt21.r-o7ynqc.r-6416eg.r-1ny4l3l.r-105ug2t'))).click()
                        print("1.5.2")  
                        
                        time.sleep(10)
                        print(driver.get_screenshot_as_base64())
                        results[spaceid]['url']=driver.wait_for_request('prod-fastly', timeout=12).url
                        print(results[spaceid]['url'])
                        print("1.7")
                        eees= driver.find_elements(By.XPATH, '//*[@id="layers"]/div[2]/div[2]/div/div/div/div[1]/div/div/div[1]/div[1]/div/button[4]')
                        print("7")
                        print(f"no of leave buttins is : {len(eees)}")
                        #end listen
                        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div[2]/div[2]/div/div/div/div[1]/div/div/div[1]/div[1]/div/button[4]'))).click()
                        time.sleep(4)
            
      except:
            print("except")
            
print(results)    
