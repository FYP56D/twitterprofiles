f_1 = open('C:\\Users\\ALI-NAQI\\Downloads\\imran khan #1.html', 'r+',encoding="utf8")
f_2 = open('C:\\Users\\ALI-NAQI\\Downloads\\imran khan #2.html', 'r+',encoding="utf8")
f_3 = open('C:\\Users\\ALI-NAQI\\Downloads\\imran khan #3.html', 'r+',encoding="utf8")
for l_no, line in enumerate(f_1):
    # search string
    if 'Follow @' in line:
        print('string found in a file')
        print('Line Number:', l_no)
        print('Line:', line)
        # don't look for next lines
        break

twitter = ''
for i in range(len(line)):
    if line[i] == 'F':
        if line[i+1] == 'o' and line[i+2] == 'l' and line[i+3] == 'l' and line[i+4] == 'o' and line[i+5] == 'w' and line[i+6] == ' ' and line[i+7] == '@':
            for r in range(15):
                e=i
                e=e+7
                if line[e] !=' ':
                    twitter+=line[e+r]
            twitter+=" "

print(twitter)

final = []
final = twitter.split("@")
print(final)
print(len(final))
#---------------------------------------------------------------------------
for l_no, line in enumerate(f_2):
    # search string
    if 'Follow @' in line:
        print('string found in a file')
        print('Line Number:', l_no)
        print('Line:', line)
        # don't look for next lines
        break

twitter = ''
for i in range(len(line)):
    if line[i] == 'F':
        if line[i+1] == 'o' and line[i+2] == 'l' and line[i+3] == 'l' and line[i+4] == 'o' and line[i+5] == 'w' and line[i+6] == ' ' and line[i+7] == '@':
            for r in range(15):
                e=i
                e=e+7
                if line[e] !=' ':
                    twitter+=line[e+r]
            twitter+=" "

print(twitter)

final = []
final = twitter.split("@")
print(final)
print(len(final))

#--------------------------------------------------------------

for l_no, line in enumerate(f_3):
    # search string
    if 'Follow @' in line:
        print('string found in a file')
        print('Line Number:', l_no)
        print('Line:', line)
        # don't look for next lines
        break

twitter = ''
for i in range(len(line)):
    if line[i] == 'F':
        if line[i+1] == 'o' and line[i+2] == 'l' and line[i+3] == 'l' and line[i+4] == 'o' and line[i+5] == 'w' and line[i+6] == ' ' and line[i+7] == '@':
            for r in range(15):
                e=i
                e=e+7
                if line[e] !=' ':
                    twitter+=line[e+r]
            twitter+=" "

print(twitter)

final = []
final = twitter.split("@")
print(final)
print(len(final))