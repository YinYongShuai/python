import requests
import os
from lxml import etree

url = "https://www.acgmhh.com/artist/cat-demon.html"

domin = "https://www.acgmhh.com"

res = requests.get(url)

# //*[@id="list"]/li[1]/a

html = etree.HTML(res.text)

srcs = html.xpath('//*[@id="list"]/li/a')

filepath = 'C:/Users/Administrator/Desktop/picture/cat_demo'


for src in srcs:
    # print(src.get('href'))
    print(src.get("title"))
    title = src.get("title")
    newtitle = title.split(" – ")[-1]
    # 创建一个文件夹newfile = filepath + "/" + newtitle
    print(newtitle)
    newfile = filepath + "/" + newtitle
    os.makedirs(newfile, exist_ok=True)

    urls = domin + src.get('href')
    print(urls)
    child_res = requests.get(urls)
    # print(child_res.text)
    child_html = etree.HTML(child_res.text)
    img1 = child_html.xpath('/html/body/div[2]/div[1]/div[3]/div[2]/p/img')
    last = child_html.xpath('//*[@id="pages"]/a[last()-1]/text()')
    last_num = int(last[0])
    print(last_num+1)
    img1_src = img1[0].get('src')
    print(img1_src)
    img1_name = img1_src.split('/')[-1]
    img1_res = requests.get(img1_src)
    filepath1 = newfile + '/' + img1_name
    with open(filepath1, 'wb') as f:
        f.write(img1_res.content)
        print('over', img1_name)
        f.close()
    img1_res.close()

    i = 2
    while i <= last_num:
        oldurl = domin + src.get('href')
        newurl = oldurl[:-5] + '-' + str(i) + oldurl[-5:]
        print(newurl)
        i = int(i) + 1
        newurl_res = requests.get(newurl)
        newhtml = etree.HTML(newurl_res.text)
        img2 = newhtml.xpath('/html/body/div[2]/div[1]/div[3]/div/p/img')
        newsrc = img2[0].get('src')
        print(newsrc)
        img2_name = newsrc.split('/')[-1]
        newres = requests.get(newsrc)
        filepath2 = newfile + '/' + img2_name
        with open(filepath2, 'wb') as f:
            f.write(newres.content)
            print('over', img2_name)
            f.close()
        newres.close()

res.close()

# 存在问题同名图片会删除前一个图片，解决方式1 每一组图片存在一个文件夹中  解决方法2 所有图片按数字排序命名存在唯一的名字
