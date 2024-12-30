import requests
from lxml import etree

url = 'https://www.zbj.com/fw/?k=saas'

cookies = "BAIDUID_BFESS=791316176AA030D37ABA9899DC3CEBE2:FG=1; HMACCOUNT_BFESS=69A0C2AE5908BFBB; BDUSS_BFESS=Z1QzgwSG4tOWtXNHd5WkRiOWRXdXJVMU92VmRISnZMd2JCcUl5bGVnRy05Z2RuRVFBQUFBJCQAAAAAAQAAAAEAAABIuNg9c2h1YWkwMDAzMTcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAL5p4Ga-aeBmZF; ZFY=Hh:Aif:ALjkNYVLDpKCu9N0J:BSzY9xoDp:BiH:BUOwP0Wv8:C"

headers = {
    'host' : "www.zbj.com",
    'Referer' : "https://www.zbj.com/",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
}

cookies_jar = requests.cookies.RequestsCookieJar()

for cookie in cookies.split(';'):
    key, value = cookie.split('=',1)
    cookies_jar.set(key, value)

# 添加cookie反反爬

response = requests.get(url,headers=headers,cookies=cookies_jar)

html = etree.HTML(response.text)

divs = html.xpath('//*[@id="__layout"]/div/div[3]/div[1]/div[4]/div/div[2]/div[1]/div[2]/div')
# //*[@id="__layout"]/div/div[3]/div[1]/div[4]/div/div[2]/div[1]/div[2]/div[1]/     div/div[3]/div[1]/span
# //*[@id="__layout"]/div/div[3]/div[1]/div[4]/div/div[2]/div[1]/div[2]/div[1]/     div/div[3]/div[2]/a/span
# //*[@id="__layout"]/div/div[3]/div[1]/div[4]/div/div[2]/div[1]/div[2]/div[1]/     div/div[5]/div/div/div

for div in divs:
    price = div.xpath('./div/div[3]/div[1]/span/text()')[0].strip("¥")
    title = "".join(div.xpath('./div/div[3]/div[2]/a/span//text()'))
    company = div.xpath('./div/div[5]/div/div/div/text()')[0]
    print(price,title,company)





