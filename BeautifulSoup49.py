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


# with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
#     writer = csv.writer(file, delimiter=';')
#     writer.writerow([
#         'Наименование','Бренд', 'Форм-фактор', 'Ёмкость', 'Объем буферной памяти', 'Цена'])
#
#     url = 'https://parsinger.ru/html/index4_page_1.html'
#
# # Отправляем GET-запрос к указанной странице
# response = requests.get(url=url)
#
# # Устанавливаем кодировку ответа сервера в UTF-8 для корректного отображения текста на кириллице
# response.encoding = 'utf-8'
#
# # Преобразуем текст ответа сервера в объект BeautifulSoup с использованием парсера 'lxml'
# soup = BeautifulSoup(response.text, 'lxml')
#
#
# pagen = [link['href'] for link in soup.find('div', class_='pagen').find_all('a')]
# schema = 'https://parsinger.ru/html/'
#
# list_link = []
#
# for link in pagen:
#      list_link.append(f"{schema}{link}")
#
# nameAll = []
# priceAll = []
# descriptionAll = []
# for stranica in list_link:
#     response = requests.get(url=stranica)
#     response.encoding = 'utf-8'
#     soup = BeautifulSoup(response.text, 'lxml')
#     for x in soup.find_all('a', class_='name_item'):
#       nameAll.append(x.text.strip())
#
#     for x in soup.find_all('p', class_='price'):
#         priceAll.append(x.text)
#
#     for x in soup.find_all('div', class_='description'):
#         descriptionAll.append(x.text.split('\n'))
#
#
# with open('res.csv', 'a', encoding='utf-8-sig', newline='') as file:
#     writer = csv.writer(file, delimiter=';')
#                        #zip(*iterables) --> Объект zip, создающий кортежи до тех пор, пока ввод не будет исчерпан.
#     for item, descr, price in zip(nameAll, descriptionAll, priceAll):
#
#         # Формируем строку для записи                      # if x если x еще существует
#         flatten = item, *[x.split(':')[1].strip() for x in descr if x], price
#
#         writer.writerow(flatten)
#

# ____________________________________________________________________________________________________________________
# Задача:Вам потребуется заходить в каждую товарную карточку и собирать данные, отмеченные на предоставленном изображении.
# Сохраните данные в формате CSV с разделителем ;:
# delimiter=';'
# Отправьте ваш csv-файл на указанный валидатор. Обратите внимание на сохранение порядка строк и столбцов,
# так чтобы они соответствовали эталонному файлу.

