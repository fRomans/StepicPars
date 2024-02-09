import requests
from bs4 import BeautifulSoup


# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
#     'x-requested-with': 'XMLHttpRequest'
# }
#
# url = "https://bitality.cc/Home/GetSum?GiveName=Ethereum&GetName=Bitcoin&Sum=4.1895414&Direction=0"
# response = requests.get(url=url, headers=headers).json()
# print(response)

# __________________________________________
# Задача: формируем такую ссылку:
#
# https://bitality.cc/Home/GetSum?GiveName=Monero&GetName=Dash&Sum=100&Direction=0

# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
#     'x-requested-with': 'XMLHttpRequest',
# }
#
# data = {
#     "GiveName": "Monero",
#     "GetName": "Dash",
#     "Sum": 100,
#     "Direction": 0
# }
#
# url = "https://bitality.cc/Home/GetSum?"
# response = requests.get(url=url, headers=headers, params=data).json()
# print(response)

# _________ТАБЛИЦЫ_____________ТАБЛИЦЫ_________ТАБЛИЦЫ___________ТАБЛИЦЫ_____ТАБЛИЦЫ_________ТАБЛИЦЫ_______ТАБЛИЦЫ__________________
# Задача:извлечь имена и возраст из этой таблицы.

# url = 'https://parsinger.ru/4.8/1/index.html'
# response = requests.get(url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'html.parser')
#
# # Ищем первую таблицу на странице
# table = soup.find('table')
#
# # Извлекаем все строки таблицы
# rows = table.find_all('tr')
#
# # Проходим по строкам таблицы, начиная со второй (индекс 1), так как первая строка - это заголовки
# for row in rows[1:]:
#     # Извлекаем ячейки текущей строки
#     columns = row.find_all('td')
#     # Первая ячейка содержит имя
#     name = columns[0].text
#     # Вторая ячейка содержит возраст
#     age = columns[1].text
#     # Выводим результат
#     print(f'Имя: {name}, Возраст: {age}')

# __________________________________________
# Задача:извлечь заголовки + имена + возраст из  таблицы.

# url = 'https://parsinger.ru/4.8/2/index.html'
# response = requests.get(url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'html.parser')
#
# # Ищем первую таблицу на странице
# table = soup.find('table')
#
# # Извлекаем заголовки таблицы, пройдясь по всем элементам th в таблице и получив их текст
# headers = [header.text for header in table.find_all('th')]
#
# # Извлекаем строки таблицы, начиная со второй (индекс 1), так как первая строка - это заголовки
# rows = table.find_all('tr')[1:]
#
# # Создаём пустой список для данных
# data = []
#
# # Проходим по каждой строке в таблице
# for row in rows:
#     # Собираем данные строки в словарь, ключами которого являются заголовки, а значениями - данные ячеек
#     row_data = dict(zip(headers, (cell.text for cell in row.find_all('td'))))
#     # Функция zip() используется для совмещения двух и более списков в один. Она возвращает итератор кортежей,
#     # где i-ый кортеж содержит i-ый элемент из каждого из переданных списков.
#
#     # Добавляем словарь с данными строки в общий список
#     data.append(row_data)
#
# # Выводим все собранные данные
# for entry in data:
#     print(entry)

# __________________________________________
# Задача:извлечь заголовки + имена + возраст из  таблицы.Усложним наш пример, добавив в таблицу ещё несколько столбцов,
# вложенные таблицы и атрибуты к ячейкам.

# def scrape_table(url):
#     response = requests.get(url)
#     response.encoding = 'utf-8'
#     soup = BeautifulSoup(response.text, 'html.parser')
#     # Поиск первой таблицы на веб-странице с атрибутом 'border' равным '3'
#     table = soup.find('table', {'border': '3'})
#     # Поиск всех строк (tr) в таблице и сохранение их в переменной rows
#     rows = table.find_all('tr')
#     data = []
#     # Проход по всем строкам таблицы, начиная со второй
#     for row in rows[1:]:
#         cell_data = {}
#         # Поиск всех ячеек (td или th) в текущей строке
#         cells = row.find_all(['td', 'th'])
#         # Если в строке больше двух ячеек, извлекаем данные
#         if len(cells) > 2:
#             # Извлечение и сохранение данных в соответствующих ключах словаря
#             cell_data['Имя'] = cells[0].text
#             cell_data['Фамилия'] = cells[1].text
#             cell_data['Возраст'] = cells[2].text
#             # Инициализация словаря для хранения контактных данных
#             contacts = {}
#             # Извлечение контактных данных из ячейки
#             contact_rows = cells[3].find_all('tr')
#             for contact_row in contact_rows:
#                 contact_cells = contact_row.find_all('td')
#                 contacts[contact_cells[0].text] = contact_cells[1].text
#             # Добавление контактных данных в cell_data
#             cell_data['Контакты'] = contacts
#             # Извлечение данных о хобби, если они есть
#             hobby = soup.find('td', {'rowspan': '2'}).text
#             if hobby:
#                 cell_data['Хобби'] = hobby
#             data.append(cell_data)
#     return data
#
#
# url = "https://parsinger.ru/4.8/3/index.html"
# scraped_data = scrape_table(url)
# print(scraped_data)

