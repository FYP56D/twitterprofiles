from ast import Try
import save1
from save1 import enter_user
import sear
from sear import Usernames
import time
import Example
from Example import Userlist
import os

#Usernames1 =[]
enter_user()
Usernames1 = Usernames()
#print(Usernames1)
#Usernames1=["@ImranKhanPTI"]
Userlist(Usernames1)
print("SUCCESS")
try:
    os.remove("new.txt")
except Exception as e:
    print(" ")
