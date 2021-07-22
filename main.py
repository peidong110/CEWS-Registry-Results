import webbrowser
import requests
import sqlite3
import sys
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen
from twilio.rest import Client

def courseAvailable(listOfItems):
    flag = False
    for i in listOfItems:
        if i['color'] == 'red':
            flag = True
    return flag
def removeSlash(items):
    for i in range(len(items)):
        if items[i][3].isalpha() == False:
            items[i] = items[i][:3]
def findCourseTicker(rawHTML):
    # Input:raw HTML, Type:String
    if rawHTML.find('href') == -1:
        #If there is no herf tag, means there are no more courses left.
        print("End of the Recursion.")
    else:

        #rawHTML find will return the current the first index.
        index = rawHTML.find('href')#return the 1st index
        tickerList.append(rawHTML[index+6:index+10])
        findCourseTicker(rawHTML[index+10:])

if __name__ == "__main__":
    url = 'https://calendar.carleton.ca/undergrad/courses/'
    html = urlopen(url).read().decode()
    soup = BeautifulSoup(html, features='lxml')
    abbr = soup.find_all("div", {"class": "course"})
    c = str(abbr)
    print(type(c))
    print(c)
    tickerList = []
    a = 'href="comp" href="nsms"'
    # index= a.find('href')
    # print(a.find('href'))
    findCourseTicker(c)
    # print(tickerList)
    removeSlash(tickerList)
    # print(tickerList)
    
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    for item in tickerList:
        cursor.execute("Insert into course(name) Values(?)",[item])
    conn.commit()
    conn.close()