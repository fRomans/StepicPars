from bs4 import BeautifulSoup
import requests

# url = 'http://parsinger.ru/html/index1_page_3.html'
# response = requests.get(url=url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')
# schema = 'http://parsinger.ru/html/'
# pagen = [link.text for link in soup.find('div', class_='pagen').find_all('a')][-1]
# #Мы применили индексацию [-1], чтобы получить последний элемент списка, в котором хранился весь список значений пагинации.
# print(pagen)



# __________________________________________
# Задача:Посетить указанный веб-сайт и извлечь названия товаров со всех четырех страниц.
# Необходимо организовать данные таким образом, чтобы названия товаров с каждой страницы хранились в отдельном списке.
# По завершении работы у вас должен быть главный список, содержащий четыре вложенных списка с названиями товаров.

# # Задаем URL-адрес веб-страницы для парсинга
# url = 'http://parsinger.ru/html/index3_page_3.html'
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
# # Ищем блок пагинации (элемент <div> с классом 'pagen') на странице,
# # затем извлекаем (элементы <a>) и из него все вложенные ссылки
# pagen = [link['href'] for link in soup.find('div', class_='pagen').find_all('a')]
#
# # Инициализируем список для хранения абсолютных URL-адресов
# list_link = []
#
# # Задаем схему URL-адреса, которая будет использоваться для преобразования относительных путей в абсолютные URL
# schema = 'https://parsinger.ru/html/'
#
# # Цикл по всем найденным ссылкам для преобразования их в абсолютные URL-адреса
# for link in pagen:
#     list_link.append(f"{schema}{link}")
#
#
# all_name = [] # тут все массивы страниц с наименованиями
# for li in list_link:
#     response = requests.get(url = li)
#     response.encoding = 'utf-8'
#     soup = BeautifulSoup(response.text, 'lxml')
#     tags = soup.findAll('a', class_='name_item')
#     this_name = [] #тут одна  страница с наименованиями
#     for tag in tags:
#             str1 = str(tag.text)
#             this_name.append(str1)
#     all_name.append(this_name)
# print(all_name)

# __________________________________________
# Задача:Посетить указанный веб-сайт, пройти по всем страницам в категории "мыши" и из каждой карточки товара извлечь артикул.
# После чего все извлеченные артикулы необходимо сложить и представить в виде одного числа.

# Задаем URL-адрес веб-страницы для парсинга
url = 'https://parsinger.ru/html/index3_page_4.html'

# Отправляем GET-запрос к указанной странице
response = requests.get(url=url)

# Устанавливаем кодировку ответа сервера в UTF-8 для корректного отображения текста на кириллице
response.encoding = 'utf-8'

# Преобразуем текст ответа сервера в объект BeautifulSoup с использованием парсера 'lxml'
soup = BeautifulSoup(response.text, 'lxml')

# Ищем блок пагинации (элемент <div> с классом 'pagen') на странице,
# затем извлекаем (элементы <a>) и из него все вложенные ссылки
pagen = [link['href'] for link in soup.find('div', class_='pagen').find_all('a')]

# Инициализируем список для хранения абсолютных URL-адресов
list_link = []

# Задаем схему URL-адреса, которая будет использоваться для преобразования относительных путей к странице в абсолютные URL
schema = 'https://parsinger.ru/html/'

# Цикл по всем найденным ссылкам для преобразования их в абсолютные URL-адреса
for link in pagen:
    list_link.append(f"{schema}{link}")

# тут я нашел ссылки на все страницы

# ссылки на все мышки
list_link_on_mouses = []

for stranica in list_link:
    response = requests.get(url=stranica)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    # ищем все div+классы с необходимыми ссылками
    pagen1 = soup.findAll('div', class_='sale_button')
    for link_mouse in pagen1:
        # получаем все ссылки и пишем в массив
        list_link_on_mouses.append(link_mouse.find('a')['href'])

# ссылка на каждую мышку
list_link_single_mouse = []
for link_single_mouse in list_link_on_mouses:
    list_link_single_mouse.append(f"{schema}{link_single_mouse}")

sum = 0
for link_single in list_link_single_mouse:
    url = link_single
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    e = str(soup.find('p', class_='article').text).replace('Артикул: ', "")
    ee = int(e)
    sum += ee
print(sum)
