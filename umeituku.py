import requests
from bs4 import BeautifulSoup
import time
url = 'https://www.umeituku.com/bizhitupian/weimeibizhi/'

res = requests.get(url)
res.encoding = 'utf-8'

main_page = BeautifulSoup(res.text, 'html.parser')

alist = main_page.find('div', class_='TypeList').findAll("a")

for a in alist:
    # print(a.get("href"))
    # 拿到子页面源代码
    child_page_res = requests.get(a.get("href"))
    child_page_res.encoding='utf-8'
    child_page_text = child_page_res.text
    child_page = BeautifulSoup(child_page_res.text, 'html.parser')
    p = child_page.find('p', align='center')
    try:
       img = p.find('img')
       src = img.get('src')
       print(src)
    except:
        print(src)
    img_res = requests.get(src)
    img_name = src.split('/')[-1]
    with open(img_name, 'wb') as f:
        f.write(img_res.content)
    print("over",img_name)
    time.sleep(1)

print("all over")