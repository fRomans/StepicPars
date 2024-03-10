import csv

import requests
from bs4 import BeautifulSoup
import json

# ____________________________________________________________________________________________________________________
# Задача:
# 1 ------------------------------------------------------
# url = 'http://parsinger.ru/html/mouse/3/3_11.html'
# response = requests.get(url=url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')
# # 1 ------------------------------------------------------
#
# # 2 ------------------------------------------------------
# result_json = {
#     'name': soup.find('p', id='p_header').text,
#     'price': soup.find('span', id='price').text}
# # 2 ------------------------------------------------------
#
# # 3 ------------------------------------------------------
# with open('res.json', 'w', encoding='utf-8') as file:
#     json.dump(result_json, file, indent=4, ensure_ascii=False)
# # 3 ------------------------------------------------------

# # ____________________________________________________________________________________________________________________
# # Задача:
#
# # 1 ------------------------------------------------------
# url = 'http://parsinger.ru/html/index3_page_1.html'
# response = requests.get(url=url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')
# # 1 ------------------------------------------------------
#
# # 2 ------------------------------------------------------
# name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
# description = [x.text.strip().split('\n') for x in soup.find_all('div', class_='description')]
# price = [x.text for x in soup.find_all('p', class_='price')]
# # 2 ------------------------------------------------------
#
# result_json = []
# # 3 ------------------------------------------------------
# for list_item, price_item, name in zip(description, price, name):
#     result_json.append({
#         'name': name,
#         'brand': [x.split(':')[1] for x in list_item][0],
#         'type': [x.split(':')[1] for x in list_item][1],
#         'connect': [x.split(':')[1] for x in list_item][2],
#         'game': [x.split(':')[1] for x in list_item][3],
#         'price': price_item
#
#     })
#
# # 3 ------------------------------------------------------
#
# # 4 ------------------------------------------------------
# with open('res.json', 'w', encoding='utf-8') as file:
#     json.dump(result_json, file, indent=4, ensure_ascii=False)
# # 4 ------------------------------------------------------

# ____________________________________________________________________________________________________________________
# Задача:

# response = requests.get('http://parsinger.ru/html/watch/1/1_1.html')
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')
# description = soup.find('ul', id='description').find_all('li')
#
# for li in description:
#     print(li['id'])

#  или списком
#  li_id = [x['id'] for x in description]
# print(li_id)


    # ____________________________________________________________________________________________________________________
# Задача:
# Не "проваливайтесь" внутрь каждой карточки. Соберите только информацию из превью.
# Сохраните данные в JSON файл с использованием указанных параметров.
# json.dump(res, file, indent=4, ensure_ascii=False)

url = 'https://parsinger.ru/html/index4_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

pagen = [link['href'] for link in soup.find('div', class_='pagen').find_all('a')]

schema = 'https://parsinger.ru/html/'

list_link = []

for link in pagen:
     list_link.append(f"{schema}{link}")

nameAll = []
priceAll = []
descriptionAll = []
for stranica in list_link:
    response = requests.get(url=stranica)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    for x in soup.find_all('a', class_='name_item'):
      nameAll.append(x.text.strip())

    for x in soup.find_all('p', class_='price'):
        priceAll.append(x.text)

    for x in soup.find_all('div', class_='description'):
        descriptionAll.append(x.text.strip().split('\n'))

result_json = []
# 3 ------------------------------------------------------
for list_item, price_item, name in zip(descriptionAll, priceAll, nameAll):

    result_json.append({
        'Наименование': name,
        'Бренд': [x.split(':')[1].strip() for x in list_item][0],
        'Форм-фактор': [x.split(':')[1].strip() for x in list_item][1],
        'Ёмкость': [x.split(':')[1].strip() for x in list_item][2],
        'Объем буферной памяти': [x.split(':')[1].strip() for x in list_item][3],
        'Цена': price_item

    })

with open('res.json', 'w', encoding='utf-8') as file:
        json.dump(result_json, file, indent=4, ensure_ascii=False)


