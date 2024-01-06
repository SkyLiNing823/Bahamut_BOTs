import requests
from bs4 import BeautifulSoup
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

GPs = []
names = []

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
    shouter1 = bsObj.findAll('a', {'class': 'TS1'})
    for item in shouter1:
        names.append(item)
    shouter2 = bsObj.findAll('span', {'class': 'BC4'})
    for item in shouter2:
        artNum += 1
        gp = item.text[:-3]
        GPs.append(gp)
    print('Analyzing {}/{} ......'.format(page, final_page))
    page += 1

names.reverse()
GPs.reverse()
GPs = list(map(int, GPs))

x = [number for number in range(1, artNum+1)]
y = GPs

plt.figure(figsize=(60, 20))  # *100
plt.title('GP_analysis for '+owner)
plt.ylabel('GP')
plt.xlabel('Titles')
plt.xticks(x, names, rotation=90)
plt.yticks([10, 20, 50, max(GPs)])
plt.axhline(10, color="Red")
plt.axhline(20, color="Blue")
plt.axhline(50, color="Orange")
for a, b in zip(x, y):
    plt.text(a, b+0.5, b, ha='center', va='bottom', fontsize=6)
plt.plot(x, y)
plt.show()
