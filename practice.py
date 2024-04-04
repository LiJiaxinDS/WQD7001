import csv

import requests
from bs4 import BeautifulSoup

with open('tv_100.csv', 'a', encoding='utf-8', newline='') as f:
    w = csv.writer(f)
    w.writerow(['电视剧名', '评分'])

def getHTML():
    #记得格式！
    header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
    for i in range(4):
        url='https://www.douban.com/doulist/116238969/?start='+str(i*25)+'&sort=seq&playable=0&sub_type='
        try:
            r=requests.get(url,headers=header,timeout=30)
            # print(r.status_code)
            parse_html(r.text)
        except:
            return 'ERROR_GETHTML'


def parse_html(html):
    soup=BeautifulSoup(html,'lxml')
    tv_list=soup.find_all('div',class_='bd doulist-subject')
    with open('tv_100.csv', 'a', encoding='utf-8', newline='') as f:
        w = csv.writer(f)
        for tv in tv_list:
            title=tv.find('div',class_='title').get_text().strip()
            rate=tv.find('div',class_='rating').find_all('span')[1].get_text().strip()
            # print(title,rate)
            w.writerow([title,rate])

if __name__ == '__main__':
    getHTML()