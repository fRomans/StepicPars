import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# ____________________________________________________________________________________________________________________
# Задача: поиском элемента и клика по нему.
# browser = webdriver.Chrome()
# browser.get('http://parsinger.ru/html/watch/1/1_1.html')
# button = browser.find_element(By.ID, "sale_button").click()
#
# time.sleep(10)

# ____________________________________________________________________________________________________________________
# Задача: завершить работу браузера с помощью driver.quit()

# driver= webdriver.Chrome()
# driver.get('http://parsinger.ru/html/watch/1/1_1.html')
# button = driver.find_element(By.ID, "sale_button")
# time.sleep(2)
# button.click()
# time.sleep(2)
# driver.quit()

# ____________________________________________________________________________________________________________________
# Задача: завершить работу браузера с помощью try/finally

# try:
#     driver= webdriver.Chrome()
#     driver.get('http://parsinger.ru/html/watch/1/1_1.html')
#     button = driver.find_element(By.ID, "sale_button")
#     time.sleep(2)
#     button.click()
#     time.sleep(2)
# finally:
#     driver.quit()


# ____________________________________________________________________________________________________________________
# Задача: завершить работу браузера с помощью менеджера контекста with/as. С этим способом нам вообще не нужно думать о том,
# когда закрывать браузер, менеджер контекста делает это за нас в тот момент, когда это нужно.

# with webdriver.Chrome() as driver:
#     driver.get('http://parsinger.ru/html/watch/1/1_1.html')
#     button = driver.find_element(By.ID, "sale_button")
#     time.sleep(2)
#     button.click()
#     time.sleep(2)

# ____________________________________________________________________________________________________________________
# Задача:найти 1 и 3 элементы p в div

# url = 'http://parsinger.ru/selenium/3/3.html'
# # Инициализация драйвера в контексте with, чтобы он закрылся после завершения работы
# with webdriver.Chrome() as browser:
#     # Открываем URL
#     browser.get(url)
#
#     # Ищем все div с классом 'text'
#     divs = browser.find_elements(By.CLASS_NAME, 'text')
#
#     # Проходимся по каждому div
#     for i, div in enumerate(divs):
#         # Получаем первый и третий теги <p> внутри каждого div.
#         # ./ — указывает на текущий элемент, в контексте которого
#         # происходит поиск. В данном случае, текущим элементом является каждый отдельный <div> с классом text.
#         first_p = div.find_element(By.XPATH, './p[1]')
#         third_p = div.find_element(By.XPATH, './p[3]')
#
#         # Выводим их текст
#         print(f"Для div #{i+1}, первый p: {first_p.text}, третий p: {third_p.text}")

# ____________________________________________________________________________________________________________________
# Задача:вскрыть виртуальный сейф, заполнить поля аутентификации и взять "ключ", который появляется на экране. И конечно же,
# это нужно сделать всё в течение трёх секунд.
# Основные Этапы:
# Точка Входа: Откройте заданный веб-сайт с помощью Selenium.
# Сканирование: Используйте метод .find_elements() для поиска всех доступных полей для ввода на странице.
# Ввод данных: В цикле, переберите все найденные поля и заполните их с помощью метода .send_keys("Текст").
# Инициация: Найдите кнопку на странице и нажмите на неё.
# Результат: Скопируйте текст, который появится на экране рядом с кнопкой, если вы уложились в трёхсекундный интервал.
# Фиксация: Запишите результат в отдельную переменную

# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/1/1.html')
#     # By.XPATH, "//div[@class='form_box']/input[1]"
#     browser.find_element(By.NAME, "first_name").send_keys("Hello, World!")
#     browser.find_element(By.NAME, "last_name").send_keys("Hello, World!")
#     browser.find_element(By.NAME, "patronymic").send_keys("Hello, World!")
#     browser.find_element(By.NAME, "age").send_keys("Hello, World!")
#     browser.find_element(By.NAME, "city").send_keys("Hello, World!")
#     browser.find_element(By.NAME, "email").send_keys("Hello, World!")
#     browser.find_element(By.ID, "btn").click()
#     time.sleep(5)


# ____________________________________________________________________________________________________________________
# Задача: Поиск Ссылки: Используйте метод By.PARTIAL_LINK_TEXT или By.LINK_TEXT для поиска ссылки с текстом 16243162441624.
# Клик по Ссылке: Нажмите на найденную ссылку.
# Получение Результата: Скопируйте текст, который появится в теге найденной страницы <p id="result"></p>.


# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/selenium/2/2.html')
#     element = browser.find_element(By.LINK_TEXT, "16243162441624")
#     print(element.click())
#     time.sleep(100)


#               By.LINK_TEXT – Поиск элемента по точному тексту ссылки. Очень удобно, если текст уникален.
# element = driver.find_element(By.LINK_TEXT, "Continue")
#               By.PARTIAL_LINK_TEXT – Поиск элемента по частичному тексту ссылки. Удобно, когда точный текст ссылки неизвестен
#               или динамичен.
#  element = driver.find_element(By.PARTIAL_LINK_TEXT, "Cont")


# ____________________________________________________________________________________________________________________
# Задача: Извлеките данные из каждого тега <p> на странице.Просуммируйте все числовые значения, которые вы извлекли.

