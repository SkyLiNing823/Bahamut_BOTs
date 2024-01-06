import requests
from bs4 import BeautifulSoup
import csv
from operator import attrgetter


class article:
    def __init__(self, name, num):
        self.name = name
        self.collect = num

    def __repr__(self):
        return repr((self.name, self.collect))


article_list = []

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
    shouter = bsObj.findAll('a', {'class': 'TS1'})
    for item in shouter:
        artNum += 1
        Name = item.text
        url = 'https://home.gamer.com.tw/'+item['href']
        request = requests.get(url, headers=send_headers)
        html = request.content
        bsObj = BeautifulSoup(html, "html.parser")
        try:
            collect_a = bsObj.find('a', id='collect_a').text
            num = int(collect_a)
        except:
            num = 0
        article_list.append(article(Name, num))
    print('Analyzing {}/{} ......'.format(page, final_page))
    page += 1

article_list = sorted(article_list, key=attrgetter('collect'), reverse=True)

filename = 'data\\'+owner+'_data.csv'
with open(filename, 'w', newline='', encoding='utf_8_sig') as csvfile:
    writer = csv.writer(csvfile)
    for i in range(artNum):
        name = article_list[i].name
        target = article_list[i].collect
        writer.writerow([name, target])
