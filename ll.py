
import save

import re




def soupydoopy(user):
  with open('new.txt') as f:
    lines = f.readlines()
  #soup = BeautifulSoup(f, "txt") 
  #usernames=[]
  user_name= []
    

    
  txt =lines
  re.findall(r'\b@\w+', txt) 
  
  #if txt.startswith('@'):
        
  print(txt)
  user_name.append(txt)
  

  user_name_name = set(user_name) 
  print(user_name_name)
  print(len(user_name_name))


  text_file = open("D:\\FYP\\Scweet-master\\duplicate1.txt", "w")

  for i in range(len(user_name)):
    text_file.write(user_name[i])
    text_file.write('\n')
  
  text_file.close()
  













