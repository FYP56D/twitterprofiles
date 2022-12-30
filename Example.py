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

def Userlist(Usernames1):

  Lines = Usernames1
  # #print(Lines)
  # L1=[]
  # i=0
  # z = len(Lines)-1
  # #print(z)
  # while (z>i):
  #   for x in range(15):
  # #     print(i)
  #       L1.append(Lines[i])
  #       if x == 14:
  #         L2 = [x[:-1] for x in L1]
  #         print(L2)
  users_info = get_user_information(Lines, headless=False)
        #   L1.clear()
        #   L2.clear()
        # if z == i :
        #   break
        # if z > i:   
        #   i = i + 1
        # x = x + 1
  