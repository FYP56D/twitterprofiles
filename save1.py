from socket import socket
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import pyperclip
import time
import pyautogui

options = Options()
options.headless = False
path = 'C:\\Users\\ALI-NAQI\\Downloads\\chromedriver_win32 (1)\chromedriver.exe'


time1 = 2
time2=5
def enter_user():
    userr1 = input("enter username: ")
#    browser=utils.init_driver(headless=True)
    browser = webdriver.Chrome(path,options = options)
    
    browser.get(f'https://twitter.com/search?q={userr1}&src=typed_query&f=user')
    #pyautogui.keyDown("ctrl")
    #pyautogui.press("r")
    #pyautogui.keyUp("ctrl")
        
    ##time.sleep(5)

    for i in range(1,10):
        
    #    time.sleep(time1)
    #    pyautogui.keyDown("ctrl")
    #    pyautogui.press("a")
    #    pyautogui.keyUp("ctrl")
    #    pyautogui.keyDown("ctrl")
    #    pyautogui.press("c")
    #    pyautogui.keyUp("ctrl")
        
    #    s = pyperclip.paste() 
    #            time.sleep(time1)
        try:
            time.sleep(time1)
            print("==================================================================================================================")
            follo = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div')))
            following = follo.text
            #print(following)
        except Exception as e:
            print(e)
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        with open('new.txt','a',encoding="utf-8") as g:
            g.write(following)

    
    time.sleep(time2)
    browser.close()
    browser.quit()
    g.close()
   


