import requests
import csv
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
url = "http://www.xinfadi.com.cn/getPriceData.html"
f = open("xinfadi.csv", "w")
csv_writer = csv.writer(f)
def page_func(current_page):
    resp = requests.post(url, data={
        "limit": 20,
        'current': current_page
    })
    dic = resp.json()
    lists = dic["list"]
    for list in lists:
        txt = (list["prodName"],list["lowPrice"],list["highPrice"],list["avgPrice"])
        # print(txt)
        csv_writer.writerow(txt)
    print("完成了第",current_page,"页")

def print_i(i):
    print(i)
if __name__ == '__main__':
    with ThreadPoolExecutor(10) as t:
        for i in range(1,100):
            # t = Thread(target=page_func, args=(i,))
            # t.start()
            # print(i)
            t.submit(page_func, current_page=i)
            # t.submit(print_i, i)

