import requests
import re
import csv
from bs4 import BeautifulSoup

url = 'http://www.xinfadi.com.cn/getPriceData.html'

res = requests.post(url)

f = open('caijia.csv', 'w')
csv_writer = csv.writer(f)

obj = re.compile(r'prodName":"(?P<name>.*?)",.*?"lowPrice":"(?P<low>.*?)","highPrice":"(?P<high>.*?)","avgPrice":"(?P<avg>.*?)"', re.S)

result = obj.finditer(res.text)

for i in result:
    t = (i.group("name"), i.group("low"), i.group("high"), i.group("avg"))
    csv_writer.writerow(t)

f.close()
res.close()
print("over")

#csv   创建一个文件流，并选择对应的mode  对这个流创建一个csv_writer对象  利用这个对象写入csv文件
