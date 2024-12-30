import requests

url ="https://fanyi.baidu.com/sug"

s = input("请输入你要翻译的内容")

dat = {
    "kw" :  s
}

#发送post请求，参数放在data中进行传递

res = requests.post(url,data = dat)

print(res.json())

res.close()