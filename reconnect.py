from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def example(query):
    browser = webdriver.Chrome()

    browser.get(query)
    password = ""  # put here your vodafone station password

    WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login_Password"]')))

    search = browser.find_element_by_id("login_Password")
    search.click()
    search.send_keys(password)
    time.sleep(1)

    WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="btn_login"]')))
    searchBtn = browser.find_element_by_id("btn_login")
    searchBtn.click()
    time.sleep(1)

    WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH, '// *[ @ id = "status-and-support"]')))
    searchConfig = browser.find_element_by_xpath('// *[ @ id = "status-and-support"]')
    searchConfig.click()
    time.sleep(1)

    WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH, '// *[ @ id = "status-and-support_restart"] / a')))
    searchRebot = browser.find_element_by_xpath('// *[ @ id = "status-and-support_restart"] / a')
    searchRebot.click()
    time.sleep(1)

    WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH, '// *[ @ id = "dsl_btn_reconnect"]')))
    searchReconnect = browser.find_element_by_xpath('// *[ @ id = "dsl_btn_reconnect"]')
    searchReconnect.click()

    time.sleep(5)  # sleep for 5 seconds so you can see the results

    browser.quit()


example("http://192.168.1.1/main.cgi?page=login.html")
