import requests
session = requests.Session()
url = 'https://www.3bqg.cc/user/action.html'

dat = {
    'action':'bookcase',
    't':'1731502386120',
    'username': '18153480024',
    'password': 'Yys173730!'
}

response = session.get(url,data=dat)

print(response.text)