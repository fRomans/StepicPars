import csv
import requests
from bs4 import BeautifulSoup


# __________________________________________
# Задача: разложить список в csv формат и записать в файл res.csv
# lst = ['one', 'two', 'three']
#
# with open('res.csv', 'w', newline='', encoding='utf-8-sig') as file:
#     writer = csv.writer(file, delimiter=';')
#     writer.writerow(lst)


# ____________________________________________________________________________________________________________________
# Задача: Получить в Exel(открыть в exel) таблицу с данными

# 1 ------------------------------------------------------
# В первом блоке мы создали файл res.csv и определили в нем первые 12 ячеек для заголовков.
# with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
#     writer = csv.writer(file, delimiter=';')
#     writer.writerow([
#         'Наименование', 'Артикул', 'Бренд', 'Модель',
#         'Тип', 'Игровая', 'Размер', 'Разрешение','Подсветка',
#         'Сайт производителя', 'В наличии', 'Цена'])
# # 1 ------------------------------------------------------
#
# # 2 ------------------------------------------------------
# # Вторая часть кода -  это стандартные запросы к сайту, которые вы уже использовали при выполнении задач;
# url = 'http://parsinger.ru/html/mouse/3/3_11.html'
#
# response = requests.get(url=url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')
# # 2 ------------------------------------------------------
#
# # 3 ------------------------------------------------------
# # Третья часть хорошо показывает, что мы получаем нужные нам элементы и храним их в переменных, которые в 4-м пункте
# # мы передаем в метод .writerow().
# name = soup.find('p', id='p_header').text
# article = soup.find('p', class_='article').text.split(': ')[1]
# brand = soup.find('li', id='brand').text.split(': ')[1]
# model = soup.find('li', id='model').text.split(': ')[1]
# type = soup.find('li', id='type').text.split(': ')[1]
# purpose = soup.find('li', id='purpose').text.split(': ')[1]
# light = soup.find('li', id='light').text.split(': ')[1]
# size = soup.find('li', id='size').text.split(': ')[1]
# dpi = soup.find('li', id='dpi').text.split(': ')[1]
# site = soup.find('li', id='site').text.split(': ')[1]
# in_stock = soup.find('span', id='in_stock').text.split(': ')[1]
# price = soup.find('span', id='price').text.split(' ')[0]
# # 3 ------------------------------------------------------
#
# # 4 ------------------------------------------------------
# # И в результате выполнения 4-го блока кода мы получаем готовый файл .csv, в котором будут красиво лежать наши данные.
# with open('res.csv', 'a', encoding='utf-8-sig', newline='') as file:
#     writer = csv.writer(file, delimiter=';')
#     writer.writerow([
#         name, article, brand, model,
#         type, purpose, light, size, dpi,
#         site, in_stock, price])
# # 4 -------------------------------------------------------------------------------------------------------------------------------
#

# ____________________________________________________________________________________________________________________
# Задача: получить аккуратно отформатированные данные, лежащие в таблице excel

# 1 ------------------------------------------------------
# with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
#     writer = csv.writer(file, delimiter=';')
#     writer.writerow([
#         'Наименование', 'Цена', 'Бренд', 'Тип', 'Подключение', 'Игровая'])
# # 1 ------------------------------------------------------
#
# # 2 ------------------------------------------------------
# url = 'http://parsinger.ru/html/index3_page_2.html'
#
# response = requests.get(url=url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')
# # 2 ------------------------------------------------------
#
# # 3 ------------------------------------------------------
# # Извлекаем имена товаров и убираем лишние пробелы
# name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
#
# # Извлекаем описание товаров и разбиваем на строки
# description = [x.text.split('\n') for x in soup.find_all('div', class_='description')]
#
# # Извлекаем цены товаров
# price = [x.text for x in soup.find_all('p', class_='price')]
# # 3 ------------------------------------------------------
#
#
# # 4------------------------------------------------------
# # Открываем файл для дополнительной записи данных
# with open('res.csv', 'a', encoding='utf-8-sig', newline='') as file:
#     writer = csv.writer(file, delimiter=';')
#                        #zip(*iterables) --> Объект zip, создающий кортежи до тех пор, пока ввод не будет исчерпан.
#     for item, price, descr in zip(name, price, description):
#
#         # Формируем строку для записи
#         flatten = item, price, *[x.split(':')[1].strip() for x in descr if x] # if x если x еще существует
#         print(*[x.split(':')[1].strip() for x in descr if x])
#         writer.writerow(flatten)
#
# print('Файл res.csv создан')


# ____________________________________________________________________________________________________________________
# Задача: "Проваливаться" в каждую карточку не нужно, соберите информацию с превью карточки.
# При создании CSV используйте разделитель:
# delimiter=';'
# Отправьте готовый csv файл в валидатор, для успешной валидации файла, необходимо сохранить тот же порядок строк и столбцов что и в эталонном файле.
# Если файл совпадает с эталонным на сервере, вы получите код который необходимо вставить в поле ответа.


with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow([
        'Наименование','Бренд', 'Форм-фактор', 'Ёмкость', 'Объем буферной памяти', 'Цена'])

    url = 'https://parsinger.ru/html/index4_page_1.html'

response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
pagen = [link.text for link in soup.find('div', class_='pagen').find_all('a')][-1]

name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
price = [x.text for x in soup.find_all('p', class_='price')]
description = [x.text.split('\n') for x in soup.find_all('div', class_='description')]

with open('res.csv', 'a', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
                       #zip(*iterables) --> Объект zip, создающий кортежи до тех пор, пока ввод не будет исчерпан.
    for item, descr, price in zip(name, description, price):

        # Формируем строку для записи                      # if x если x еще существует
        flatten = item, *[x.split(':')[1].strip() for x in descr if x], price

        writer.writerow(flatten)