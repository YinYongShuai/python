from bs4 import BeautifulSoup
import requests

url = 'https://www.zhizuobiao.com'

response = requests.get(url)

# print(response.text)

page = BeautifulSoup(response.text, 'html.parser')
#
left = page.find('dd', class_='left')


#
# print(left)

blanks = left.findAll('a', target='_blank')

for blank in blanks:
    print(blank.text)
# print(smooth)


