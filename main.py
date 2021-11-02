from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
import time
import requests




def create_csv():
    path = "file.csv"
    with open(path, 'w', newline='') as file:
        csv_write = csv.writer(file)
        csv_head = ['Business Name', 'Operating Name']
        csv_write.writerow(csv_head)


def write_csv(business: list, operating: list):
    path = "file.csv"
    with open(path, 'a+', newline='') as f:
        csv_write = csv.writer(f)
        for i in range(len(business)):
            data_row = [business[i], operating[i]]
            csv_write.writerow(data_row)


def remove_chr(items):
    lis = []
    for item in items:
        lis.append(item.replace('\n', "").replace('\r', "").replace('\t', ""))
    return lis

def getMax():
    #This function is unnecessary if you know the max page though
    max = 400
    url = 'https://apps.cra-arc.gc.ca/ebci/hacc/cews/srch/pub/fllLstSrh?dsrdPg=400&q.ordrClmn=NAME&q.ordrRnk=ASC'
    r= requests.get(url)
    txt=r.text

    # f = open('file.html', 'x', encoding='utf-8')
    while(txt.find("We found no match for the search criteria you used.") < 0 ):
      max+=1
      url = 'https://apps.cra-arc.gc.ca/ebci/hacc/cews/srch/pub/fllLstSrh?dsrdPg='+str(max)+'&q.ordrClmn=NAME&q.ordrRnk=ASC'

      r= requests.get(url)
      txt=r.text
      if(txt.find("We found no match for the search criteria you used.") > 0):
        max = max-1
        break;
    return max



def craw_single_page(pagenum):
    # front = 'https://apps.cra-arc.gc.ca/ebci/hacc/cews/srch/pub/bscSrch?dsrdPg='
    # back = '&q.srchNm=car&q.ordrClmn=NAME&q.ordrRnk=ASC'
    front = 'https://apps.cra-arc.gc.ca/ebci/hacc/cews/srch/pub/fllLstSrh?dsrdPg='
    back = '&q.ordrClmn=NAME&q.ordrRnk=ASC'
    url = front + str(pagenum) + back
    html = urlopen(url).read().decode()
    soup = BeautifulSoup(html, features='lxml')
    new_address = soup.find_all("div", class_="mrgn-tp-sm")
    business_name = []
    operating_name = []
    flag = True
    for i in new_address:
        text = i.get_text()
        if flag:
            business_name.append(text)
            flag = not flag
        else:
            operating_name.append(text)
            flag = not flag
        # print(i.get_text())
    new_operating_name = remove_chr(operating_name)
    new_business_name = remove_chr(business_name)
    write_csv(new_operating_name, new_business_name)




if __name__ == "__main__":
    start = time.time()
    url = 'https://apps.cra-arc.gc.ca/ebci/hacc/cews/srch/pub/bscSrch?dsrdPg=1&q.srchNm=car&q.ordrClmn=NAME&q.ordrRnk=ASC'
    create_csv()
    # page_range()
    max = getMax()
    print("Max Page:"+str(max))
    for i in range(max):
        print(i)
        craw_single_page(i+1)

    end = time.time()
    print("end time:" + str(end - start))
    #end time:12.6405189037323
    # 1- 100 end time:55.16016626358032
