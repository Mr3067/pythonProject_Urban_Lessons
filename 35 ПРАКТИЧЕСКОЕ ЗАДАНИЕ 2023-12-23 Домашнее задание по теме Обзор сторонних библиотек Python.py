"""
ПРАКТИЧЕСКОЕ ЗАДАНИЕ
2023/12/23 00:00|Домашнее задание по теме "Обзор сторонних библиотек Python"

https://urban-university.ru/members/courses/course999421818026/20231223-0000domasnee-zadanie-po-teme-obzor-storonnih-bibliotek-python-400269495184

"""

import requests
from bs4 import BeautifulSoup
from fake_useragent import FakeUserAgent
import os

page_number = 1
pic_number = 1
user = FakeUserAgent().random
head = {
    'user_agent': user
}
site = 'https://zastavok.net/'
folder = 'pic_Danilov'

if not os.path.exists(f'{os.getcwd()}\\{folder}'):
    print('No')
    os.mkdir(f'{os.getcwd()}\\{folder}')
main_page = requests.get(site, headers=head).text
soup_main = BeautifulSoup(main_page, 'lxml')
totle_page_number = soup_main.find('div', id="clsLink3").find_all('a')[-2].text
totle_pic_number = soup_main.find('div', id="clsLink3").text.split('Всего обоев: ')[1]
print(f'Будет скачено {totle_pic_number} фотографий с {totle_page_number} страниц сайта {site}')

while page_number <= int(totle_page_number):
    url = f'{site}{page_number}'
    answer = requests.get(url=url, headers=head).text
    soup1 = BeautifulSoup(answer, 'lxml')
    pic_block = soup1.find('div', class_="block-photo")
    foto_in_block = pic_block.find_all('div', class_="short_full")
    for section in foto_in_block:
        image_link = section.find('a').get('href')
        download_page = requests.get(f'{site}{image_link}').text
        soup2 = BeautifulSoup(download_page, 'lxml')
        url_download = f'{site}{soup2.find('div', class_='block_down').find('a').get('href')}'
        print(pic_number, url_download)
        with open(f'{os.getcwd()}\\{folder}\\{pic_number}.jpg', 'wb') as f:
            f.write(requests.get(url_download, headers=head).content)
        pic_number += 1
        # break

    #break
    page_number += 1