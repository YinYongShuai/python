
import requests
from base64 import b64encode
from Crypto.Cipher import AES
import json
from jsonsearch import JsonSearch


url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token=c16cd6d3c08d14e232e27e247357a175"

data = {
    "rid":"R_SO_4_421203731",
    "threadId":"R_SO_4_421203731",
    "pageNo":"1",
    "pageSize":"20",
    "cursor":"-1",
    "offset":"0",
    "orderType":"1",
    "csrf_token":"c16cd6d3c08d14e232e27e247357a175"
    }

e = '010001'
f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
g = '0CoJUm6Qyw8W8jud'
i = "cXVRs8mc0MQvkWmM"
encseckey = "dc9dd003c72d594229558f5209ce852413227cf8f36c6d7dbd043d2303ebfcb2232aa9065c4986072fbfea6ef687c1856fef399ca9d02dc35bb288689d7b51724401f0352f659cd930f38dd15fdfca6df80f6dcc233dffe3db0683f73f4c8ded4383537300282088b0c3078d723f4d465cf6de2c30fc63771e409a22df22df7f"



def get_encSecKey():
    return encseckey

def get_params(data):
    first = encparams(data,g)
    second = encparams(first,i)
    return second

def to_16(data):
    pad = 16 - len(data) % 16
    data += chr(pad) * pad
    return data
def encparams(data,key):
    iv = '0102030405060708'
    data = to_16(data)
    aes = AES.new(key=key.encode('utf-8'), IV=iv.encode('utf-8'), mode=AES.MODE_CBC)
    bs = aes.encrypt(data.encode('utf-8'))
    return str(b64encode(bs), 'utf-8')
# function
# a(a){
#     var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
#     for (d = 0; a > d; d += 1)
#     e = Math.random() * b.length,
#     e = Math.floor(e),
#     c += b.charAt(e);
#     return c
# }
# function
# b(a, b)
# {
# var
# c = CryptoJS.enc.Utf8.parse(b)
# , d = CryptoJS.enc.Utf8.parse("0102030405060708")
# , e = CryptoJS.enc.Utf8.parse(a)
# , f = CryptoJS.AES.encrypt(e, c, {
#     iv: d,
#     mode: CryptoJS.mode.CBC
# });
# return f.toString()
# }
# function
# c(a, b, c)
# {
# var
# d, e;
# return setMaxDigits(131),
# d = new
# RSAKeyPair(b, "", c),
# e = encryptedString(d, a)
# }
# function
# d(d, e, f, g)
# {
# var
# h = {}
# , i = a(16);
# return h.encText = b(d, g),
# h.encText = b(h.encText, i),
# h.encSecKey = c(i, e, f),
# h
# }
resp = requests.post(url=url,data = {
'params': get_params(json.dumps(data)),
 'encSecKey': get_encSecKey()
})

json_data = JsonSearch(resp.text,mode="s")
contens = json_data.search_all_value(key= "content")

num = 1
for i in contens:
    print(str(num) + "," +i)
    num += 1