# with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
#     writer = csv.writer(file, delimiter=';')
#     writer.writerow([
#         'Наименование','Артикул', 'Бренд', 'Модель', 'Тип', 'Технология экрана',
#         'Материал корпуса','Материал браслета', 'Размер', 'Сайт производителя', 'Наличие', 'Цена',
#         'Старая цена', 'Ссылка на карточку с товаром'])
#
#     url = 'https://parsinger.ru/html/index1_page_1.html'
#
# # Отправляем GET-запрос к указанной странице
# response = requests.get(url=url)
#
# # Устанавливаем кодировку ответа сервера в UTF-8 для корректного отображения текста на кириллице
# response.encoding = 'utf-8'
#
# # Преобразуем текст ответа сервера в объект BeautifulSoup с использованием парсера 'lxml'
# soup = BeautifulSoup(response.text, 'lxml')
#
#
# pagen = [link['href'] for link in soup.find('div', class_='pagen').find_all('a')]
#
# schema = 'https://parsinger.ru/html/'
#
# list_link = []
#
# for link in pagen:
#      list_link.append(f"{schema}{link}")
#
# hrefAll = []
# for stranica in list_link:
#     response = requests.get(url=stranica)
#     response.encoding = 'utf-8'
#     soup = BeautifulSoup(response.text, 'lxml')
#     for link in soup.find_all('a', class_='name_item'):
#         s = link['href']
#         hrefAll.append(s)
#
# list_ref = [] # ссылки на все карточки с часами
# schemaCard = 'https://parsinger.ru/html/'
# for ref in hrefAll:
#     list_ref.append(f"{schema}{ref}")
#
#
# nameAll = []
# articleAll = []
# descriptionAll = []
# in_stockAll = []
# priceAll = []
# old_priceAll = []
# for refend in list_ref:
#     response = requests.get(url=refend)
#     response.encoding = 'utf-8'
#     soup = BeautifulSoup(response.text, 'lxml')
#
#     nameAll.append(soup.find('p', id='p_header').text)
#     dd = str(soup.find('p', class_='article').text).replace('Артикул: ', "").replace(" ", "")
#     articleAll.append(dd)
#     descriptionAll.append(soup.find('ul', id='description').text.split('\n'))
#                           # .replace('Бренд: ', "").replace('Модель: ', "")
#                           # .replace('Тип подключения: ', "").replace('Технология экрана: ', "").replace('Материал корпуса: ', "")
#                           # .replace('Материал браслета: ', "").replace('Размеры: ', "").replace('Сайт производителя: ', ""))
#
#     in_stockAll.append(str(soup.find('span', id='in_stock').text).replace('В наличии: ', ""))
#     priceAll.append(soup.find('span', id='price').text)
#     old_priceAll.append(soup.find('span', id='old_price').text)
#
#
# print(articleAll)
#
#
#
# with open('res.csv', 'a', encoding='utf-8-sig', newline='') as file:
#     writer = csv.writer(file, delimiter=';')
#                        #zip(*iterables) --> Объект zip, создающий кортежи до тех пор, пока ввод не будет исчерпан.
#     for name, article, descr, in_stock, price, old_price, refL in zip(nameAll, articleAll, descriptionAll,in_stockAll, priceAll, old_priceAll, list_ref):
#
#         # Формируем строку для записи                      # if x если x еще существует
#         flatten = name, article, *[x.split(':')[1].strip() for x in descr if x],  in_stock, price, old_price, refL
#         # x.split(':')[1].strip() - разделяет двоеточием (Технология экрана: монохромный) на
#         # [0] -Технология экрана и [1]-монохромный
#
#         writer.writerow(flatten)
#

# ____________________________________________________________________________________________________________________
# Задача: Соберите указанные на изображении ниже данные с сайта тренажёра.
# Заходить в каждую карточку с товаром не требуется, собирать необходимо только с превью карточки.
# Сохраните данные в формате CSV с разделителем ;.
# delimiter=';'
# Заголовки указывать не нужно.


url1 = 'https://parsinger.ru/html/index1_page_1.html'
url2 = 'https://parsinger.ru/html/index2_page_1.html'
url3 = 'https://parsinger.ru/html/index3_page_1.html'
url4 = 'https://parsinger.ru/html/index4_page_1.html'
url5 = 'https://parsinger.ru/html/index5_page_1.html'
urls = [url1,url2,url3,url4,url5]

nameAll = []
priceAll = []
descriptionAll = []

for url in urls:
    # Отправляем GET-запрос к указанной странице
    response = requests.get(url=url)

    # Устанавливаем кодировку ответа сервера в UTF-8 для корректного отображения текста на кириллице
    response.encoding = 'utf-8'

    # Преобразуем текст ответа сервера в объект BeautifulSoup с использованием парсера 'lxml'
    soup = BeautifulSoup(response.text, 'lxml')

    pagen = [link['href'] for link in soup.find('div', class_='pagen').find_all('a')]
    schema = 'https://parsinger.ru/html/'

    list_link = []

    for link in pagen:
         list_link.append(f"{schema}{link}")


    for stranica in list_link:
        response = requests.get(url=stranica)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        for x in soup.find_all('a', class_='name_item'):
          nameAll.append(x.text.strip())

        for x in soup.find_all('p', class_='price'):
            priceAll.append(x.text)

        for x in soup.find_all('div', class_='description'):
            descriptionAll.append(x.text.split('\n'))


with open('res.csv', 'a', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
                       #zip(*iterables) --> Объект zip, создающий кортежи до тех пор, пока ввод не будет исчерпан.
    for item, descr, price in zip(nameAll, descriptionAll, priceAll):

        # Формируем строку для записи                      # if x если x еще существует
        flatten = item, *[x.split(':')[1].strip() for x in descr if x], price

        writer.writerow(flatten)

