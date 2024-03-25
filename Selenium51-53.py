import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from seleniumwire import webdriver



# ____________________________________________________________________________________________________________________
# Задача: показать страницу при помощи webdriver
# with webdriver.Chrome() as driver:
#     driver.get("https://stepik.org/a/104774")
#     time.sleep(.5)
#     title = driver.title
#     print(title)

    # ____________________________________________________________________________________________________________________
# Задача: воспользоваться упакованным расширением(те сначала надо упаковать расширение)


# options_chrome = webdriver.ChromeOptions()
# options_chrome.add_extension('coordinates.crx')
#
# with webdriver.Chrome(options=options_chrome) as browser:
#     url = 'https://stepik.org/course/104774'
#     browser.get(url)
#     time.sleep(15)

    # ____________________________________________________________________________________________________________________
# Задача: запустить браузер в скрытом режиме с использованием Selenium

# Создание объекта ChromeOptions для дополнительных настроек браузера
# options_chrome = webdriver.ChromeOptions()

# Добавление аргумента '--headless' для запуска браузера в фоновом режиме
# options_chrome.add_argument('--headless')

# Инициализация драйвера Chrome с указанными опциями
# Использование менеджера контекста 'with' для автоматического закрытия браузера после выполнения кода
# with в Python предназначен для облегчения работы с ресурсами, которые требуют корректного освобождения после использования.
# with webdriver.Chrome(options=options_chrome) as browser:
#     url = 'https://stepik.org/a/104774'
#     browser.get(url)
#
#     # Ищем элемент по тегу 'a' (ссылку)
#     a = browser.find_element(By.TAG_NAME, 'a')
#
#     # Выводим атрибут 'href' найденного элемента (URL ссылки)
#     print(a.get_attribute('href'))

    # ____________________________________________________________________________________________________________________
# Задача: Запуск браузера в скрытом (или "headless") режиме с расширением

# options_chrome = webdriver.ChromeOptions()
# options_chrome.add_argument('--headless')
# options_chrome.add_extension('coordinates.crx')
#
#
#
#
# with webdriver.Chrome(options=options_chrome) as browser:
#     url = 'https://yandex.ru/'
#     browser.get(url)
#     time.sleep(5)
#     a = browser.find_element(By.TAG_NAME, 'a')
#     print(a.get_attribute('href'))

# ____________________________________________________________________________________________________________________
# Задача:перенести все настройки, закладки, историю с основного браузера, в браузер под управлением Selenium.Определяем
# путь к папке с профилями \User Data\, для этого напишите команду, в адресной строке браузера chrome://version/  и ищите адрес в поле с заголовком "Путь к профилю:" У меня адрес выглядит вот так: C:\Users\user\AppData\Local\Google\Chrome\User Data\
# 'user-data-dir=C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\User Data' добавьте путь к профилю в метод
# .add_argument()

# options_chrome = webdriver.ChromeOptions()
# options_chrome.add_argument('user-data-dir=C:\\Users\\fRomanSt\\AppData\\Local\\Google\\Chrome\\User Data')
# with webdriver.Chrome(options=options_chrome) as browser:
#     url = 'https://yandex.ru/'
#     browser.get(url)
#     time.sleep(10)

# ____________________________________________________________________________________________________________________
# Задача: узнать свой IP на сайте 2ip.ru.  модифицируем данный код, чтобы запрос отправлялся через прокси.

# узнаем ip
# url = 'https://2ip.ru/'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     time.sleep(5)
#     print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
#     time.sleep(5)

# отправлялся через прокси

# Если этот прокси еще живой, можете запустить этот код у себя в IDE. Если прокси умер, то приобретите надёжный прокси
# , и запустите код с ним.
# proxy = '8.210.83.33:80'
#
# url = 'https://2ip.ru/'
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server=%s' % proxy)
#
# with webdriver.Chrome(options=chrome_options) as browser:
#     browser.get(url)
#     print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
#     time.sleep(5)

    # ____________________________________________ИЛИ__________________________________________

# proxy_list = ['8.210.83.33:80', '199.60.103.28:80',
#               '103.151.246.38:10001', '199.60.103.228:80',
#               '199.60.103.228:80', '199.60.103.28:80', ]
#
# for PROXY in proxy_list:
#     try:
#         chrome_options = webdriver.ChromeOptions()
#         chrome_options.add_argument('--proxy-server=%s' % PROXY)
#         url = 'https://2ip.ru/'
#
#         with webdriver.Chrome(options=chrome_options) as browser:
#             browser.get(url)
#             print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
#
#             browser.set_page_load_timeout(5)
#
#             proxy_list.remove(PROXY)
#     except Exception as _ex:
#         print(f"Превышен timeout ожидания для - {PROXY}")
#         continue

        # ___________________________Proxy с авторизацией__________________________
        # Установка
        #
        # pip install selenium-wire
        #
        #
        # Импорт
        #
        # from seleniumwire import webdriver

# options = {'proxy': {
#     'http': "socks5://D2Frs6:75JjrW@194.28.210.39:9867",
#     'https': "socks5://D2Frs6:75JjrW@194.28.210.39:9867",
# }}
#
# url = 'https://2ip.ru/'
#
# with webdriver.Chrome(seleniumwire_options=options) as browser:
#     browser.get(url)
#     print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
#     time.sleep(5)