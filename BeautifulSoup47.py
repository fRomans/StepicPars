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

# url = 'https://parsinger.ru/table/2/index.html'
# response = requests.get(url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'html.parser')
#
# # Ищем первую таблицу на странице
# table = soup.find('table')
#
# # Извлекаем все строки таблицы
# rows = table.find_all('tr')
# sum: int = 0
#
# # Проходим по строкам таблицы, начиная со второй (индекс 1), так как первая строка - это заголовки
# for row in rows[1:]:
#     # Извлекаем ячейки текущей строки
#     columns = row.find_all(['td'])
#     el = columns[0].text
#     el = float(el)
#     sum += el
# print(sum)

# __________________________________________
# Задача:Cобрать только числа, отформатированные жирным шрифтом.
# .find('b')
# или
# .find_all('b')
# Суммировать выделенные числа.

# url = 'https://parsinger.ru/table/3/index.html'
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
# sum: int = 0
# # Проходим по строкам таблицы, начиная со второй (индекс 1), так как первая строка - это заголовки
# for row in rows[1:]:
#     columns =row.find_all('td')
#
#     for i in columns:
#         d = i.find('b')
#         if d!= None:
#           d = d.text
#           d = float(d)
#           sum += d
# print(sum)

# __________________________________________
# Задача:Выделить и подсчитать сумму всех чисел из зелёных ячеек.
# Внести полученную сумму в поле ответа.

# url = 'https://parsinger.ru/table/4/index.html'
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
# sum: int = 0
# # Проходим по строкам таблицы, начиная со второй (индекс 1), так как первая строка - это заголовки
# for row in rows[1:]:
#     columns =row.find_all('td', class_="green")
#
#     for i in columns:
#         d = i
#         d = d.text
#         d = float(d)
#         sum += d
# print(sum)

# __________________________________________
# Задача: Для каждой строки таблицы найти числа в оранжевой и голубой ячейках, после чего умножить их друг на друга.
# Сложить все получившиеся произведения, чтобы получить общую сумму.

# url = 'https://parsinger.ru/table/5/index.html'
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
# sum: int = 0
# # Проходим по строкам таблицы, начиная со второй (индекс 1), так как первая строка - это заголовки
# for row in rows[1:]:
#     columns1 =row.find('td', class_="orange")
#     columns1 = columns1.text
#     columns1 = float(columns1)
#     columns2 =row.find_all(['td'])
#     columns2 = columns2[14]
#     columns2 = columns2.text
#     columns2 = float(columns2)
#     elem = float(columns1 * columns2)
#     sum += elem
# print(sum)

# __________________________________________
# Задача:Для каждого столбца вычислить сумму всех чисел в этом столбце.
# Округлить каждое получившееся значение до трех знаков после запятой.
# row: round(sum(column), 3)
# Формировать словарь, где ключами будут названия столбцов, а значениями - рассчитанные суммы.

# url = 'https://parsinger.ru/table/5/index.html'
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
# # все суммы по столбцам
# all_summ = []
# sum: int = 0
#
# for i in range(15):
# # Проходим по строкам таблицы, начиная со второй (индекс 1), так как первая строка - это заголовки
#         for row in rows[1:]:
#             columns =row.find_all('td')
#             el = columns[i].text
#             el = float(el)
#             sum += el
#         sum = round(sum, 3)
#         all_summ.append(sum)
#         sum = 0
# # print(all_summ)
#
# all_title = []
#
# for i in range(15):
#     for row in rows[:1]:
#         columns =row.find_all('th')
#         el = str(columns[i].text)
#     all_title.append(el)
#
# # print(all_title)
#
# yyy = {}
# for i in range(15):
#     yyy[all_title[i]] = all_summ[i]
# print(yyy)

# __________________________________________
# Задача:Пройтись по каждой ячейке каждой таблицы и проверить значение на кратность трём.
# Если число кратно трем, добавить его к общей сумме.

# url = 'https://parsinger.ru/4.8/7/index.html'
# response = requests.get(url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'html.parser')
#
# # Ищем первую таблицу на странице
# tables = soup.findAll('table')
#
# sum = 0
# for table in tables:
#         rows = table.find_all('tr')
#         for row in rows:
#                 columns =row.find_all('td')
#                 for column in columns:
#                         el = column.text
#                         el = int(el)
#                         if el % 3 == 0:
#                                 sum += el
# print(sum)


# __________________________________________
# Задача: Извлечь данные из каждой объединённой ячейки(всего 16 ячеек), объединённую ячейку можно определить по атрибуту colspan.
# Суммировать все числовые значения, полученные из объединённых ячеек.

url = 'https://parsinger.ru/4.8/8/index.html'
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
tags = soup.find_all(['td', 'th'], {'colspan': True})
sums = 0
#  ТЕГИ БЕЗ ПЕРВОГО ТЕГА   table ( ОН НЕ ПОДХОДИТ)
for i in tags[1:]:
        sums += int(i.text)

print(sums)
# _________________________________________________________________

