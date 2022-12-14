import time

from Scweet1 import utils
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium
from time import sleep
import random
import json
import csv

def get_user_information(users, driver=None, headless=True):
    """ get user information if the "from_account" argument is specified """

    driver = utils.init_driver(headless=False)

    users_info = {}

    for i, user in enumerate(users):

        log_user_page(user, driver)

        if user is not None:

            try:
                time.sleep(5)
                #follo = WebDriverWait(driver, 120).until(
                    #EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/form/div[3]/div[3]/a[2]')))
                follo = driver.find_element(By.XPATH,'//a[contains(@href,"/following")]/span[1]/span[1]')
                #following = driver.find_element_by_xpath(
                    #'//a[contains(@href,"/following")]/span[1]/span[1]').text
                following = follo.text
                follo = driver.find_element(By.XPATH, '//a[contains(@href,"/followers")]/span[1]/span[1]')
                #followers = driver.find_element_by_xpath(
                    #'//a[contains(@href,"/followers")]/span[1]/span[1]').text
                followers = follo.text
            except Exception as e:
                # print(e)
                following=""
                followers=""
                #print(e)

            try:
                time.sleep(10)
                element = driver.find_elements(By.XPATH, '//div[contains(@data-testid,"UserProfileHeader_Items")]//a[1]')
                #element = driver.find_element_by_xpath('//div[contains(@data-testid,"UserProfileHeader_Items")]//a[1]')
                website = ""
            except Exception as e:
                #print(e)
                #print("2")
                website = ""

            try:
                descc = driver.find_element(By.XPATH,'//div[contains(@data-testid,"UserDescription")]')
                desc = descc.text
            except Exception as e:
                #print(e)
                #print("3")
                desc = ""
            a = 0
            try:

                join_date = driver.find_element(By.XPATH,
                    '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[4]/div/span/span').text
                birthday = driver.find_element(By.XPATH,
                    '//div[contains(@data-testid,"UserProfileHeader_Items")]/span[2]').text

                location = driver.find_element(By.XPATH,
                    '//div[contains(@data-testid,"UserProfileHeader_Items")]/span[1]').text

            except Exception as e:
                #print(e)
                #print("4")
                try:
                    join_date = driver.find_element(By.XPATH,
                        '//div[contains(@data-testid,"UserProfileHeader_Items")]/span[2]').text
                    span1 = driver.find_element(By.XPATH,
                        '//div[contains(@data-testid,"UserProfileHeader_Items")]/span[1]').text
                    if hasNumbers(span1):
                        birthday = span1
                        location = ""
                    else:
                        location = span1
                        birthday = ""
                except Exception as e:
                    #print(e)
                    #print("5")
                    try:
                        join_date = driver.find_element(By.XPATH,
                            '//div[contains(@data-testid,"UserProfileHeader_Items")]/span[1]').text
                        birthday = ""
                        location = ""
                    except Exception as e:
                        print(e)
                        print("6")
                        join_date = ""
                        birthday = ""
                        location = ""
            print("--------------- " + user + " information : ---------------")
            print("Following   : ", following)
            print("Followers   : ", followers)
            print("Location    : ", location)
            print("Join date   : ", join_date)
            print("Birth date  : ", birthday)
            print("Description : ", desc)
            print("Website     : ", website)
            users_info[user] = [following, followers, join_date, birthday, location, website, desc]
            Profiles_header = ['name', 'following', 'followers', 'location','join_date','birthday','bio','website']
            Profiles_data = [ user , following , followers , location, join_date, birthday, desc, website, ]
            with open('Profiles1.csv', 'a', encoding='utf') as file:
                writer = csv.writer(file)
                writer.writerow(Profiles_header)
                writer.writerow(Profiles_data)
            try:
                driver.get(f"https://twitter.com/{user}/photo")
                time.sleep(5)
                driver.save_screenshot(f"D:\FYP\Scweet-master\yo\{user}")

            
            except Exception as e:
                print(e)
            if i == len(users) - 1:
                driver.close()
                return users_info
        else:
            print("You must specify the user")
            continue
        sleep(10)


def log_user_page(user, driver, headless=True):
    sleep(random.uniform(1, 2))
    driver.get('https://twitter.com/' + user)
    sleep(random.uniform(1, 2))


def get_users_followers(users, env, verbose=1, headless=True, wait=2, limit=float('inf'), file_path=None):
    followers = utils.get_users_follow(users, headless, env, "followers", verbose, wait=wait, limit=limit)

    if file_path == None:
        file_path = 'outputs/' + str(users[0]) + '_' + str(users[-1]) + '_' + 'followers.json'
    else:
        file_path = file_path + str(users[0]) + '_' + str(users[-1]) + '_' + 'followers.json'
    with open(file_path, 'w') as f:
        json.dump(followers, f)
        print(f"file saved in {file_path}")
    return followers


def get_users_following(users, env, verbose=1, headless=True, wait=2, limit=float('inf'), file_path=None):
    following = utils.get_users_follow(users, headless, env, "following", verbose, wait=wait, limit=limit)

    if file_path == None:
        file_path = 'outputs/' + str(users[0]) + '_' + str(users[-1]) + '_' + 'following.json'
    else:
        file_path = file_path + str(users[0]) + '_' + str(users[-1]) + '_' + 'following.json'
    with open(file_path, 'w') as f:
        json.dump(following, f)
        print(f"file saved in {file_path}")
    return following


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)