# # URL веб-страницы для парсинга
# url = 'http://parsinger.ru/selenium/3/3.html'
#
# # Инициализируем драйвер Chrome
# with webdriver.Chrome() as browser:
#     # Открываем веб-страницу по заданному URL
#     browser.get(url)
#
#     # Используем метод .find_elements() для поиска всех элементов, соответствующих нашему XPath
#     elements1 = browser.find_elements(By.XPATH, "//div[@class='text']/p[1]")
#     elements2 = browser.find_elements(By.XPATH, "//div[@class='text']/p[2]")
#     elements3 = browser.find_elements(By.XPATH, "//div[@class='text']/p[3]")
#
#     # объединение list
#     joined = elements1 + elements2 + elements3
#
#     sum = 0
#
#     # Проходимся по списку найденных элементов и выводим их текст
#     for i, element in enumerate(joined):
#         sum = sum + int(str(element.text))
# print(sum)


# ____________________________________________________________________________________________________________________
# Задача: Найдите и извлеките данные из каждого второго тега <p> на странице.Просуммируйте все числовые значения,
# полученные из этих тегов.Скопируйте число, которое появится в теге <p id="result">Result</p>.

# url = 'http://parsinger.ru/selenium/3/3.html'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#
#     elements2 = browser.find_elements(By.XPATH, "//div[@class='text']/p[2]")
#
#     sum = 0
#
#     for i, element in enumerate(elements2):
#         sum = sum + int(str(element.text))
# print(sum)

# ____________________________________________________________________________________________________________________
# Задача:Найдите все чек-боксы на странице и установите их в положение checked с помощью .click().
# Как только все чек-боксы будут активированы, нажмите на кнопку.Скопируйте число, которое появится в теге <p id="result">Result</p>.


# with webdriver.Chrome() as browser:
#
#     browser.get('https://parsinger.ru/selenium/4/4.html')
#
#     elements = browser.find_elements(By.CLASS_NAME, "check")
#     btn = browser.find_element(By.CLASS_NAME, "btn")
#     res = browser.find_element(By.ID, "result")
#
#     for i, element in enumerate(elements):
#
#           element.click()
#           btn.click()
#           print(res.text)

# ____________________________________________________________________________________________________________________
# Задача:С помощью Selenium и метода click() установите в положение checked только те чек-боксы, значение атрибута value которых
# есть в заданном списке numbers.Как только все нужные чек-боксы активны, кнопка станет активной. Нажмите на неё.
# После нажатия на кнопку, результат появится в теге <p id="result">Result</p>.


# with webdriver.Chrome() as browser:
#
#     browser.get('https://parsinger.ru/selenium/5/5.html')
#
#     elements = browser.find_elements(By.CLASS_NAME, "check")
#     btn = browser.find_element(By.CLASS_NAME, "btn")
#     res = browser.find_element(By.ID, "result")
#     numbers = [1, 2, 3, 4, 8, 9, 11, 12, 13, 14, 15, 16, 17, 22, 23, 28, 29, 33, 34, 38,
#                39, 43, 44, 48, 49, 51, 52, 53, 54, 55, 56, 57, 58, 61, 62, 63, 64, 68, 69, 73,
#                74, 78, 79, 83, 84, 88, 89, 91, 92, 97, 98, 101, 104, 108, 109, 113, 114, 118,
#                119, 123, 124, 128, 129, 131, 132, 137, 138, 140, 141, 144, 145, 148, 149, 153,
#                154, 158, 159, 163, 164, 165, 168, 169, 171, 172, 177, 178, 180, 181, 184, 185,
#                187, 188, 189, 190, 192, 193, 194, 195, 197, 198, 199, 200, 204, 205, 206, 207,
#                208, 209, 211, 212, 217, 218, 220, 221, 224, 225, 227, 228, 229, 230, 232, 233,
#                234, 235, 237, 238, 239, 240, 245, 246, 247, 248, 249, 251, 252, 253, 254, 255,
#                256, 257, 258, 260, 261, 264, 265, 268, 269, 273, 274, 278, 279, 288, 289, 291,
#                292, 293, 294, 295, 296, 297, 300, 301, 302, 303, 304, 305, 308, 309, 313, 314,
#                318, 319, 328, 329, 331, 332, 339, 340, 341, 342, 343, 344, 345, 346, 348, 349,
#                353, 354, 358, 359, 368, 369, 371, 372, 379, 380, 385, 386, 408, 409, 411, 412,
#                419, 420, 425, 426, 428, 429, 433, 434, 438, 439, 444, 445, 446, 447, 448, 451,
#                452, 459, 460, 465, 466, 467, 468, 469, 470, 472, 473, 474, 475, 477, 478, 479,
#                480, 485, 486, 487, 488, 491, 492, 499, 500, 505, 506, 508, 509, 513, 514, 518, 519]
#
#     for i, element in enumerate(elements):
#             val = int(element.get_attribute('value'))
#             for num in numbers:
#                 if val == num:
#                     element.click()
#     btn.click()
#     print(res.text)


    # ____________________________________________________________________________________________________________________
# Задача: Получите значения всех элементов выпадающего списка.Сложите (плюсуйте) все извлеченные значения.
# Вставьте получившийся результат в поле на сайте и нажмите кнопку.

with webdriver.Chrome() as browser:

    browser.get('https://parsinger.ru/selenium/7/7.html')

    elements2 = browser.find_elements(By.XPATH, "//select[@id='opt']/option")
    pole = browser.find_element(By.ID, "input_result")
    btn = browser.find_element(By.CLASS_NAME, "btn")
    res = browser.find_element(By.ID, "result")

    sum = 0
    for i, element in enumerate(elements2):
            chis = int(element.text)
            sum += chis

    pole.send_keys(sum)
    btn.click()
    print(res.text)












