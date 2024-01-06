import requests
from bs4 import BeautifulSoup
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

send_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

UID = ''  # 你的帳號
PW = ''  # 你的密碼
content = '蓋'  # 你蓋樓的內容


def starter():
    driver.get(URL)
    driver.find_element(By.ID, "postTips").click()
    time.sleep(0.3)
    ActionChains(driver).send_keys(content).perform()


URL = input('URL:')
floor_target = int(input('欲搶樓層:'))

if '&last=1' not in URL:
    URL += '&last=1'

driver = webdriver.Chrome(chrome_options=options)
driver.get('https://www.gamer.com.tw/')
driver.find_element(By.LINK_TEXT, "我要登入").click()
driver.find_element(By.NAME, "userid").send_keys(UID)
driver.find_element(By.NAME, "password").send_keys(PW)
driver.find_element(By.ID, "btn-login").click()
time.sleep(0.5)
starter()
os.system('cls')
while True:
    request = requests.get(URL, headers=send_headers)
    html = request.content
    bsObj = BeautifulSoup(html, 'html.parser')
    shouter = bsObj.findAll('a', {'class': 'floor'})
    for page in shouter:
        floor_now = page.get_text()
    print(floor_now)
    floor_now = int(floor_now[:-2])
    t = 60
    if floor_now >= floor_target:
        t = 60
        print('已超過目標樓層 請重新輸入下一欲搶樓層')
        floor_target = int(input('欲搶樓層:'))
        os.system('cls')
        starter()
        continue
    elif floor_target - floor_now <= 10:
        t = 0.4
    if floor_now == floor_target - 1:
        driver.find_element(By.CLASS_NAME, "btn--send").click()
        time.sleep(0.3)
        driver.find_element(By.CLASS_NAME, "btn-primary")
        try:
            driver.find_element(By.CLASS_NAME, "btn-primary").click()
        except:
            pass
        print("已發文")
    time.sleep(t)
