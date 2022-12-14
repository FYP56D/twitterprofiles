from socket import socket
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import pygetwindow
import time
import pyautogui

# start web browser
path = 'C:\\Users\\ALI-NAQI\\Downloads\\chromedriver_win32 (1)\chromedriver.exe'



def enter_user():
    userr1 = input("enter username: ")
    browser = webdriver.Chrome(path)
    browser.get(f'https://twitter.com/search?q={userr1}&src=typed_query&f=user')
    window  =browser.window_handles[0]
    print('search ')
    print(pyautogui.getWindows())
    time.sleep(20)
    print('reloading')

    pyautogui.keyDown("ctrl")
    pyautogui.press("r")
    pyautogui.keyUp("ctrl")
    print('reloaded')
    time.sleep(5)# get source code


    print(window)

enter_user()