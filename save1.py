from socket import socket
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import pyperclip
    
import time
import pyautogui


path = 'C:\\Users\\ALI-NAQI\\Downloads\\chromedriver_win32 (1)\chromedriver.exe'


time1 = 2
def enter_user():
    userr1 = input("enter username: ")
    browser = webdriver.Chrome(path)
    browser.get(f'https://twitter.com/search?q={userr1}&src=typed_query&f=user')
    pyautogui.keyDown("ctrl")
    pyautogui.press("r")
    pyautogui.keyUp("ctrl")
        
    #time.sleep(5)

    for i in range(1,3):
        
        time.sleep(time1)
        pyautogui.keyDown("ctrl")
        pyautogui.press("a")
        pyautogui.keyUp("ctrl")
        pyautogui.keyDown("ctrl")
        pyautogui.press("c")
        pyautogui.keyUp("ctrl")
        
        s = pyperclip.paste() 
        with open('new.txt','a',encoding="utf-8") as g:
            g.write(s)
        time.sleep(time1)
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #
        
    browser.close()
    browser.quit()
    
