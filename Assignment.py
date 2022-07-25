from urllib import response
from seleniumwire import webdriver
from seleniumwire.utils import decode
import json
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_experimental_option('excludeSwitches',['enable-logging'])

path = 'C:\Program Files (x86)\chromedriver.exe'

driver = webdriver.Chrome(path,options=options)
driver.maximize_window()

url = 'https://food.grab.com/sg/en/'

driver.get(url=url)

location_input = driver.find_element(By.CLASS_NAME,'ant-input')
location_input.clear()
location_input.send_keys('312A Clementi Ave 4, Clementi Ridges - 312A Clementi Ave 4, Singapore, 121312')
search = driver.find_element(By.XPATH,'//*[@id="page-content"]/div[2]/div/button')
try:
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="page-content"]/div[2]/div/button'))).click()
except TimeoutException as e:
    print('Search click failed')




# while True:
#     try:
#         WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@class="ant-btn ant-btn-block"]'))).click()
#         print('loadmore clicked')
#     except Exception as e:
#         print('load failed')
#         break
        


while True:
    try:
        WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@class="ant-btn ant-btn-block"]'))).click()
        print("load more clicked")
        # for request in driver.requests:
        #     if request.response:
        #         if request.url.startswith('https://portal.grab.com/foodweb/v2/search'):
        #             response = request.response
        #             b = decode(response.body,response.headers.get('Content-Encoding','identity'))
        #             b = b.decode('utf-8')
        #             data = json.loads(b)
                    
        #             for i in data['searchResult']['searchMerchants']:
        #                 print(i['address']['name'],i['latlng'])
    except Exception as e:
        print("load completed")
        break

# time.sleep(3)

# time.sleep(2)
# for request in driver.requests:
#     if request.response:
#         if request.url.startswith('https://portal.grab.com/foodweb/v2/search'):
#             response = request.response
#             b = decode(response.body,response.headers.get('Content-Encoding','identity'))
#             b = b.decode('utf-8')
#             data = json.loads(b)
            
#             for i in data['searchResult']['searchMerchants']:
#                 print(i['address']['name'],i['latlng'])

for request in driver.requests:
    if request.response:
        if request.url.startswith('https://portal.grab.com/foodweb/v2/category?'):
            b = json.loads(decode(request.response.body,request.response.headers.get('Content-Encoding','identity')).decode('utf-8'))
            
            for i in b['searchResult']['searchMerchants']:
               print(i['address']['name'],i['latlng'])
            

            


time.sleep(10)