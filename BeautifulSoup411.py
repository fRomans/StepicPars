import requests


# ____________________________________________________________________________________________________________________
# Задача: вытащить userId и title из json
# url = 'https://jsonplaceholder.typicode.com/posts'
#
# response = requests.get(url=url).json()
# for item in response:
#     print(item["userId"], item["title"])


# ____________________________________________________________________________________________________________________
# Задача: вытащить вложенный json

# url = 'http://parsinger.ru/downloads/get_json/res.json'
#
# response = requests.get(url=url).json()
# for item in response:
#     print(item["description"]["brand"], item["description"]["model"])

# ____________________________________________________________________________________________________________________
# Задача: На выходе вашей программы должен быть словарь в одну строку в формате Python:
#
# {'watch': N, 'mobile': N, 'mouse': N, 'hdd': N, 'headphones': N}
# где N — это общее количество товаров для каждой категории.

# url = 'https://parsinger.ru/downloads/get_json/res.json'
#
# response = requests.get(url=url).json()
# watchCount = 0
# mobileCount = 0
# mouseCount = 0
# hddCount = 0
# headphonesCount = 0
# dict={}
# for item in response:
#     # print(item["categories"], item["count"])
#     if(item["categories"]== "watch" ):
#         watchCount += int(item["count"])
#     elif(item["categories"]== "mobile" ):
#         mobileCount += int(item["count"])
#     elif(item["categories"]== "mouse" ):
#         mouseCount += int(item["count"])
#     elif(item["categories"]== "hdd" ):
#         hddCount += int(item["count"])
#     elif(item["categories"]== "headphones" ):
#         headphonesCount += int(item["count"])
#
# dict["watch"] = watchCount
# dict["mobile"] = mobileCount
# dict["mouse"] = mouseCount
# dict["hdd"] = hddCount
# dict["headphones"] = headphonesCount
# print(dict)

# ____________________________________________________________________________________________________________________
# Задача:Сделать GET-запрос и получить JSON-структуру по указанной ссылке.
# Для каждой категории товаров ('watch', 'mobile', 'mouse', 'hdd', 'headphones') рассчитать общую стоимость( Умножить стоимость товара на количество товара для каждой отдельной карточки).
# Суммируйте значения для каждой отдельной категории.
# Сформируйте словарь, где ключи - названия категорий, а значения - словаря с общей стоимостью товаров в этой категории.

# url = 'https://parsinger.ru/downloads/get_json/res.json'
#
# response = requests.get(url=url).json()
# watchPrice = 0
# mobilePrice = 0
# mousePrice = 0
# hddPrice = 0
# headphonesPrice = 0
#
# dict={}
# for item in response:
#     # print(item["categories"], item["count"])
#     if(item["categories"]== "watch" ):
#         price = int(str(item["price"]).replace(" руб", ""))
#         count= int(item["count"])
#         watchPrice += price*count
#     elif(item["categories"]== "mobile" ):
#         price = int(str(item["price"]).replace(" руб", ""))
#         count= int(item["count"])
#         mobilePrice += price*count
#     elif(item["categories"]== "mouse" ):
#         price = int(str(item["price"]).replace(" руб", ""))
#         count= int(item["count"])
#         mousePrice += price*count
#     elif(item["categories"]== "hdd" ):
#         price = int(str(item["price"]).replace(" руб", ""))
#         count= int(item["count"])
#         hddPrice += price*count
#     elif(item["categories"]== "headphones" ):
#         price = int(str(item["price"]).replace(" руб", ""))
#         count= int(item["count"])
#         headphonesPrice += price*count
#
# dict["watch"] = watchPrice
# dict["mobile"] = mobilePrice
# dict["mouse"] = mousePrice
# dict["hdd"] = hddPrice
# dict["headphones"] = headphonesPrice
# print(dict)

# ____________________________________________________________________________________________________________________
# Задача:Получение данных: Используйте инструменты разработчика для определения источника данных(вкладка Network).
# В нашем случае, данные лежат на этом веб-сайте.
# Обработка данных: Извлеките данные со страницы и создайте словарь, в котором для каждой карточки вычислите произведение
# значений "article" и "rating".
# Сбор значений: Суммируйте результаты произведений для каждой категории.
# Формирование словаря: Завершая задачу, создайте словарь, в котором ключами будут категории, а значениями - суммы произведений
# "article" и "rating".

url = 'https://parsinger.ru/4.6/1/res.json'

response = requests.get(url=url).json()


watchPr = 0
mobilePr = 0
mousePr = 0
hddPr = 0
headphonesPr = 0

dict={}
for item in response:

    if(item["categories"]== "watch" ):
        article = int(item["article"])
        rating= int(item["description"]["rating"])
        watchPr += article * rating
    elif(item["categories"]== "mobile" ):
        article = int(item["article"])
        rating= int(item["description"]["rating"])
        mobilePr += article * rating
    elif(item["categories"]== "mouse" ):
        article = int(item["article"])
        rating= int(item["description"]["rating"])
        mousePr += article * rating
    elif(item["categories"]== "hdd" ):
        article = int(item["article"])
        rating= int(item["description"]["rating"])
        hddPr += article * rating
    elif(item["categories"]== "headphones" ):
        article = int(item["article"])
        rating= int(item["description"]["rating"])
        headphonesPr += article * rating

dict["watch"] = watchPr
dict["mobile"] = mobilePr
dict["mouse"] = mousePr
dict["hdd"] = hddPr
dict["headphones"] = headphonesPr
print(dict)
