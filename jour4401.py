import webbrowser
import requests
import sqlite3
import sys
import os
import json
import csv

from bs4 import BeautifulSoup
from urllib.request import urlopen

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



def write_to_csv(data):
    with open('names.csv', 'w', newline='') as csvfile:
        fieldnames = ['Bussiness Name', 'Operating Name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        # for i in data:
        # writer.writerow({'Bussiness Name': bussinessName, 'Operating Name': operatingName})

def remove_chr(type,list):

    for i in list:
        if type == 1:
                i = i.replace('\r',"").replace('\n',"").replace('\t',"")
        elif type == 2:
            if i == "\n":
                i = i.replace('\n'," ")
            else:
                i = i.replace('\r',"").replace('\n',"").replace('\t',"")


if __name__ == "__main__":
    url = 'https://apps.cra-arc.gc.ca/ebci/hacc/cews/srch/pub/bscSrch?dsrdPg=1&q.srchNm=car&q.ordrClmn=NAME&q.ordrRnk=ASC'
    html = urlopen(url).read().decode()
    soup = BeautifulSoup(html, features='lxml')
    abbr = soup.find_all("div", {"class": "mrgn-tp-sm"})
    
    newAddr = soup.find_all("div",class_="mrgn-tp-sm")
    bussinessName = []
    operatingName = []

    vv = 0
    flag = True

    for i in newAddr:
        # bussinessName.append(i.get_text().replace("\t","").replace("\r","").replace("\n",""))
        # print(i.get_text().replace("\t","").replace("\r","").replace)
        vv += 1
        text = i.get_text()
        if flag:
            bussinessName.append(text)
            flag = not flag
        else:
            operatingName.append(text)
            flag = not flag
        # print(i.get_text())

    remove_chr(1,bussinessName)
    remove_chr(2,operatingName)
    print(bussinessName)

    print("------------------------------")
    print(operatingName)

    # print(len(operatingName))
    # write_to_csv(newAddr)
    
    # c = str(abbr)
    # print(type(c))
    # print(c)
    # tickerList = []
    # a = 'href="comp" href="nsms"'
    # index= a.find('href')
    # print(a.find('href'))
    # findCourseTicker(c)
    # print(tickerList)
    # removeSlash(tickerList)
    # print(tickerList)
    
    # conn = sqlite3.connect('test.db')
    # cursor = conn.cursor()
    # for item in tickerList:
    #     cursor.execute("Insert into course(name) Values(?)",[item])
    # conn.commit()
    # conn.close()