import requests

url = "https://m.acgnfl.com/24/09/content_54/546255/6769f98126eda7168d54aa2743e4c642.webp"
file_path = "C:/Users/Administrator/Desktop/picture/image.jpg"

response = requests.get(url)
with open(file_path, "wb") as f:
    f.write(response.content)

print("文件下载完成")