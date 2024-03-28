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

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/1/1.html')
    els = browser.find_elements(By.CLASS_NAME, 'form')
    # print(els)

    for el in els:
        # Получаем первый и третий теги <p> внутри каждого div
        first_p = el.send_keys("ирина турик")
            # .send_keys('Text')
        time.sleep(5)
        print(el)