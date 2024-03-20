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
# Задача: