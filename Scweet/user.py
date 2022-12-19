import time
import os
import requests
import json
from Scweet import utils
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import selenium
from time import sleep
import random
import json
import csv 
from csv import DictWriter
import snscrape
import snscrape.modules.twitter as sntwitter
import pandas as pd
path = 'C:\\Users\\ALI-NAQI\\Downloads\\chromedriver_win32 (1)\chromedriver.exe'
#browser = webdriver.Chrome(path)
def get_user_information(users ,driver=None, headless=True):
    """ get user information if the "from_account" argument is specified """

    driver = utils.init_driver(headless=True)
    #users = ["@ImranKhanPTI","@elonmusk"]
    users_info = {}

    for i, user in enumerate(users):
        flag = 0

        log_user_page(user, driver)

        if user is not None:
            driver.get(f'https://twitter.com/{user}')
            
            try: 
                followww  = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[contains(@href,"/following")]/span[1]/span[1]')))
            except Exception as e:
                print(f"{user}'s Account is protected or doesnot exist")
                flag =1
                continue
            try:
               # time.sleep(3)
                follo = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//a[contains(@href,"/following")]/span[1]/span[1]')))
                #follo = driver.find_element(By.XPATH,'//a[contains(@href,"/following")]/span[1]/span[1]')
                #following = driver.find_element_by_xpath(
                    #'//a[contains(@href,"/following")]/span[1]/span[1]').text
                following = follo.text
                #follo = driver.find_element(By.XPATH, '//a[contains(@href,"/followers")]/span[1]/span[1]')
                followers = WebDriverWait(driver, 2).until(
                    EC.presence_of_element_located((By.XPATH,'//a[contains(@href,"/followers")]/span[1]/span[1]'))).text
                #followers = driver.find_element_by_xpath(
                    #'//a[contains(@href,"/followers")]/span[1]/span[1]').text
                #followers = follo.text
            except Exception as e:
                print("------------")
                if flag == 0:
                    driver.get(f'https://twitter.com/{user}')
                    print("e")
                #following=""
                #followers=""
                #print(e)

            try:
                element = driver.find_element_by_xpath('//div[contains(@data-testid,"UserProfileHeader_Items")]//a[1]')
                website = element.get_attribute("href")
            except Exception as e:
                # print(e)
                website = ""

            try:
                desc = driver.find_element_by_xpath('//div[contains(@data-testid,"UserDescription")]').text
            except Exception as e:
                # print(e)
                desc = ""
            a = 0

            try:
                join_date = driver.find_element_by_xpath(
                    '//div[contains(@data-testid,"UserProfileHeader_Items")]/span[3]').text
                birthday = driver.find_element_by_xpath(
                    '//div[contains(@data-testid,"UserProfileHeader_Items")]/span[2]').text
                location = driver.find_element_by_xpath(
                    '//div[contains(@data-testid,"UserProfileHeader_Items")]/span[1]').text
            except Exception as e:
                # print(e)
                try:
                    join_date = driver.find_element_by_xpath(
                        '//div[contains(@data-testid,"UserProfileHeader_Items")]/span[2]').text
                    span1 = driver.find_element_by_xpath(
                        '//div[contains(@data-testid,"UserProfileHeader_Items")]/span[1]').text
                    if hasNumbers(span1):
                        birthday = span1
                        location = ""
                    else:
                        location = span1
                        birthday = ""
                except Exception as e:
                    # print(e)
                    try:
                        join_date = driver.find_element_by_xpath(
                            '//div[contains(@data-testid,"UserProfileHeader_Items")]/span[1]').text
                        birthday = ""
                        location = ""
                    except Exception as e:
                        # print(e)
                        join_date = ""
                        birthday = ""
                        location = ""
            try:
                s = WebDriverWait(driver,2).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/h2/div/div/div/div/span[2]')))
                s1 = s.is_displayed()
                if s1 is False:
                    verification = f"{user} not verified"
                else:
                    verification = f"{user} verified"

                #print(verification)
            

                tweetno = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/div").text
                #tweetno = [int(s) for s in str.split(tweetno) if s.isdigit()]
                #browser.get(f"https://twitter.com/{user}/likes")
                #time.sleep(2)
                #likes = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/div").text
                
                #print(tweetno)
                #print(likes)
            except Exception as e:
                print("Not found")
