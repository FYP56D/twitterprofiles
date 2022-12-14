
import save1
from save1 import enter_user
import re

def getbook():
    bookname = "new.txt"
    bookFile = open(bookname, 'r',encoding="utf-8")
    bookString = bookFile.read()
    lowerBook = bookString.lower()
    wordList = lowerBook.split()
    return wordList

import string

def listAllThe(longString):
    theList = []
    for i in longString:
        if i.startswith('@'):
            theList.append(i)
    return theList

def Usernames():
    book = getbook()
    getList = listAllThe(book)
    
    getList = list(set(getList))
    print (getList)
    return getList
Usernames()