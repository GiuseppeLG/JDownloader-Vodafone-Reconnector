from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def example(query, passwd):
    browser = webdriver.Chrome()

    browser.get(query)

    WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login_Password"]')))

    search = browser.find_element_by_id("login_Password")
    search.click()
    search.send_keys(passwd)
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

print("@author Giuseppe La Gualano - https://www.linkedin.com/in/giuseppe-la-gualano-56bb8210b")
print("@license This software is free - http://www.gnu.org/licenses/gpl.html")

# Password Handler
try:  # try to open file configRouter.txt
    with open("ConfigRouter.txt", "r") as f:
        data = f.readlines()

    #  format list of config vars
    configRouter = [line.rstrip('\n') for line in open('ConfigRouter.txt')]
    configRouter = [w.replace('password=', '') for w in configRouter]

    try:  # check if file is empty
        password = configRouter[0]
    except:
        pass

    f.close()

except IOError:  # if file configRouter.txt not exist, create new
    file = open("configRouter.txt", 'w', newline='\n')
    print("\nRouter connector config\n")

    #  user input for new password
    password = input("Password: ")
    file.write("password=" + password)

    file.close()

example("http://192.168.1.1/main.cgi?page=login.html", password)
