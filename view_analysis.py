import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

views = []

send_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    "Connection": "keep-alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8"}

page = 1
final_page = 1
artNum = 0
owner = input('Please enter the ID : ')

URL = 'https://home.gamer.com.tw/creation.php?page=1&owner='+owner+'&v=3&t=0'
request = requests.get(URL, headers=send_headers)
html = request.content
bsObj = BeautifulSoup(html, "html.parser")
shouter = bsObj.findAll('a')
for p in shouter:
    if p.text.isdigit() and ('TS1' not in str(p)):
        if int(p.text) > final_page:
            final_page = int(p.text)

while page <= final_page:
    URL = 'https://home.gamer.com.tw/creation.php?page=' + \
        str(page)+'&owner='+owner+'&v=3&t=0'
    request = requests.get(URL, headers=send_headers)
    html = request.content
    bsObj = BeautifulSoup(html, "html.parser")
    shouter2 = bsObj.findAll('span', {'class': 'ST1'})
    for item in shouter2:
        item = str(item)
        if '：' in item:
            artNum += 1
            num = 0
            while(item.find('│') != -1):
                n = item.index('│')
                item = item[n+1:]
            item = item[3:-7]
            print(item)
            views.append(item)
    print('Analyzing {}/{} ......'.format(page, final_page))
    page += 1

views.reverse()
views = list(map(int, views))

x = [number for number in range(1, artNum+1)]
y = views

plt.figure(figsize=(60, 20))  # *100
plt.title('view_analysis for '+owner)
plt.ylabel('Number of views')
plt.xlabel('Number of Articles')
plt.yticks([300, 500, 1000, max(views)])
plt.axhline(300, color="Red")
plt.axhline(500, color="Blue")
plt.axhline(1000, color="Orange")
for a, b in zip(x, y):
    plt.text(a, b+0.5, b, ha='center', va='bottom', fontsize=6)
plt.plot(x, y)
plt.show()
