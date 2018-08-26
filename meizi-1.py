import requests
from bs4 import BeautifulSoup
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

Hostreferer = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer': 'http://www.mzitu.com'
}
Picreferer = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer': 'http://i.meizitu.net'
}
all_url = 'http://www.mzitu.com/all'

start_html = requests.get(all_url, headers=Hostreferer)

soup = BeautifulSoup(start_html.text, 'lxml')

all = soup.find('div', class_='all').find_all('a')

all.remove(all[0])
# print(all)

for a in all:
    title = a.get_text()
    href = a['href']
    html = requests.get(href, headers=Hostreferer)
    html_soup = BeautifulSoup(html.text, 'lxml')
    max_span = html_soup.find('div', class_='pagenavi').find_all('span')[-2].get_text()

    for page in range(1, int(max_span) + 1):
        page_url = href + "/" + str(page)
        img_html = requests.get(page_url, headers=Hostreferer)
        img_soup = BeautifulSoup(img_html.text, 'lxml')
        img_url = img_soup.find('div', class_='main-image').find('img')['src']
        print(img_url)
        name = img_url[-9:-4]

        img = requests.get(img_url, headers=Picreferer)
        print(img)
        f = open(name + '.jpg', 'ab')  # 写入多媒体文件必须要 b 这个参数！！必须要！！
        f.write(img.content)
        f.close()
