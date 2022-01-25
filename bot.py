from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from keyboard import press
import time
from pynput.keyboard import Key, Controller
import sched, time
from datetime import datetime
import os
from apscheduler.schedulers.blocking import BlockingScheduler

while(True):
    print('Checking for Class Again')
    usernameStr = 'S.1107'
    passwordStr = 'Captain Roger'
    
    keyboard = Controller()
#browser stuffs
    browser = webdriver.Chrome()
    browser.maximize_window()

    browser.get(('https://mis.ankuram.edu.np/Student/Accounts/Login'))



#Username And Password input in site
    browser.find_element_by_name('username').send_keys('S.1107')

    browser.find_element_by_name('password').send_keys('Captain Roger')

    time.sleep(2)

    browser.find_element_by_css_selector('button.btn.btn-secondary.btn-block').click()

    time.sleep(2)

    browser.get(('https://mis.ankuram.edu.np/Student/Student/Creation/LiveClass'))
    time.sleep(10)
    
    classValue =  browser.find_element_by_xpath("//*[@id='add-subject-section']/div[1]/div[2]/div/div[4]/span/span").text

    print(classValue)
    if classValue!="-":

    
#joining class


        browser.find_element_by_css_selector('button.btn.btn-sm.btn-info.mb-2').click()
        time.sleep(3)
        browser.switch_to.alert.accept()
        time.sleep(4)
        keyboard.press(Key.up)
        keyboard.release(Key.up)
        press('enter')
        time.sleep(4)
        browser.quit()
        print('Joining Class. Program will pause for 40 minutes')
        time.sleep(2400)
        

#exiting browser

    else:
        browser.quit()



    time.sleep(45)








