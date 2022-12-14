from Scweet.scweet import scrape
from Scweet.user import get_user_information, get_users_following, get_users_followers
env_path = ".env"
import csv
import pandas

# scrape top tweets with the words 'covid','covid19' and without replies. the process is slower as the interval is
# smaller (choose an interval that can divide the period of time betwee, start and max date) scrape english top
# tweets geolocated less than 200 km from Alicante (Spain) Lat=38.3452, Long=-0.481006.
#data = scrape(words=['bitcoin', 'ethereum'], since="2021-10-01", until="2021-10-05", from_account=None, interval=1,
 #             headless=False, display_type="Top", save_images=False, lang="en",
#              resume=False, filter_replies=False, proximity=False, geocode="38.3452,-0.481006,200km")

# scrape top tweets of with the hashtag #covid19, in proximity and without replies. the process is slower as the
# interval is smaller (choose an interval that can divide the period of time betwee, start and max date)
#data = scrape(words=['Imran Khan', 'PTI'], since="2022-08-05", until="2022-08-08", from_account=None, interval=1,
 #             headless=False, display_type="Top", save_images=False,
  #            resume=False, filter_replies=True, proximity=True)

# Get the main information of a given list of users
# These users belongs to my following. 
# opening the file in read mode
#my_file = open("Imran_Khan.txt", "r")
  
# reading the file
#data = my_file.read()  
# replacing end splitting the text 
# when newline ('\n') is seen.
#f1 = open("Imran_Khan.txt", "r")
#lines= 10
#x = 0
#z=0
#y = len(f1.readlines())
#for s in range(0,y-1,10):
#  users=[]   
#  for x in range(lines):
#      x = x + 1
#a = f1.readlines()
#      print("a",a,x,s)
#      users += [a]
#      if x == 10:
#print(a)

  #users_info = get_user_information(res, headless=True)
#z = z + 1
def Userlist(Usernames1):

  Lines = Usernames1
  print(Lines)
  L1=[]
  i=0
  z = len(Lines)-1
  #print(z)
  while (z>i):
    for x in range(6):
  #     print(i)
        L1.append(Lines[i])
        if x == 5 :
          L2 = [x[:-1] for x in L1]
          print(L2)
          users_info = get_user_information(L2, headless=True)
          L1.clear()
          L2.clear()
        if z == i :
          break
        if z > i:   
          i = i + 1
        x = x + 1
        
  if L1 :
    L2 = [x[:-1] for x in L1]
    users_info = get_user_information(L2, headless=True)
    L1.clear()
    L2.clear()
  Lines1 = []
  for n in Lines:
      Lines1.append(str(n))

  #print(Lines1)
  def Skipped_Users(Skipped):
    z1=len(Skipped)
    L11=[]
    while (z1>i):
      for x in range(4):
  #     print(i)
        L11.append(Lines[i])
        if x == 3 :
          L22 = [x[:-1] for x in L1]
          users_info = get_user_information(L22, headless=True)
          L11.clear()
          L22.clear()
        if z1 == i :
          break
        if z1 > i:   
          i = i + 1
        x = x + 1
    return 0    
      


  b=0
  Skipped = []
  data = pandas.read_csv("Profiles/Profiles.csv", header=0, encoding="utf-8")
  csvfile = list(data.User_Name)
  print(csvfile,"CSV FILE")
  for b in range(z):
    L3 = [x[:-1] for x in Lines1]
    if L3[b] in csvfile:
      print("Yes : ",L3[b])
    if L3[b] not in csvfile:
      print("Not : ", L3[b])  
      Skipped.append(L3[b])
    b+=1
  print(Skipped)  
  ad =Skipped_Users(Skipped)


#print(z)        
#my_file.close()
#users = data_into_list
#['nagouzil', '@yassineaitjeddi', 'TahaAlamIdrissi',
 #        '@Nabila_Gl', 'geceeekusuu', '@pabu232', '@av_ahmet', '@x_born_to_die_x']

# this function return a list that contains : 
# ["nb of following","nb of followers", "join date", "birthdate", "location", "website", "description"]


# Get followers and following of a given list of users Enter your username and password in .env file. I recommande
# you dont use your main account. Increase wait argument to avoid banning your account and maximise the crawling
# process if the internet is slow. I used 1 and it's safe.

# set your .env file with SCWEET_EMAIL, SCWEET_USERNAME and SCWEET_PASSWORD variables and provide its path

#following = get_users_following(users=users, env=env_path, verbose=0, headless=True, wait=2, limit=50, file_path=None)

#followers = get_users_followers(users=users, env=env_path, verbose=0, headless=True, wait=1, limit=50, file_path=None)