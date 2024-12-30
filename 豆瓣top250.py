import requests
import re
import csv
url = "https://movie.douban.com/top250"

headers = {
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
}

resp = requests.get(url, headers=headers)

page_content = resp.text

obj = re.compile(r'<li>.*?<span class="title">(?P<name>.*?)'
                 r'</span>.*?<p class="">.*?(?P<year>\d+).*?</p>'
                 r'.*?<span class="rating_num" property="v:average">(?P<secore>.*?)</span>',re.S)

result = obj.finditer(page_content)

f = open("data.csv", "w")
csv_writer = csv.writer(f)

for i in result:
#      print(i.group("name"))
    # print(i.group("year"))
    # print(i.group("secore"))
    dic = i.groupdict()
    dic['year'] = dic['year'].strip()
    csv_writer.writerow(dic.values())
f.close()
print('over')


