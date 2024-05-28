"""
2023/12/23 00:00|Домашнее задание по теме "Обзор сторонних библиотек Python

https://urban-university.ru/members/courses/course999421818026/20231223-0000domasnee-zadanie-po-teme-obzor-storonnih-bibliotek-python-400269495184
"""

"""
Опрашиваем сайт суда
"""
import requests
import sys
from pprint import pprint
from requests.exceptions import HTTPError

url = 'https://leninsky--sml.sudrf.ru/modules.php?name=sud_delo&srv_num=1&name_op=sf&delo_id=1540005'
url1 = 'https://www.mos.ru'
url2 = 'https://api.api-parser.com/?service=sudrf&method=search&text=%D1%82%D0%B5%D0%BA%D1%81%D1%82%20%D0%BF%D0%BE%D0%B8%D1%81%D0%BA%D0%B0&key=API_KEY'


# # family_name_form = '"G1_PARTS__NAMESS"'
# # input_data = 'Данилов Александр Валерьевич'
# datas = {'G1_PARTS__NAMESS': 'Данилов Александр Валерьевич'}
# s = requests.Session()
# info = s.post(url, data=datas)
# with open('result.txt', 'w+') as f:
#     f.write(info.text)
#

# try:
#     response = requests.get(url2)
#
#     # если ответ успешен, исключения задействованы не будут
#     response.raise_for_status()
# except HTTPError as a:
#     print(f'HTTP error occurred: {a}')  # Python 3.6
# except Exception as err:
#     print(f'Other error occurred: {err}')  # Python 3.6
# else:
#     print('Success!')
# #
# # # response.encoding = 'utf-8'
#
# # response = requests.post(url2)
# # # response.encoding = 'utf-8'
# pprint(response.url)
# создаем словарь
# pip install fake_useragent

from bs4 import BeautifulSoup as BS
import requests
from fake_useragent import UserAgent

URL = "https://nsk.rbc.ru/"

# получаем сайт с передачей случайного user-agent
r = requests.get(URL, headers={"user-agent": UserAgent().random})
# получаем весь текст-код сайта
text = r.text

# создаем парсера
soup = BS(text, "html.parser")
# ищем все элементы по исследованному тегу и классу
news = soup.find_all("span", class_="main__feed__title")
d = []
for n in news:
    # получаем ссылку на новость
    link = n.parent.parent['href']
    # получаем заголовок новости
    header = n.text
    d.append((header, link))

# делаем текст
t = ''
for i in d:
    t += i[0] + ';' + i[1] + '\n'
# заносим текст в файл
with open("data1.csv", "w", encoding="utf-8") as f:
    f.write(t)
