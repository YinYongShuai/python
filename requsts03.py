import requests

url = "https://movie.douban.com/j/chart/top_list"

header = {
"user-agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
}

param = {
"type": 24,
"interval_id": "100:90",
"action": "",
"start": 0,
"limit": 20,
}

res = requests.get(url = url,params = param,headers = header)

print(res.json())

res.close()





