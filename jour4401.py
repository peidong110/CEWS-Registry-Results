from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
import time


def create_csv():
    path = "file.csv"
    with open(path, 'w') as file:
        csv_write = csv.writer(file)
        csv_head = ['Business Name', 'Operating Name']
        csv_write.writerow(csv_head)


def write_csv(business: list[str], operating: list[str]):
    path = "file.csv"
    with open(path, 'a+') as f:
        csv_write = csv.writer(f)
        for i in range(100):
            data_row = [business[i], operating[i]]
            csv_write.writerow(data_row)


def remove_chr(items):
    lis = []
    for item in items:
        lis.append(item.replace('\n', "").replace('\r', "").replace('\t', ""))
    return lis


def craw_single_page(pagenum):
    front = 'https://apps.cra-arc.gc.ca/ebci/hacc/cews/srch/pub/bscSrch?dsrdPg='
    back = '&q.srchNm=car&q.ordrClmn=NAME&q.ordrRnk=ASC'
    url = front + str(pagenum) + back
    html = urlopen(url).read().decode()
    soup = BeautifulSoup(html, features='lxml')
    newAddress = soup.find_all("div", class_="mrgn-tp-sm")
    businessName = []
    operatingName = []
    flag = True
    for i in newAddress:
        text = i.get_text()
        if flag:
            businessName.append(text)
            flag = not flag
        else:
            operatingName.append(text)
            flag = not flag
        # print(i.get_text())
    newOperatingName = remove_chr(operatingName)
    newBusinessName = remove_chr(businessName)
    write_csv(newBusinessName, newOperatingName)


def page_range():
    start, end = map(int, input("Please enter starting page and ending page").split())
    for i in range(start, end + 1):
        craw_single_page(i)


if __name__ == "__main__":
    start = time.time()
    url = 'https://apps.cra-arc.gc.ca/ebci/hacc/cews/srch/pub/bscSrch?dsrdPg=1&q.srchNm=car&q.ordrClmn=NAME&q.ordrRnk=ASC'
    create_csv()
    page_range()
    end = time.time()
    print("end time:" + str(end - start))
#end time:12.6405189037323
