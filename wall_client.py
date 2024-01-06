from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

UID = input('UID: ')
PW = input('PW: ')

driver = webdriver.Chrome()
driver.get("https://wall.gamer.com.tw/")

driver.find_element(By.ID, "uidh").send_keys(UID)
driver.find_element(By.NAME, "passwdh").send_keys(PW)
driver.find_element(
    By.CSS_SELECTOR, ".form__buttonbar:nth-child(6) > .btn--primary").click()
time.sleep(0.5)
while True:
    os.system('cls')
    content = input('content(換行請打\\n): ')
    driver.find_element(By.CSS_SELECTOR, ".sidebar_section_btn-post").click()
    driver.find_element(By.CSS_SELECTOR, ".input-main-editor-content").click()
    time.sleep(0.5)
    element = driver.find_element(
        By.CSS_SELECTOR, ".input-main-editor-content")
    driver.execute_script(
        "if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '"+content+" '}", element)
    driver.find_element(By.CSS_SELECTOR, ".input-main-editor-content").click()
    driver.find_element(
        By.CSS_SELECTOR, ".input-main-editor-content").send_keys(Keys.BACK_SPACE)
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, ".btn").click()
    driver.execute_script("window.scrollTo(0,0)")
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
