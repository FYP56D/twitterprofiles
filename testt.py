from bs4 import BeautifulSoup


f_1 = open('C:\\Users\\ALI-NAQI\\Downloads\\imran khan #1.html', 'r+',encoding="utf8")
f_2 = open('C:\\Users\\ALI-NAQI\\Downloads\\imran khan #2.html', 'r+',encoding="utf8")
f_3 = open('C:\\Users\\ALI-NAQI\\Downloads\\imran khan #3.html', 'r+',encoding="utf8")
f_4 = open('C:\\Users\\ALI-NAQI\\Downloads\\imran khan #4.html', 'r+',encoding="utf8")
f_5 = open('C:\\Users\\ALI-NAQI\\Downloads\\imran khan #5.html', 'r+',encoding="utf8")



with open('C:\\Users\\ALI-NAQI\\Downloads\\imran khan #1.html') as f1:
    soup = BeautifulSoup(f_1, "lxml")
    links = []
    for link in soup.findAll('a'):
        print(link.get('href'))
        print("\n")
        links.append(link.get('href'))
    for i in range(len(links)):
        print(links[i])
    
    print('------')
    usernames=[]
    spans = soup.find_all('span',"css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0")
    user_name= []
    
    for span in spans:
     
        txt = span.text
        if txt.startswith('@'):
        
            print(txt)
            user_name.append(txt)

print(user_name)
print(len(user_name))