# __________________________________________
# Задача:извлечь заголовки + имена + возраст из  таблицы.Усложним наш пример, добавив в таблицу ещё несколько столбцов,
# вложенные таблицы и атрибуты к ячейкам.

# url = 'https://parsinger.ru/4.8/4/index.html'
#
# response = requests.get(url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'html.parser')
#
# # Ищем первую таблицу на странице
# table = soup.find('table')
#
# # Задаём заголовки для таблицы
# headers = ['Имя', 'Фамилия', 'Возраст', 'Контакты', 'Хобби', 'Фото']
#
# # Получаем все строки таблицы, начиная со второй (индекс 1), так как первая строка - это заголовки
# rows = table.find_all('tr')[1:]
#
# # Создаём пустой список для данных
# data = []
#
# # Проходим по каждой строке в таблице
# for row in rows:
#     # Инициализируем словарь для данных одной строки
#     row_data = {}
#     # Проходим по каждой ячейке в строке и соответствующему заголовку
#     for header, cell in zip(headers, row.find_all('td')):
#         # Проверяем, есть ли в ячейке ссылка
#         if cell.find('a'):
#             links = cell.find_all('a')
#             # Проверяем, является ли первая ссылка email-ссылкой
#             if 'mailto' in links[0]['href']:
#                 row_data['Email'] = links[0].text
#                 row_data['Телефон'] = links[1].text
#             else:
#                 row_data[header] = cell.text
#         # Проверяем, есть ли в ячейке изображение
#         elif cell.find('img'):
#             row_data['Фото'] = cell.find('img')['src']
#         # Если ячейка не содержит ни ссылки, ни изображения, сохраняем её текст
#         else:
#             row_data[header] = cell.text
#
#     # Добавляем данные строки в общий список
#     data.append(row_data)
#
# # Выводим все собранные данные
# for entry in data:
#     print(entry)

# __________________________________________
# Задача: Произвести парсинг данных из таблицы.
# Отфильтровать и извлечь все уникальные числа, исключая числа в заголовке таблицы.
# Посчитать сумму этих чисел.

# url = 'https://parsinger.ru/table/1/index.html'
# response = requests.get(url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'html.parser')
#
# # Ищем первую таблицу на странице
# table = soup.find('table')
#
# # Извлекаем все строки таблицы
# rows = table.find_all('tr')
#
# all_td = []
#
# # Проходим по строкам таблицы, начиная со второй (индекс 1), так как первая строка - это заголовки
# for row in rows[1:]:
#     # Извлекаем ячейки текущей строки
#     columns = row.find_all(['td'])
#
#     # 15 столбцов . columns[i]- это весь столбец до низа
#     for i in range(15):
#         chis = float(columns[i].text)
#         all_td.append(chis)
#
# unique = []
# #  проход по значениям
# for number in all_td:
#     #  берем только те, которых нет в массиве(уникальные)
#     if number not in unique:
#         unique.append(number)
#
# sum = 0
# for n in unique:
#     sum = sum+n
# print(sum)

# __________________________________________
# Задача: Произвести парсинг данных из первого столбца таблицы.
# Суммировать все числа, найденные в первом столбце.

url = 'https://parsinger.ru/table/2/index.html'
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

# Ищем первую таблицу на странице
table = soup.find('table')

# Извлекаем все строки таблицы
rows = table.find_all('tr')
sum: int = 0

# Проходим по строкам таблицы, начиная со второй (индекс 1), так как первая строка - это заголовки
for row in rows[1:]:
    # Извлекаем ячейки текущей строки
    columns = row.find_all(['td'])
    el = columns[0].text
    el = float(el)
    sum += el
print(sum)
