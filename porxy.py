import requests

# 111.1.61.49:3128

proxies = {
    'http': 'http://111.1.61.49:3128'
}

response = requests.get('http://www.baidu.com',proxies=proxies)
response.encoding= 'utf-8'
print(response.text)