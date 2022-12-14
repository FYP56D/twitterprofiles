import pyperclip as pc

s = pc.paste() 
with open('new.txt','w',encoding="utf-8") as g:
    g.write(s)
    