from bs4 import BeautifulSoup
import requests
# from urllib.request import Request, urlopen
# from urllib import urlretrieve
import urllib.request


def dl_jpg(url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path)


source = requests.get(
    'https://mangakakalot.com/chapter/please_dont_bully_me_nagatoro/chapter_1').text

soup = BeautifulSoup(source, 'lxml')

div = soup.find("div", {"class": "vung-doc"})
data = []
# print(source)
for img in div:
    data.append(img)

data.remove(data[0])
data.remove(data[len(data)-1])

# print(data[0]['src'])
data1 = []
for img in data:
    try:
        data1.append(img['src'])
    except:
        pass

i = 1

for img in data1:
    urllib.request.urlretrieve(img, "./image/"+str(1)+".jpg")
    i = i+1
