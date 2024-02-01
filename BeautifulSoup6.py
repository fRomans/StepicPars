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


# Задаем URL-адрес веб-страницы для парсинга
url = 'http://parsinger.ru/html/index1_page_3.html'

# Отправляем GET-запрос к указанной странице
response = requests.get(url=url)

# Устанавливаем кодировку ответа сервера в UTF-8 для корректного отображения текста на кириллице
response.encoding = 'utf-8'

# Преобразуем текст ответа сервера в объект BeautifulSoup с использованием парсера 'lxml'
soup = BeautifulSoup(response.text, 'lxml')

# Ищем блок пагинации (элемент <div> с классом 'pagen') на странице,
# затем извлекаем из него все вложенные ссылки (элементы <a>)
pagen = soup.find('div', class_='pagen').find_all('a')



pagen = [link['href'] for link in soup.find('div', class_='pagen').find_all('a')]

# Выводим на экран список найденных ссылок
print(pagen)

# Инициализируем список для хранения абсолютных URL-адресов
list_link = []

# Задаем схему URL-адреса, которая будет использоваться для преобразования относительных путей в абсолютные URL
schema = 'http://parsinger.ru/html/'

# Цикл по всем найденным ссылкам для преобразования их в абсолютные URL-адреса
for link in pagen:
    list_link.append(f"{schema}{link}")

# Выводим на экран список абсолютных URL-адресов
print(list_link)