#            try: 
#                verified  = WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@data-testid,"icon-verified")]' )))

#                print("verified")
 #           except Exception as e:
 #               print("Not verified")    
            try:
                Full_name = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/h2/div/div/div/div/span[1]/span/span').text 
            except Exception as e:
                print ('cannot get name')
            try:
                print("--------------- " + user + " information : ---------------")
                print("Full Name : ", Full_name)
                print("Following : ", following)
                print("Followers : ", followers)
                print("Location : ", location)
                print("Join date : ", join_date)
                print("Birth date : ", birthday)
                print("Description : ", desc)
                print("Description : ", tweetno)
                print("Website : ", website)
                print("Verification status: ", verification)
                users_info[user] = [Full_name,user,following, followers, join_date, birthday, location, website, desc, tweetno, verification]
                Profiles_header = ['Full-name','User-name', 'following', 'followers', 'location','join_date','birthday','bio','website','Tweet no ', 'verification']
                Profiles_data = [ Full_name ,user , following , followers , location, join_date, birthday, desc, website, tweetno, verification ]
                dict1 =  {'Full_name':Full_name, 'User-name':user, 'Following':following, 'Followers':followers, 'Location':location,'join-date':join_date,'birthday':birthday,'description':desc,'website':website,'tweetno':tweetno,'verification':verification}
                #df = pd.DataFrame(dict1, index=[0]) 
                #df.to_csv('Profiles1.csv' )                
                with open('Profiles/Profiles.json', 'a') as file:
                    #dictwriter_object = DictWriter(file, fieldnames=Profiles_header , delimiter=',')
                    #dictwriter_object.writerow(dict1)
                    #file.close()
                    json.dump(dict1,file )
    
#                with open('Profiles/Profiles1.csv', 'w+', newline ='',encoding='utf-8') as file:
 #                   is_header = not any(cell.isdigit() for cell in file[0])
  #                  writer = csv.writer(file)
   #                 if is_header == False:
    #                    writer.writerow(Profiles_header)
     #               writer.writerow(Profiles_data)
                print("----------Data printed to CSV file")
            except Exception as e:
                print("Exception of writing To CSV File", e)

            try: 
                # Creating list to append tweet data to
                tweets_list1 = []

                # Using TwitterSearchScraper to scrape data and append tweets to list
                for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'from:{user}').get_items()):
                    if i>150:
                        break
                    tweets_list1.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
                    
                # Creating a dataframe from the tweets list above 
                tweets_df1 = pd.DataFrame(tweets_list1, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
                tweets_df1.to_csv(f'Tweets/{user}.csv', sep=',', index=False)
                print("fetched tweets-------------------------")
                                #os.system(f"snscrape --format '{content!r}' --max-results 100 twitter-search 'from:{user}'> {user}-tweets.json")
            except Exception as e:
                print("-----cannot fetch tweets---")

            try:
                #driver1 = uc.Chrome(use_subprocess = True )
                #driver1.get(f"https://twitter.com/{user}/photo")
                #time.sleep(3)
                #driver1.save_screenshot(f"D:\FYP\Scweet-master\yo\{user}.png")
                #time.sleep(1)
                #driver1.quit()
                #driver1.close()
                URL = f"https://unavatar.io/twitter/{user}"
                response = requests.get(URL)
                # 3. Open the response into a new file 
                open(f"images/{user}-profilepic.png", "wb").write(response.content)
                URL2 = f"https://twitter.com/{user}/header_photo"
                response = requests.get(URL2)
                # 3. Open the response into a new file 
                open(f"images/{user}-coverpic.png", "wb").write(response.content)
                print("fetched Images----------------")
            
            except Exception as e:
                    print("Cannot fetch images")
            if i == len(users) - 1:
                driver.close()
                driver.quit()
                return users_info
                print("-----picture not found--------------")
        else:
            print("You must specify the user")
            continue
        sleep(2)


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

def search(user):
    driver.get(f"https://twitter.com/search?q={user}&src=typed_query&f=user")
    list_of_users_get = []
    for i in range(1,28):
        q = WebDriverWait(driver, 120).until(
                    EC.presence_of_element_located((By.XPATH, f'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div/div[{i}]/div/div/div/div/div[2]/div[1]/div[1]/div/div[2]/div/a/div/div/span')))
        print(q.text)
  
