import requests

url = 'https://www.pearvideo.com/video_1707010'

contId = url.split('_')[1]

videoStatusUrl = f'https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.48241643436585346'

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
    'Referer': 'https://www.pearvideo.com/video_1707010'
}

response = requests.get(videoStatusUrl,headers=header)

dic = response.json()

srcUrl = dic['videoInfo']['videos']['srcUrl']
systemTime = dic['systemTime']

# https://video.pearvideo.com/mp4/adshort/20201114/1731503704407-15483292_adpkg-ad_hd.mp4
# https://video.pearvideo.com/mp4/adshort/20201114/cont-1707010-15483292_adpkg-ad_hd.mp4

srcUrl = srcUrl.replace(systemTime,f'cont-{contId}')


print(srcUrl)

with open(f'{contId}.mp4','wb') as f:
    f.write(requests.get(srcUrl,headers=header).content)
    print('over')