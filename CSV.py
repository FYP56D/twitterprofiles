import csv
b=0

with open('Profiles.csv', newline='',encoding="utf-8" ) as csvfile:
 data = csv.DictReader(csvfile)
 print("User Name")
 print("---------------------------------")
 for b in range(z):

  for row in data:
    if Lines[b] in csvfile:
      print(row['User_Name'])
  b+=1