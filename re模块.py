import re

#findall 匹配字符串中所有的符合正则的内容 返回列表
# lsd = re.findall(r"\d+","我的电话是10086")
# print(lsd)

#finditer 匹配字符串中的内容（返回的是迭代器）

# it = re.finditer(r"\d+","我的电话是10086，你的电话是10010")
# for i in it :
#     print(i.group())
# search 匹配第一个出现的字符串
#s = re.search(r"\d+","我的电话是10086，你的电话是10010")
#print(s.group())

#match 从第一个字符开始匹配
# s = re.match(r"\d+","10086，你的电话是10010")
# print(s.group())

#预加载正则表达式
# obj = re.compile(r"\d+")
# ret = obj.finditer("我的电话是10086，你的电话是10010")
# for i in ret:
#     print(i.group())


s = """
<div class = 'jay'> <span id = '1'>郭麒麟</span></div>
<div class = 'jj'> <span id = '2'>宋秩</span></div>
<div class = 'joy'> <span id = '3'>范思哲</span></div>
<div class = 'job'> <span id = '4'>返现</span></div>
"""

#（？P<组名>正则）可以对匹配内容进行再一次匹配
obj = re.compile(r"<div class = '.*?'> <span id = '.*?'>(?P<name>.*?)</span></div>",re.S)
result = obj.finditer(s)
for i in result:
    print(i.group("name"))

