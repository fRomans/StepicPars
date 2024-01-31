import json

import requests

# 1. Получение и вывод HTML-кода веб-страницы
# url = "https://parsinger.ru/3.4/2/index.html"
#
# response = requests.get(url)
# response.encoding = 'utf-8'
# print(response.text)

# ________________________________________

# 2. Цель данного задания — научиться работе с сетевыми запросами для скачивания файлов.
# url = "https://parsinger.ru/img_download/img/ready/"
#
# i = 1
#
# while i <= 160:
#     response = requests.get(url + str(i) + ".png")
#     with open('R://AProgr/Python/parsPictures/' + str(i) + ".png", 'wb') as file:
#      file.write(response.content)
#     i = i + 1
# ________________________________________

# 3.Целью задания является закрепление навыков работы с методом response.json()

# url = "https://parsinger.ru/3.4/1/json_weather.json"
# response = requests.get(url)
# slovar = {}
# temp = 0
# data = " "
#                      i -- это key
# for i in response.json():
#     slovar = i
#     d = str(slovar["Температура воздуха"]).rstrip('°C')
#     s: int = int(d)
#     if s < temp:
#             temp = s
#             data = slovar["Дата"]
#
# print(temp)
# print(data)

# ________________________________________

# 4.Пройдитесь по древовидной структуре переписки.
# Подсчитайте, сколько сообщений отправил каждый участник.
# Участника необходимо определить по полю "username", поле  "user_id" не имеет отношения к решению данной задачи.

url = "https://parsinger.ru/3.4/3/dialog.json"
response = requests.get(url)
data = response.json()
list = [data]

def get_posts(lst):  # в функцию поступает список со словарями
    answer = {}  # это словарь-счетчик юзеров и постов
    for dct in lst:  # далее прохожу по каждому словарю в списке (lst - это dct['comments'])
        # print(answer.get(dct['username'], 0))
        answer[dct['username']] = answer.get(dct['username'], 0) + 1  # добавляю юзера в мой словарь
        if not dct['comments']:  # если это крайний случай - ничего не делаю
            continue
        else:  # если не крайний, то ищу дальше, пока не нащупаю дно :)

            for key, value in get_posts(dct['comments']).items():
                # print(key)
                # print(value)
                answer[key] = answer.get(key, 0) + value
    return answer


a = get_posts(list)
#пытался через reverse сортировку сделать, но не выходило.Очень элегантный метод сделать при сортировке
# все числа отрицательными
sorted_a = sorted(a.items(), key=lambda item: (-item[-1], item[0]))
print(dict(sorted_a))
