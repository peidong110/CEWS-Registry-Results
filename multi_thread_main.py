import queue
import threading

from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
import time
import requests


def create_csv():
    path = "file1.csv"
    with open(path, 'w', newline='') as file:
        csv_write = csv.writer(file)
        csv_head = ['Business Name', 'Operating Name']
        csv_write.writerow(csv_head)


def write_csv(business: list, operating: list):
    path = "file1.csv"
    with open(path, 'a+', newline='') as f:
        csv_write = csv.writer(f)
        for i in range(len(business)):
            data_row = [business[i], operating[i]]
            csv_write.writerow(data_row)


def remove_chr(items):
    lis = []
    for x in items:
        lis.append(x.replace('\n', "").replace('\r', "").replace('\t', ""))
    return lis


def get_max():
    # This function is unnecessary if you know the max page though
    max_pg = 400
    url = 'https://apps.cra-arc.gc.ca/ebci/hacc/cews/srch/pub/fllLstSrh?dsrdPg=400&q.ordrClmn=NAME&q.ordrRnk=ASC'
    r = requests.get(url)
    txt = r.text

    # f = open('file.html', 'x', encoding='utf-8')
    while txt.find("We found no match for the search criteria you used.") < 0:
        max_pg += 1
        url = 'https://apps.cra-arc.gc.ca/ebci/hacc/cews/srch/pub/fllLstSrh?dsrdPg=' + str(
            max) + '&q.ordrClmn=NAME&q.ordrRnk=ASC'

        r = requests.get(url)
        txt = r.text
        if txt.find("We found no match for the search criteria you used.") > 0:
            max_pg = max - 1
            break
    return max


def crawl(url_queue: queue.Queue, parsed_html_queue: queue.Queue):
    while not url_queue.empty():
        single_page = url_queue.get()  # get the first link
        html = urlopen(single_page).read().decode()
        soup = BeautifulSoup(html, features='lxml')
        new_address = soup.find_all("div", class_="mrgn-tp-sm")
        parsed_html_queue.put(new_address)
        print("Fetching: " + str(parsed_html_queue.qsize()))
    print("END")


def parsed(parsed_html: queue.Queue):
    while not parsed_html.empty():
        print("Current PARSED HTML SIZE:" + str(parsed_html.qsize()))
        html = parsed_html.get()
        business_name = []
        operating_name = []
        flag = True
        for x in html:
            text = x.get_text()
            if flag:
                business_name.append(text)
                flag = not flag
            else:
                operating_name.append(text)
                flag = not flag
        new_operating_name = remove_chr(operating_name)
        new_business_name = remove_chr(business_name)
        write_csv(new_operating_name, new_business_name)


if __name__ == "__main__":
    start = time.time()
    create_csv()
    # # page_range()
    max_page = 410
    start = time.time()

    urls = [
        f"https://apps.cra-arc.gc.ca/ebci/hacc/cews/srch/pub/fllLstSrh?dsrdPg={page}&q.ordrClmn=NAME&q.ordrRnk=ASC"
        for page in range(1, max_page + 1)
    ]

    url_q = queue.Queue(maxsize=max_page)  # 410
    html_q = queue.Queue(maxsize=max_page)

    for item in range(max_page):
        url_q.put(urls[item])

    thread_list = []
    for thread in range(5):
        print(f"crawl in Thread {thread}")
        t = threading.Thread(target=crawl, args=(url_q, html_q,), name=f"crawl in Thread {thread}")
        t.start()
        thread_list.append(t)
    thread_list1 = []

    for item in thread_list:
        item.join()
    parsed(html_q)
    end_time = time.time()

    print("END TIME:" + str(end_time - start))
