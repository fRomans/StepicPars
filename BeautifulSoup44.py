from bs4 import BeautifulSoup
import requests
import lxml

# Пример 1. Передача файла HTML напрямую без использования менеджера контекста
# file = open('R:\AProgr\Python\index.html', encoding='utf-8')
# soup = BeautifulSoup(file, 'lxml')
# file.close()
# print("Анализ файла без использования менеджера контекста:\n", soup)

# Пример 2. Передача файла HTML с использованием менеджера контекста
# with open('R:\AProgr\Python/index.html', 'r', encoding='utf-8') as file:
#     soup2 = BeautifulSoup(file, 'lxml')
#     print("Анализ файла с использованием менеджера контекста:\n", soup2)

# Пример 3. Передача объекта response прямо из запроса
# response = requests.get(url='http://parsinger.ru/html/watch/1/1_1.html')
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')

# __________________________________________
# Задача 4.3
# with open('R:\AProgr\Python/index.html', 'r', encoding='utf-8') as file:
#     soup2 = BeautifulSoup(file, 'lxml')
# print(soup2)

# __________________________________________
# Задача : Написать код, который будет обрабатывать предоставленную HTML-структуру, представляющую собой карточку товара.
# Код должен находить тег <p> с классом card-description и извлекать из него текстовое описание товара.

# html_doc = """
# <!DOCTYPE html>
# <html lang="ru">
# <head>
#     <meta charset="UTF-8">
#     <title>Пример карточки товара</title>
# </head>
# <body>
#     <div class="card">
#         <img src="image.jpg" alt="Пример изображения товара">
#         <h2 class="card-title"> iPhone 15 </h2>
#         <p class="card-description">Аппаратной основой Apple iPhone 15 Pro Max стал 3-нанометровый чипсет A17 Pro с 6-ядерным GPU и поддержкой трассировки лучей.</p>
#         <p class="card-price">999 999 руб.</p>
#         <a href="https://example.com/product-link" class="card-link">Подробнее</a>
#     </div>
# </body>
# </html>
# """
# soup = BeautifulSoup(html_doc, 'html.parser')
#
# tag = soup.p

# print(type(tag))   # <class 'bs4.element.Tag'>
# print(tag.name)    # div
# print(tag.attrs)   # {'class': ['myclass']}
# print(tag.string)  # Hello, world!

# __________________________________________
# Задача : Написать код, который будет обрабатывать HTML-структуру, содержащую карточки товаров.
# Код должен находить все теги с классом card-articul, извлекать из них числовые значения артикулов и
# суммировать их.

# html_doc = """
# <!DOCTYPE html>
# <html lang="ru">
# <head>
#     <meta charset="UTF-8">
# </head>
# <body>
#     <div class="cards">
#         <!-- Карточка товара 1 -->
#         <div class="card">
#             <img src="parsing.png" alt="WEB Парсинг на Python">
#             <h2 class="card-title">WEB Парсинг на Python</h2>
#             <p class="card-articul">Артикул: 104774</p>
#             <p class="card-stock">Наличие: 5 шт.</p>
#             <p class="card-price">3500 руб.</p>
#             <a href="https://stepik.org/a/104774" class="card-button">Купить</a>
#         </div>
#         <!-- Карточка товара 2 -->
#         <div class="card">
#             <img src="async.png" alt="Асинхронный Python">
#             <h2 class="card-title">Асинхронный Python</h2>
#             <p class="card-articul">Артикул: 170777</p>
#             <p class="card-stock">Наличие: 10 шт.</p>
#             <p class="card-price">3500 руб.</p>
#             <a href="https://stepik.org/a/170777" class="card-button">Купить</a>
#         </div>
#         <!-- Карточка товара 3 -->
#         <div class="card">
#             <img src="selenium.PNG" alt="Selenium Python">
#             <h2 class="card-title">Selenium Python</h2>
#             <p class="card-articul">Артикул: 119495</p>
#             <p class="card-stock">Наличие: 5 шт.</p>
#             <p class="card-price">1250 руб.</p>
#             <a href="https://stepik.org/a/119495" class="card-button">Купить</a>
#         </div>
#     </div>
# </body>
# </html>
# """
# Инициализация объекта BeautifulSoup
# soup = BeautifulSoup(html_doc, 'html.parser')

# Поиск всех элементов с классом 'card-articul'
# articuls = soup.findAll('p', class_='card-articul')

# Извлечение числовых значений артикулов и их суммирование
# sum_articuls = 0
# for tag1 in articuls:
#     str1 = str(tag1.text)
#     gg = str1.replace('Артикул: ','')
#     sum_articuls = sum_articuls+int(gg)
#
# print(f"Сумма артикулов: {sum_articuls}")  # Вывод результата

# __________________________________________
# Задача : Написать код, который будет обрабатывать HTML-структуру, состоящую из различных тегов,
# включая теги <img>. Код должен находить все теги <img> и суммировать значения их атрибута alt.

# html_doc = """
# <!DOCTYPE html>
# <html lang="ru">
# <head>
#     <meta charset="UTF-8">
# </head>
# <body>
#
# <div class="card">
#     <h2>Товар 1</h2>
#     <img src="parsing.png" alt="779966">
#     <p>Цена: 1000 руб.</p>
#     <p>Описание: Отличный товар, изготовлен из качественных материалов.</p>
#     <p>Технические характеристики: Размеры: 10x10x10 см, Вес: 1 кг.</p>
#     <p>Доступные размеры: S, M, L</p>
#     <p>Отзывы: 5 звезд</p>
#     <p>Наличие на складе: В наличии</p>
#     <p>Информация о доставке: Бесплатно при заказе от 3000 руб.</p>
#     <a href="https://stepik.org/a/104774" class="btn">Купить</a>
# </div>
#
# <div class="card">
#     <h2>Товар 2</h2>
#     <img src="async.png" alt="331155">
#     <p>Цена: 1500 руб.</p>
#     <p>Описание: Превосходный товар, подходит для повседневного использования.</p>
#     <p>Технические характеристики: Размеры: 15x15x15 см, Вес: 1.5 кг.</p>
#     <p>Доступные размеры: M, L, XL</p>
#     <p>Отзывы: 4.5 звезд</p>
#     <p>Наличие на складе: В наличии</p>
#     <p>Информация о доставке: Бесплатно при заказе от 5000 руб.</p>
#     <a href="https://stepik.org/a/170777" class="btn">Купить</a>
# </div>
#
# <div class="card">
#     <h2>Товар 3</h2>
#     <img src="parsing.png" alt="558877">
#     <p>Цена: 2000 руб.</p>
#     <p>Описание: Удобный товар для дома и офиса.</p>
#     <p>Технические характеристики: Размеры: 12x12x12 см, Вес: 1.2 кг.</p>
#     <p>Доступные размеры: S, M</p>
#     <p>Отзывы: 4.7 звезд</p>
#     <p>Наличие на складе: В наличии</p>
#     <p>Информация о доставке: Бесплатно при заказе от 3500 руб.</p>
#     <a href="https://stepik.org/a/104774" class="btn">Купить</a>
# </div>
#
# <div class="card">
#     <h2>Товар 4</h2>
#     <img src="async.png" alt="449933">
#     <p>Цена: 2500 руб.</p>
#     <p>Описание: Стильный и практичный товар.</p>
#     <p>Технические характеристики: Размеры: 14x14x14 см, Вес: 1.4 кг.</p>
#     <p>Доступные размеры: L, XL</p>
#     <p>Отзывы: 4.8 звезд</p>
#     <p>Наличие на складе: В наличии</p>
#     <p>Информация о доставке: Бесплатно при заказе от 4000 руб.</p>
#     <a href="https://stepik.org/a/170777" class="btn">Купить</a>
# </div>
#
# <div class="card">
#     <h2>Товар 5</h2>
#     <img src="parsing.png" alt="667711">
#     <p>Цена: 2700 руб.</p>
#     <p>Описание: Идеальный товар для повседневного использования.</p>
#     <p>Технические характеристики: Размеры: 13x13x13 см, Вес: 1.3 кг.</p>
#     <p>Доступные размеры: M, L, XL</p>
#     <p>Отзывы: 4.9 звезд</p>
#     <p>Наличие на складе: В наличии</p>
#     <p>Информация о доставке: Бесплатно при заказе от 4500 руб.</p>
#     <a href="https://stepik.org/a/104774" class="btn">Купить</a>
# </div>
#
# <div class="card">
#     <h2>Товар 6</h2>
#     <img src="async.png" alt="334455">
#     <p>Цена: 3000 руб.</p>
#     <p>Описание: Прочный и надежный товар.</p>
#     <p>Технические характеристики: Размеры: 16x16x16 см, Вес: 1.6 кг.</p>
#     <p>Доступные размеры: S, M</p>
#     <p>Отзывы: 5 звезд</p>
#     <p>Наличие на складе: В наличии</p>
#     <p>Информация о доставке: Бесплатно при заказе от 5000 руб.</p>
#     <a href="https://stepik.org/a/170777" class="btn">Купить</a>
# </div>
#
#
# </body>
# </html>
# """


# Инициализация объекта BeautifulSoup
# soup = BeautifulSoup(html_doc, 'html.parser')
# total_sum = 0
# # Находим все теги img
# img_tags = soup.findAll('img')
# for x in img_tags:
#  total_sum = total_sum + int(x['alt'])
#
# print(f"Сумма всех значений в атрибуте alt тега img: {total_sum}")

# __________________________________________
# Задача : Написать код, который будет обрабатывать HTML-структуру, состоящую из тегов <p>.
# Код должен анализировать текст внутри каждого тега и, если количество символов в тексте (без учета пробелов)
# является чётным, суммировать значения атрибутов id и class.

# html = '''<!DOCTYPE html>
# <html lang="ru">
# <head>
#     <meta charset="UTF-8">
#     <title>Тестовая страница для веб-парсинга</title>
# </head>
# <body>
#     <p id="435456" class="123984">Веб-парсинг – это мощный инструмент для анализа данных в интернете.</p>
#     <p id="284359" class="493572">Python предоставляет отличные библиотеки для парсинга веб-страниц.</p>
#     <p id="789234" class="293487">Для начинающих веб-парсеров важно изучить основы HTML и CSS.</p>
#     <p id="239048" class="392874">Библиотека BeautifulSoup позволяет легко извлекать данные с веб-страниц.</p>
#     <p id="923874" class="120948">Scrapy – другой популярный фреймворк для веб-парсинга на Python.</p>
#     <p id="982374" class="302984">Веб-парсинг может помочь аналитикам и маркетологам собирать ценную информацию.</p>
#     <p id="238940" class="238492">Соблюдение законов и правил при парсинге веб-сайтов – это ключевой момент.</p>
#     <p id="923485" class="283947">Ограничения robots.txt могут влиять на возможность парсинга некоторых сайтов.</p>
#     <p id="293847" class="394872">Динамические веб-сайты могут требовать использование Selenium для парсинга.</p>
#     <p id="239487" class="238492">Регулярные выражения могут быть полезными при извлечении специфических данных.</p>
#     <p id="203984" class="394872">При веб-парсинге важно учитывать нагрузку на целевой веб-сайт.</p>
#     <p id="394872" class="203984">Кэширование данных может ускорить процесс парсинга и снизить нагрузку на сервер.</p>
#     <p id="238492" class="394872">Прокси-сервера могут помочь обойти ограничения, связанные с IP-адресом.</p>
#     <p id="239847" class="238947">Парсинг может быть автоматизирован с помощью планировщика задач.</p>
#     <p id="394872" class="238492">Обработка ошибок – важный этап в разработке парсера.</p>
#     <p id="238492" class="394872">Сохранение данных в базу данных позволяет легко анализировать и обрабатывать информацию.</p>
#     <p id="293847" class="203984">Многопоточность может значительно ускорить процесс парсинга веб-сайтов.</p>
#     <p id="394872" class="203984">Веб-парсинг – это не только технический процесс, но и аналитический навык.</p>
#     <p id="293847" class="394872">Изучение веб-парсинга открывает новые возможности для исследования интернета.</p>
#     <p id="238947" class="238492">Качественный парсер требует тщательной проработки и тестирования.</p>
#     <p id="384756" class="293487">Парсинг веб-страниц – это процесс извлечения данных с онлайн-ресурсов.</p>
#     <p id="238947" class="293487">Python стал популярным языком для веб-парсинга благодаря своей простоте и богатой экосистеме.</p>
#     <p id="384756" class="238492">Знание структуры HTML и CSS сделает вас более эффективным веб-парсером.</p>
#     <p id="238947" class="238492">BeautifulSoup предоставляет удобные методы для поиска и извлечения данных из HTML-документов.</p>
#     <p id="384756" class="293487">Scrapy облегчает парсинг множества страниц и управление запросами.</p>
#     <p id="238947" class="293487">Веб-парсинг помогает в анализе конкурентов и рынка для бизнеса.</p>
#     <p id="384756" class="238492">Соблюдение этичных и юридических норм важно при веб-парсинге.</p>
#     <p id="238947" class="238492">Файл robots.txt указывает правила доступа для веб-краулеров и парсеров.</p>
#     <p id="384756" class="293487">Selenium полезен для парсинга динамических веб-сайтов с JavaScript.</p>
#     <p id="238947" class="293487">Регулярные выражения могут быть мощным инструментом для извлечения данных из текста.</p>
#     <p id="384756" class="238492">Оптимизация запросов и паузы важны для избежания блокировки при парсинге.</p>
#     <p id="238947" class="238492">Кэширование данных улучшает производительность парсера и снижает нагрузку.</p>
#     <p id="384756" class="293487">Использование прокси-серверов помогает в обходе ограничений по IP-адресу.</p>
#     <p id="238947" class="293487">Автоматизация парсинга с помощью планировщика может сэкономить время.</p>
#     <p id="384756" class="238492">Обработка и логирование ошибок важны для стабильной работы парсера.</p>
#     <p id="238947" class="238492">Сохранение данных в базу данных обеспечивает их долгосрочное хранение и анализ.</p>
#     <p id="384756" class="293487">Многопоточность увеличивает скорость парсинга и снижает время выполнения задач.</p>
#     <p id="238947" class="293487">Веб-парсинг требует аналитического мышления и понимания данных.</p>
#     <p id="384756" class="238492">Изучение веб-парсинга расширяет возможности для исследования интернета и данных.</p>
#     <p id="238947" class="238492">Разработка качественного парсера – это процесс, требующий тщательной проработки и тестирования.</p>
#     <p id="384756" class="293487">Извлечение данных из веб-страницы – ключевой этап в анализе интернет-контента.</p>
#     <p id="238947" class="293487">Python предоставляет множество возможностей для работы с текстом и данными.</p>
#     <p id="384756" class="238492">Оптимизация запросов и управление скоростью парсинга – залог успешного сбора данных.</p>
#     <p id="238947" class="238492">Использование кэширования может значительно снизить нагрузку на серверы и ускорить работу парсера.</p>
#     <p id="384756" class="293487">Прокси-сервера – надежный способ обойти ограничения по IP и повысить анонимность.</p>
#     <p id="238947" class="293487">Автоматизация задач с помощью планировщика обеспечивает регулярное обновление данных.</p>
#     <p id="384756" class="238492">Обработка ошибок и их логирование помогают выявить проблемы и улучшить стабильность парсера.</p>
#     <p id="238947" class="238492">Сохранение данных в базе обеспечивает их сохранность и возможность дальнейшего анализа.</p>
#     <p id="384756" class="293487">Использование многопоточности позволяет параллельно обрабатывать множество страниц.</p>
#     <p id="238947" class="293487">Веб-парсинг – это искусство анализа и извлечения информации из виртуального мира.</p>
#     <p id="384756" class="238492">Изучение веб-парсинга даёт возможность исследовать интернет в поисках ценных данных.</p>
#     <p id="238947" class="238492">Разработка парсера – это непрерывный процесс улучшения и оптимизации.</p>
#     <p id="384756" class="293487">API предоставляют более удобный способ доступа к данным, чем парсинг страниц.</p>
#     <p id="238947" class="293487">XPath – мощный инструмент для навигации и извлечения данных из XML и HTML.</p>
#     <p id="384756" class="238492">Парсинг данных из JSON позволяет эффективно работать с данными в этом формате.</p>
#     <p id="238947" class="238492">Анализ времени выполнения запросов помогает оптимизировать парсинг и снизить нагрузку.</p>
#     <p id="384756" class="293487">Эффективный веб-парсинг требует понимания принципов работы HTTP-протокола.</p>
#     <p id="238947" class="293487">Системы управления версиями помогают отслеживать изменения в коде парсера.</p>
#     <p id="384756" class="238492">Интеграция с облачными хранилищами данных облегчает анализ собранных данных.</p>
#     <p id="238947" class="238492">Аналитика и визуализация данных помогают получить ценные инсайты из собранных информационных ресурсов.</p>
#     <p id="384756" class="293487">Понимание DOM-структуры помогает эффективно навигировать по веб-страницам.</p>
#     <p id="238947" class="293487">Python имеет богатую экосистему для анализа данных, что делает его отличным выбором для парсинга.</p>
#     <p id="384756" class="238492">Контроль частоты запросов позволяет избегать блокировок со стороны серверов.</p>
#     <p id="238947" class="238492">Использование регулярных выражений требует навыков и практики, но может быть мощным инструментом.</p>
#     <p id="384756" class="293487">Прокси-сервера могут быть необходимы для работы с сайтами, блокирующими IP-адреса.</p>
#     <p id="238947" class="293487">Планировщики задач помогают автоматизировать процесс парсинга по расписанию.</p>
#     <p id="384756" class="238492">Обработка ошибок включает в себя исключения и стратегии восстановления парсера.</p>
#     <p id="238947" class="238492">Сохранение данных в базе обеспечивает надежное хранение и возможность долгосрочного анализа.</p>
#     <p id="384756" class="293487">Использование многопоточности может значительно ускорить процесс сбора данных.</p>
#     <p id="238947" class="293487">Веб-парсинг помогает исследователям извлекать информацию из различных источников.</p>
#     <p id="384756" class="238492">Разработка парсера требует тщательного планирования и тестирования функциональности.</p>
#     <p id="238947" class="238492">Интеграция с RESTful API облегчает получение данных с веб-серверов.</p>
#     <p id="384756" class="293487">XPath позволяет точно находить и извлекать элементы на веб-странице.</p>
#     <p id="238947" class="293487">JSON является удобным форматом для передачи и хранения данных при парсинге.</p>
#     <p id="384756" class="238492">Мониторинг и управление ресурсами помогают избежать перегрузки серверов.</p>
#     <p id="238947" class="293487">Знание структуры URL важно для формирования правильных запросов.</p>
#     <p id="384756" class="293487">Веб-парсинг может использоваться для сравнения цен на товары и услуги.</p>
#     <p id="238947" class="238492">Эффективный парсер должен быть адаптирован к особенностям целевых веб-сайтов.</p>
#     <p id="384756" class="293487">Интеграция с базами данных позволяет хранить и анализировать большие объемы данных.</p>
#     <p id="238947" class="238492">Аналитика данных позволяет выявить тенденции и паттерны в собранных информационных ресурсах.</p>
# </body>
# </html>
# '''
#
#
# def sum_even_length_ids(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     total_id_sum = 0
#     total_class_sum = 0
#     p_tags = soup.findAll('p')
#
#     for x in p_tags:
#
#         str1 = str(x.text)
#         len = str1.replace(" ", "").__len__()
#         if len % 2 == 0:
#             str1 = str(x['class']).replace("['", "").replace("']", "")
#             total_class_sum = total_class_sum + int(str1)
#             total_id_sum = total_id_sum + int(x['id'])
#     return print(f"Сумма ID и CLASS тегов <p> с чётной длиной текста без пробелов: {total_id_sum + total_class_sum}")
#
#
# sum_even_length_ids(html)

# __________________________________________
# Задача : Ваша задача найти тег который имеет имя и значение атрибута data-gpu="nVidia GeForce RTX 4060".
# Извлеките текст из тега после его нахождения.

# html = '''
# <html>
# <head>
# <title>Каталог продуктов</title>
# <link rel="stylesheet" href="styles.css">
# <meta charset="UTF-8">
# </head>
# <body>
# <div class="item_card">
# <div class="item product_item" id="item_1">
# <div class="img_box product_img_box">
# <a href="product/1/1_details.html" name="1_img">
# <img src="images/Видеокарта GigaByte nVidia GeForce RTX 4060 EAGLE OC PCI-E 8192Mb GDDR6 128 Bit Retail GV-N4060EAGLE OC-8GD.jpg" alt="Видеокарта GigaByte nVidia GeForce RTX 4060 EAGLE OC PCI-E 8192Mb GDDR6 128 Bit Retail">
# </a>
# <a href="product/1/1_details.html" name="1_name" class="name_item product_name">
# Видеокарта GigaByte nVidia GeForce RTX 4060 EAGLE OC PCI-E 8192Mb GDDR6 128 Bit Retail GV-N4060EAGLE OC-8GD
# </a>
# <div class="description product_description">
# <li class="description_detail Ferrari Lamborghini Bugatti" data-brand="GigaByte" data-model="GV-N4060" data-series="Eagle">Бренд: GigaByte</li>
# <li class="description_detail AMD Intel Nvidia" data-card_type="gaming" data-api="DirectX 12" data-performance="high">Тип видеокарты: игровая</li>
# <li class="description_detail Sparrow Eagle Falcon" data-cpu_series="nVidia GeForce RTX" data-generation="30-series" data-architecture="Ampere">Серия процессора: nVidia GeForce RTX</li>
# <li class="description_detail Hawk Owl Raven" data-gpu="nVidia GeForce RTX 4060" data-cuda_cores="3584" data-boost_clock="1815MHz">Графический процессор: nVidia GeForce RTX 4060</li>
# <li class="description_detail SSD HDD RAM" data-memory="8192Mb" data-type="GDDR6" data-bandwidth="448GB/s">Объем видеопамяти: 8192Mb</li>
# <li class="description_detail Kingston Crucial Samsung" data-memory_type="GDDR6" data-speed="16Gbps" data-interface="256-bit">Тип видеопамяти: GDDR6</li>
# <li class="description_detail Airbus Boeing Cessna" data-bus_width="128 Bit" data-memory_bus="GDDR6" data-bandwidth_bus="256GB/s">Разрядность шины видеопамяти: 128 Bit</li>
# <li class="description_detail Tesla Rivian Lucid" data-connection_type="PCI-E" data-version="4.0" data-bandwidth_pci="16GT/s">Тип подключения: PCI-E</li>
# <li class="description_detail Asus MSI Gigabyte" data-interface_type="PCI-E 16x 4.0" data-slots="2" data-bandwidth_interface="32GB/s">Интерфейс подключения: PCI-E 16x 4.0</li>
# <li class="description_detail HDMI DisplayPort USB-C" data-hdmi="yes" data-version_hdmi="2.1" data-max_resolution="8K">Разъём HDMI: есть</li>
# <li class="description_detail DisplayPort HDMI DVI" data-displayport="yes" data-version_dp="1.4a" data-max_refresh="240Hz">Выход DisplayPort: есть</li>
# <li class="description_detail PowerConnector USB TypeC Ethernet" data-power_pins="8" data-connector_type="PCIe" data-voltage="12V">Разъёмы дополнительного питания видеокарты, pin: 8</li>
# </div>
#
# <div class="container product_container">
# <div class="price_box">
# <p class="price product_price">35 280 руб</p>
# </div>
# <div class="sale_button product_sale_button">
# <a href="product/1/1_details.html">
# <p>Подробнее</p>
# </a>
# </div>
# </div>
# </div>
# </div>
# </div>
#
#
# </body>
# </html>
# '''
#
# def get_html(html):
#     soup = BeautifulSoup(html, 'html.parser')
#
#     tag = soup.find(attrs={'data-gpu': 'nVidia GeForce RTX 4060'})
#
#     print(tag.text)
#
# get_html(html)

# __________________________________________
# Задача : Найдите тег <li> который имеет имя атрибута data-key и значение атрибута cooling_system.
# Извлеките текст из тега.

# html = '''
# <html><head>
#       <title>Каталог продуктов</title>
#       <link rel="stylesheet" href="styles.css">
#       <meta charset="UTF-8">
#    </head>
#    <body>
#       <div class="item_card">
#          <div class="item product_item" id="item_1">
#             <div class="img_box product_img_box">
#                <a href="product/1/1_details.html" name="1_img">
#                <img src="images/Видеокарта MSI Radeon RX 6650 XT MECH 2X OC PCI-E 8192Mb GDDR6 128 Bit Retail.jpg" alt="Видеокарта MSI Radeon RX 6650 XT MECH 2X OC PCI-E 8192Mb GDDR6 128 Bit Retail">
#                </a>
#                <a href="product/1/1_details.html" name="1_name" class="name_item product_name">
#                Видеокарта MSI Radeon RX 6650 XT MECH 2X OC PCI-E 8192Mb GDDR6 128 Bit Retail
#                </a>
#                <div class="description product_description">
#                   <li id="item_1_brand" data-key="brand" class="description_detail">Бренд: MSI</li>
#                   <li id="item_1_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_1_processor series" data-key="processor series" class="description_detail">Серия процессора: Radeon RX</li>
#                   <li id="item_1_graphic_processor" data-key="graphic_processor" class="description detailz">Графический процессор: Radeon RX 6650 XT</li>
#                   <li id="item_1_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_1_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_1_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_1_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_1_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_1_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_1_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_1_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                   <li id="item_1_model" data-key="model" class="description_detail">Модель: MECH 2X OC</li>
#                   <li id="item_1_tech_process" data-key="tech_process" class="description_detail">Техпроцесс: 7 нм</li>
#                   <li id="item_1_gpu_frequency" data-key="gpu_frequency" class="description_detail">Частота графического процессора, МГц: 2669</li>
#                   <li id="item_1_stream_processors" data-key="stream_processors" class="description_detail">Количество потоковых процессоров: 2048</li>
#                   <li id="item_1_memory_frequency" data-key="memory_frequency" class="description_detail">Частота видеопамяти, МГц: 17500</li>
#                   <li id="item_1_max_resolution" data-key="max_resolution" class="description_detail">Максимальное поддерживаемое разрешение: 7680x4320 пикс</li>
#                   <li id="item_1_output_ports" data-key="output_ports" class="description_detail">Порты вывода изображения: HDMI, 3 x DisplayPort</li>
#                   <li id="item_1_cooling_system" data-key="cooling_system" class="description_detail">Система охлаждения: Активная (радиатор + 2 вентилятора)</li>
#                   <li id="item_1_cooling_features" data-key="cooling_features" class="description_detail">Особенности системы охлаждения: Двухслотовая система охлаждения</li>
#                   <li id="item_1_power_requirements" data-key="power_requirements" class="description_detail">Требования к блоку питания: 500 Вт</li>
#                   <li id="item_1_os_support" data-key="os_support" class="description_detail">Поддержка операционных систем: Windows 10, Windows 11</li>
#                   <li id="item_1_length" data-key="length" class="description_detail">Длина, мм: 235</li>
#                   <li id="item_1_gross_weight" data-key="gross_weight" class="description_detail">Вес брутто, кг: 0.7</li>
#                   <li id="item_1_manufacturer_site" data-key="manufacturer_site" class="description_detail">Сайт производителя: www.msi.com</li>
#                   <li id="item_1_delivery" data-key="delivery" class="description_detail">Поставка: Retail</li>
#
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">29 040 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/1/1_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#
#       </div>
#
# </body></html>
# '''
#
# def get_html(html):
#     soup = BeautifulSoup(html, 'html.parser')
#
#     li_tag = soup.find('li', attrs={'data-key': 'cooling_system'})
#
#     print(li_tag.text)
#
#
# get_html(html)

# __________________________________________
# Задача : Ваша задача, проанализировать страницу и понять как извлечь тег <img> целиком.
# У тега <img> есть только родитель  и название тега. Найдите способ извлечь тег целиком.

# html = '''
# <html><head>
#       <title>Каталог продуктов</title>
#       <link rel="stylesheet" href="styles.css">
#       <meta charset="UTF-8">
#    </head>
#    <body>
#       <div class="item_card">
#          <div class="item product_item" id="item_1">
#             <div class="img_box product_img_box">
#                <a href="product/1/1_details.html" name="1_img">
#                <img src="images/Видеокарта MSI Radeon RX 6650 XT MECH 2X OC PCI-E 8192Mb GDDR6 128 Bit Retail.jpg" alt="Видеокарта MSI Radeon RX 6650 XT MECH 2X OC PCI-E 8192Mb GDDR6 128 Bit Retail">
#                </a>
#                <a href="product/1/1_details.html" name="1_name" class="name_item product_name">
#                Видеокарта MSI Radeon RX 6650 XT MECH 2X OC PCI-E 8192Mb GDDR6 128 Bit Retail
#                </a>
#                <div class="description product_description">
#                   <li id="item_1_brand" data-key="brand" class="description_detail">Бренд: MSI</li>
#                   <li id="item_1_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_1_processor series" data-key="processor series" class="description_detail">Серия процессора: Radeon RX</li>
#                   <li id="item_1_graphic_processor" data-key="graphic_processor" class="description detailz">Графический процессор: Radeon RX 6650 XT</li>
#                   <li id="item_1_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_1_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_1_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_1_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_1_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_1_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_1_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_1_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                   <li id="item_1_model" data-key="model" class="description_detail">Модель: MECH 2X OC</li>
#                   <li id="item_1_tech_process" data-key="tech_process" class="description_detail">Техпроцесс: 7 нм</li>
#                   <li id="item_1_gpu_frequency" data-key="gpu_frequency" class="description_detail">Частота графического процессора, МГц: 2669</li>
#                   <li id="item_1_stream_processors" data-key="stream_processors" class="description_detail">Количество потоковых процессоров: 2048</li>
#                   <li id="item_1_memory_frequency" data-key="memory_frequency" class="description_detail">Частота видеопамяти, МГц: 17500</li>
#                   <li id="item_1_max_resolution" data-key="max_resolution" class="description_detail">Максимальное поддерживаемое разрешение: 7680x4320 пикс</li>
#                   <li id="item_1_output_ports" data-key="output_ports" class="description_detail">Порты вывода изображения: HDMI, 3 x DisplayPort</li>
#                   <li id="item_1_cooling_system" data-key="cooling_system" class="description_detail">Система охлаждения: Активная (радиатор + 2 вентилятора)</li>
#                   <li id="item_1_cooling_features" data-key="cooling_features" class="description_detail">Особенности системы охлаждения: Двухслотовая система охлаждения</li>
#                   <li id="item_1_power_requirements" data-key="power_requirements" class="description_detail">Требования к блоку питания: 500 Вт</li>
#                   <li id="item_1_os_support" data-key="os_support" class="description_detail">Поддержка операционных систем: Windows 10, Windows 11</li>
#                   <li id="item_1_length" data-key="length" class="description_detail">Длина, мм: 235</li>
#                   <li id="item_1_gross_weight" data-key="gross_weight" class="description_detail">Вес брутто, кг: 0.7</li>
#                   <li id="item_1_manufacturer_site" data-key="manufacturer_site" class="description_detail">Сайт производителя: www.msi.com</li>
#                   <li id="item_1_delivery" data-key="delivery" class="description_detail">Поставка: Retail</li>
#
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">29 040 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/1/1_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#
#       </div>
#
# </body></html>
# '''
#
# def get_html(html):
#     soup = BeautifulSoup(html, 'html.parser')
#
#     img = soup.find('img')
#
#     print(img)
#
#
# get_html(html)

# __________________________________________
# Задача : Проанализируйте страницу и найдите там тег с двойным классом description detailz
# Ваша задача найти способ извлечь текст из этого тега.

# html = '''
# <html><head>
#       <title>Каталог продуктов</title>
#       <link rel="stylesheet" href="styles.css">
#       <meta charset="UTF-8">
#    </head>
#    <body>
#       <div class="item_card">
#          <div class="item product_item" id="item_1">
#             <div class="img_box product_img_box">
#                <a href="product/1/1_details.html" name="1_img">
#                <img src="images/Видеокарта MSI Radeon RX 6650 XT MECH 2X OC PCI-E 8192Mb GDDR6 128 Bit Retail.jpg" alt="Видеокарта MSI Radeon RX 6650 XT MECH 2X OC PCI-E 8192Mb GDDR6 128 Bit Retail">
#                </a>
#                <a href="product/1/1_details.html" name="1_name" class="name_item product_name">
#                Видеокарта MSI Radeon RX 6650 XT MECH 2X OC PCI-E 8192Mb GDDR6 128 Bit Retail
#                </a>
#                <div class="description product_description">
#                   <li id="item_1_brand" data-key="brand" class="description_detail">Бренд: MSI</li>
#                   <li id="item_1_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_1_processor series" data-key="processor series" class="description_detail">Серия процессора: Radeon RX</li>
#                   <li id="item_1_graphic_processor" data-key="graphic_processor" class="description detailz">Графический процессор: Radeon RX 6650 XT</li>
#                   <li id="item_1_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_1_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_1_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_1_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_1_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_1_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_1_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_1_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                   <li id="item_1_model" data-key="model" class="description_detail">Модель: MECH 2X OC</li>
#                   <li id="item_1_tech_process" data-key="tech_process" class="description_detail">Техпроцесс: 7 нм</li>
#                   <li id="item_1_gpu_frequency" data-key="gpu_frequency" class="description_detail">Частота графического процессора, МГц: 2669</li>
#                   <li id="item_1_stream_processors" data-key="stream_processors" class="description_detail">Количество потоковых процессоров: 2048</li>
#                   <li id="item_1_memory_frequency" data-key="memory_frequency" class="description_detail">Частота видеопамяти, МГц: 17500</li>
#                   <li id="item_1_max_resolution" data-key="max_resolution" class="description_detail">Максимальное поддерживаемое разрешение: 7680x4320 пикс</li>
#                   <li id="item_1_output_ports" data-key="output_ports" class="description_detail">Порты вывода изображения: HDMI, 3 x DisplayPort</li>
#                   <li id="item_1_cooling_system" data-key="cooling_system" class="description_detail">Система охлаждения: Активная (радиатор + 2 вентилятора)</li>
#                   <li id="item_1_cooling_features" data-key="cooling_features" class="description_detail">Особенности системы охлаждения: Двухслотовая система охлаждения</li>
#                   <li id="item_1_power_requirements" data-key="power_requirements" class="description_detail">Требования к блоку питания: 500 Вт</li>
#                   <li id="item_1_os_support" data-key="os_support" class="description_detail">Поддержка операционных систем: Windows 10, Windows 11</li>
#                   <li id="item_1_length" data-key="length" class="description_detail">Длина, мм: 235</li>
#                   <li id="item_1_gross_weight" data-key="gross_weight" class="description_detail">Вес брутто, кг: 0.7</li>
#                   <li id="item_1_manufacturer_site" data-key="manufacturer_site" class="description_detail">Сайт производителя: www.msi.com</li>
#                   <li id="item_1_delivery" data-key="delivery" class="description_detail">Поставка: Retail</li>
#
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">29 040 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/1/1_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#
#       </div>
#
# </body></html>
# '''
#
# def get_html(html):
#     soup = BeautifulSoup(html, 'html.parser')
#
#     li_tag = soup.find('li', class_='description detailz')
#
#     print(li_tag.text)
#
#
# get_html(html)

# __________________________________________
# Задача : Ваша задача заключается в поиске тега который содержит сразу все перечисленные ниже атрибуты и значения.
# class="description_detail class1 class2 class3"
# data-fdg45="value13"
# data-54dfg60="value14"
# data-d6f50hg="value15"
# После того как тег будет найден, извлеките из него текст.

# html = '''
# <html><head>
#       <title>Каталог продуктов</title>
#       <link rel="stylesheet" href="styles.css">
#       <meta charset="UTF-8">
#    </head>
#    <body>
#       <div class="item_card">
#          <div class="item product_item" id="item_1">
#             <div class="img_box product_img_box">
#                <a href="product/1/1_details.html" name="1_img">
#                <img src="images/Видеокарта GigaByte nVidia GeForce RTX 4060 EAGLE OC PCI-E 8192Mb GDDR6 128 Bit Retail GV-N4060EAGLE OC-8GD.jpg" alt="Видеокарта GigaByte nVidia GeForce RTX 4060 EAGLE OC PCI-E 8192Mb GDDR6 128 Bit Retail">
#                </a>
#                <a href="product/1/1_details.html" name="1_name" class="name_item product_name">
#                Видеокарта GigaByte nVidia GeForce RTX 4060 EAGLE OC PCI-E 8192Mb GDDR6 128 Bit Retail GV-N4060EAGLE OC-8GD
#                </a>
#                <div class="description product_description">
#                   <li class="description_detail class1 class2 class3" data-gn3f="value1" data-hcvbn="value2" data-456ud="value3">Бренд: GigaByte</li>
#                   <li class="description_detail class1 class2 class3" data-gmsd="value4" data-5344v="value5" data-ddfssd="value6">Тип видеокарты: игровая</li>
#                   <li class="description_detail class1 class2 class3" data-fdg45="value13" data-54dfg60="value14" data-45667g="value9">Серия процессора: nVidia GeForce RTX</li>
#                   <li class="description_detail class1 class2 class3" data-gncv="value10" data-54dfg60="value14" data-d6f50hg="value15">Графический процессор: nVidia GeForce RTX 4060</li>
#                   <li class="description_detail class1 class2 class3" data-fdg45="value13" data-54dfg60="value14" data-d6f50hg="value15">Объем видеопамяти: 8192Mb</li>
#                   <li class="description_detail class1 class2 class3" data-hxcn="value16" data-534nfb="value17" data-536hd="value18">Тип видеопамяти: GDDR6</li>
#                   <li class="description_detail class1 class2 class3" data-2346x="value19" data-3hcbm="value20" data-634gd="value21">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li class="description_detail class1 class2 class3" data-hjdv="value22" data-swq34="value23" data-34dfg="value24">Тип подключения: PCI-E</li>
#                   <li class="description_detail class1 class2 class3" data-dvbn="value25" data-g46md="value26" data-567df="value27">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li class="description_detail class1 class2 class3" data-fscb="value28" data-4jdfx="value29" data-234gd="value30">Разъём HDMI: есть</li>
#                   <li class="description_detail class1 class2 class3" data-sdbx="value31" data-634df="value32" data-623fgd="value33">Выход DisplayPort: есть</li>
#                   <li class="description_detail class1 class2 class3" data-f4653="value34" data-5ipfg4="value35" data-d347dff="value36">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">35 280 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/1/1_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#       </div>
#
# </body></html>
# '''
#
# def get_html(html):
#     soup = BeautifulSoup(html, 'html.parser')
#
#     tag = soup.find(class_='description_detail class1 class2 class3', attrs={'data-fdg45': 'value13', 'data-54dfg60': 'value14', 'data-d6f50hg': 'value15'})
#
#     print(tag.text)
#
#
# get_html(html)

# ВОПРОС а в чем разница между class: 'class1 class2 class3' и class: ['class1', 'class2', 'class3'] ??????????????????
# ОТВЕТ  # Итак, основное различие заключается в логике поиска: строка с пробелами требует наличия всех классов в элементе,
# в то время как список допускает наличие любого из перечисленных классов.

# __________________________________________
# Задача :Проанализируйте страницу, определите тег и его атрибуты, затем примените метод .find_all(),
# извлеките из каждого соответствующего тега текст и уберите лишние пробелы.Проанализируйте страницу, определите тег и его атрибуты,
# затем примените метод .find_all(), извлеките из каждого соответствующего тега текст и уберите лишние пробелы.

# html = '''
# <html><head>
#       <title>Каталог продуктов</title>
#       <link rel="stylesheet" href="styles.css">
#       <meta charset="UTF-8">
#    </head>
#    <body>
#       <div class="item_card">
#          <div class="item product_item" id="item_1">
#             <div class="img_box product_img_box">
#                <a href="product/1/1_details.html" name="1_img">
#                <img src="images/Видеокарта MSI Radeon RX 6650 XT MECH 2X OC PCI-E 8192Mb GDDR6 128 Bit Retail.jpg" alt="Видеокарта MSI Radeon RX 6650 XT MECH 2X OC PCI-E 8192Mb GDDR6 128 Bit Retail">
#                </a>
#                <a href="product/1/1_details.html" name="1_name" class="name_item product_name">
#                Видеокарта MSI Radeon RX 6650 XT MECH 2X OC PCI-E 8192Mb GDDR6 128 Bit Retail
#                </a>
#                <div class="description product_description">
#                   <li id="item_1_brand" data-key="brand" class="description_detail">Бренд: MSI</li>
#                   <li id="item_1_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_1_processor_series" data-key="processor_series" class="description_detail">Серия процессора: Radeon RX</li>
#                   <li id="item_1_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: Radeon RX 6650 XT</li>
#                   <li id="item_1_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_1_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_1_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_1_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_1_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_1_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_1_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_1_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">29 040 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/1/1_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_2">
#             <div class="img_box product_img_box">
#                <a href="product/2/2_details.html" name="2_img">
#                <img src="images/Видеокарта GigaByte nVidia GeForce RTX 3050 WINDFORCE OC 8G PCI-E 8192Mb GDDR6 128 Bit Retail GV-N3050WF2OC-8GD.jpg" alt="Видеокарта GigaByte nVidia GeForce RTX 3050 WINDFORCE OC 8G PCI-E 8192Mb GDDR6 128 Bit Retail GV-N3050WF2OC-8GD">
#                </a>
#                <a href="product/2/2_details.html" name="2_name" class="name_item product_name">
#                Видеокарта GigaByte nVidia GeForce RTX 3050 WINDFORCE OC 8G PCI-E 8192Mb GDDR6 128 Bit Retail GV-N3050WF2OC-8GD
#                </a>
#                <div class="description product_description">
#                   <li id="item_2_brand" data-key="brand" class="description_detail">Бренд: GigaByte</li>
#                   <li id="item_2_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_2_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_2_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 3050</li>
#                   <li id="item_2_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_2_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_2_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_2_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_2_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_2_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_2_Разъём DVI" data-key="Разъём DVI" class="description_detail">Разъём DVI: есть</li>
#                   <li id="item_2_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_2_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">27 840 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/2/2_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_3">
#             <div class="img_box product_img_box">
#                <a href="product/3/3_details.html" name="3_img">
#                <img src="images/Видеокарта Palit nVidia GeForce RTX 4070 GamingPro PCI-E 12288Mb GDDR6X 192 Bit Retail NED4070019K9-1043A.jpg" alt="Видеокарта Palit nVidia GeForce RTX 4070 GamingPro PCI-E 12288Mb GDDR6X 192 Bit Retail NED4070019K9-1043A">
#                </a>
#                <a href="product/3/3_details.html" name="3_name" class="name_item product_name">
#                Видеокарта Palit nVidia GeForce RTX 4070 GamingPro PCI-E 12288Mb GDDR6X 192 Bit Retail NED4070019K9-1043A
#                </a>
#                <div class="description product_description">
#                   <li id="item_3_brand" data-key="brand" class="description_detail">Бренд: Palit</li>
#                   <li id="item_3_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_3_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_3_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4070</li>
#                   <li id="item_3_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 12288Mb</li>
#                   <li id="item_3_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6X</li>
#                   <li id="item_3_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 192 Bit</li>
#                   <li id="item_3_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_3_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_3_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_3_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_3_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 16</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">68 490 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/3/3_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_4">
#             <div class="img_box product_img_box">
#                <a href="product/4/4_details.html" name="4_img">
#                <img src="images/Видеокарта MSI nVidia GeForce RTX 3060 GAMING X LHR PCI-E 12288Mb GDDR6 192 Bit Retail (RTX 3060 GAMING X 12G).jpg" alt="Видеокарта MSI nVidia GeForce RTX 3060 GAMING X LHR PCI-E 12288Mb GDDR6 192 Bit Retail (RTX 3060 GAMING X 12G)">
#                </a>
#                <a href="product/4/4_details.html" name="4_name" class="name_item product_name">
#                Видеокарта MSI nVidia GeForce RTX 3060 GAMING X LHR PCI-E 12288Mb GDDR6 192 Bit Retail (RTX 3060 GAMING X 12G)
#                </a>
#                <div class="description product_description">
#                   <li id="item_4_brand" data-key="brand" class="description_detail">Бренд: MSI</li>
#                   <li id="item_4_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_4_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_4_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 3060</li>
#                   <li id="item_4_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 12288Mb</li>
#                   <li id="item_4_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_4_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 192 Bit</li>
#                   <li id="item_4_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_4_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_4_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_4_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_4_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8+6</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">41 280 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/4/4_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_5">
#             <div class="img_box product_img_box">
#                <a href="product/5/5_details.html" name="5_img">
#                <img src="images/Видеокарта MSI nVidia GeForce RTX 4060 Ti GAMING X PCI-E 8192Mb GDDR6 128 Bit Retail.jpg" alt="Видеокарта MSI nVidia GeForce RTX 4060 Ti GAMING X PCI-E 8192Mb GDDR6 128 Bit Retail">
#                </a>
#                <a href="product/5/5_details.html" name="5_name" class="name_item product_name">
#                Видеокарта MSI nVidia GeForce RTX 4060 Ti GAMING X PCI-E 8192Mb GDDR6 128 Bit Retail
#                </a>
#                <div class="description product_description">
#                   <li id="item_5_brand" data-key="brand" class="description_detail">Бренд: MSI</li>
#                   <li id="item_5_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_5_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_5_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4060 Ti</li>
#                   <li id="item_5_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_5_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_5_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_5_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_5_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_5_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_5_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_5_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">48 720 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/5/5_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_6">
#             <div class="img_box product_img_box">
#                <a href="product/6/6_details.html" name="6_img">
#                <img src="images/Видеокарта MSI nVidia GeForce RTX 4060 Ti GAMING X TRIO PCI-E 8192Mb GDDR6 128 Bit Retail.jpg" alt="Видеокарта MSI nVidia GeForce RTX 4060 Ti GAMING X TRIO PCI-E 8192Mb GDDR6 128 Bit Retail">
#                </a>
#                <a href="product/6/6_details.html" name="6_name" class="name_item product_name">
#                Видеокарта MSI nVidia GeForce RTX 4060 Ti GAMING X TRIO PCI-E 8192Mb GDDR6 128 Bit Retail
#                </a>
#                <div class="description product_description">
#                   <li id="item_6_brand" data-key="brand" class="description_detail">Бренд: MSI</li>
#                   <li id="item_6_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_6_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_6_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4060 Ti</li>
#                   <li id="item_6_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_6_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_6_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_6_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_6_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_6_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_6_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_6_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">52 500 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/6/6_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_7">
#             <div class="img_box product_img_box">
#                <a href="product/7/7_details.html" name="7_img">
#                <img src="images/Видеокарта Palit nVidia GeForce RTX 4060 Dual OC PCI-E 8192Mb GDDR6 128 Bit Retail NE64060T19P1-1070D.jpg" alt="Видеокарта Palit nVidia GeForce RTX 4060 Dual OC PCI-E 8192Mb GDDR6 128 Bit Retail NE64060T19P1-1070D">
#                </a>
#                <a href="product/7/7_details.html" name="7_name" class="name_item product_name">
#                Видеокарта Palit nVidia GeForce RTX 4060 Dual OC PCI-E 8192Mb GDDR6 128 Bit Retail NE64060T19P1-1070D
#                </a>
#                <div class="description product_description">
#                   <li id="item_7_brand" data-key="brand" class="description_detail">Бренд: Palit</li>
#                   <li id="item_7_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_7_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_7_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4060</li>
#                   <li id="item_7_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_7_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_7_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_7_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_7_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_7_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_7_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_7_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">35 520 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/7/7_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_8">
#             <div class="img_box product_img_box">
#                <a href="product/8/8_details.html" name="8_img">
#                <img src="images/Видеокарта Palit nVidia GeForce RTX 4060 StormX PCI-E 8192Mb GDDR6 128 Bit Retail NE64060019P1-1070F.jpg" alt="Видеокарта Palit nVidia GeForce RTX 4060 StormX PCI-E 8192Mb GDDR6 128 Bit Retail NE64060019P1-1070F">
#                </a>
#                <a href="product/8/8_details.html" name="8_name" class="name_item product_name">
#                Видеокарта Palit nVidia GeForce RTX 4060 StormX PCI-E 8192Mb GDDR6 128 Bit Retail NE64060019P1-1070F
#                </a>
#                <div class="description product_description">
#                   <li id="item_8_brand" data-key="brand" class="description_detail">Бренд: Palit</li>
#                   <li id="item_8_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_8_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_8_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4060</li>
#                   <li id="item_8_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_8_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_8_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_8_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_8_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_8_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_8_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_8_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">34 720 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/8/8_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_9">
#             <div class="img_box product_img_box">
#                <a href="product/9/9_details.html" name="9_img">
#                <img src="images/Видеокарта Palit nVidia GeForce RTX 4060 DUAL PCI-E 8192Mb GDDR6 128 Bit Retail NE64060019P1-1070D.jpg" alt="Видеокарта Palit nVidia GeForce RTX 4060 DUAL PCI-E 8192Mb GDDR6 128 Bit Retail NE64060019P1-1070D">
#                </a>
#                <a href="product/9/9_details.html" name="9_name" class="name_item product_name">
#                Видеокарта Palit nVidia GeForce RTX 4060 DUAL PCI-E 8192Mb GDDR6 128 Bit Retail NE64060019P1-1070D
#                </a>
#                <div class="description product_description">
#                   <li id="item_9_brand" data-key="brand" class="description_detail">Бренд: Palit</li>
#                   <li id="item_9_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_9_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_9_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4060</li>
#                   <li id="item_9_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_9_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_9_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_9_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_9_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_9_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_9_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_9_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">33 580 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/9/9_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_10">
#             <div class="img_box product_img_box">
#                <a href="product/10/10_details.html" name="10_img">
#                <img src="images/Видеокарта MSI nVidia GeForce RTX 4060 Ti GAMING X SLIM 16G PCI-E 16384Mb GDDR6 128 Bit Retail.jpg" alt="Видеокарта MSI nVidia GeForce RTX 4060 Ti GAMING X SLIM 16G PCI-E 16384Mb GDDR6 128 Bit Retail">
#                </a>
#                <a href="product/10/10_details.html" name="10_name" class="name_item product_name">
#                Видеокарта MSI nVidia GeForce RTX 4060 Ti GAMING X SLIM 16G PCI-E 16384Mb GDDR6 128 Bit Retail
#                </a>
#                <div class="description product_description">
#                   <li id="item_10_brand" data-key="brand" class="description_detail">Бренд: MSI</li>
#                   <li id="item_10_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_10_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_10_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4060 Ti</li>
#                   <li id="item_10_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 16384Mb</li>
#                   <li id="item_10_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_10_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_10_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_10_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_10_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_10_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_10_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">55 950 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/10/10_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_11">
#             <div class="img_box product_img_box">
#                <a href="product/11/11_details.html" name="11_img">
#                <img src="images/Видеокарта MSI nVidia GeForce RTX 4060 Ti VENTUS 3X 16G OC PCI-E 16384Mb GDDR6 128 Bit Retail.jpg" alt="Видеокарта MSI nVidia GeForce RTX 4060 Ti VENTUS 3X 16G OC PCI-E 16384Mb GDDR6 128 Bit Retail">
#                </a>
#                <a href="product/11/11_details.html" name="11_name" class="name_item product_name">
#                Видеокарта MSI nVidia GeForce RTX 4060 Ti VENTUS 3X 16G OC PCI-E 16384Mb GDDR6 128 Bit Retail
#                </a>
#                <div class="description product_description">
#                   <li id="item_11_brand" data-key="brand" class="description_detail">Бренд: MSI</li>
#                   <li id="item_11_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_11_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_11_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4060 Ti</li>
#                   <li id="item_11_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 16384Mb</li>
#                   <li id="item_11_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_11_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_11_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_11_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_11_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_11_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_11_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">52 260 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/11/11_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_12">
#             <div class="img_box product_img_box">
#                <a href="product/12/12_details.html" name="12_img">
#                <img src="images/Видеокарта Maxsun nVidia GeForce RTX 4060 Ti iCraft OC PCI-E 8192Mb GDDR6 128 Bit Retail.jpg" alt="Видеокарта Maxsun nVidia GeForce RTX 4060 Ti iCraft OC PCI-E 8192Mb GDDR6 128 Bit Retail">
#                </a>
#                <a href="product/12/12_details.html" name="12_name" class="name_item product_name">
#                Видеокарта Maxsun nVidia GeForce RTX 4060 Ti iCraft OC PCI-E 8192Mb GDDR6 128 Bit Retail
#                </a>
#                <div class="description product_description">
#                   <li id="item_12_brand" data-key="brand" class="description_detail">Бренд: Maxsun</li>
#                   <li id="item_12_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_12_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_12_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4060 Ti</li>
#                   <li id="item_12_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_12_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_12_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_12_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_12_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_12_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_12_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_12_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">45 350 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/12/12_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_13">
#             <div class="img_box product_img_box">
#                <a href="product/13/13_details.html" name="13_img">
#                <img src="images/Видеокарта GigaByte nVidia GeForce RTX 4070 Ti GAMING PCI-E 12288Mb GDDR6X 192 Bit Retail GV-N407TGAMING-12GD.jpg" alt="Видеокарта GigaByte nVidia GeForce RTX 4070 Ti GAMING PCI-E 12288Mb GDDR6X 192 Bit Retail GV-N407TGAMING-12GD">
#                </a>
#                <a href="product/13/13_details.html" name="13_name" class="name_item product_name">
#                Видеокарта GigaByte nVidia GeForce RTX 4070 Ti GAMING PCI-E 12288Mb GDDR6X 192 Bit Retail GV-N407TGAMING-12GD
#                </a>
#                <div class="description product_description">
#                   <li id="item_13_brand" data-key="brand" class="description_detail">Бренд: GigaByte</li>
#                   <li id="item_13_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_13_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_13_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4070 Ti</li>
#                   <li id="item_13_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 12288Mb</li>
#                   <li id="item_13_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6X</li>
#                   <li id="item_13_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 192 Bit</li>
#                   <li id="item_13_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_13_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_13_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_13_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_13_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 16</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">89 040 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/13/13_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_14">
#             <div class="img_box product_img_box">
#                <a href="product/14/14_details.html" name="14_img">
#                <img src="images/Видеокарта Palit nVidia GeForce RTX 4070 Ti GamingPro White OC PCI-E 12288Mb GDDR6X 192 Bit Retail NED407TV19K9-1043W.jpg" alt="Видеокарта Palit nVidia GeForce RTX 4070 Ti GamingPro White OC PCI-E 12288Mb GDDR6X 192 Bit Retail NED407TV19K9-1043W">
#                </a>
#                <a href="product/14/14_details.html" name="14_name" class="name_item product_name">
#                Видеокарта Palit nVidia GeForce RTX 4070 Ti GamingPro White OC PCI-E 12288Mb GDDR6X 192 Bit Retail NED407TV19K9-1043W
#                </a>
#                <div class="description product_description">
#                   <li id="item_14_brand" data-key="brand" class="description_detail">Бренд: Palit</li>
#                   <li id="item_14_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_14_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_14_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4070 Ti</li>
#                   <li id="item_14_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 12288Mb</li>
#                   <li id="item_14_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6X</li>
#                   <li id="item_14_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 192 Bit</li>
#                   <li id="item_14_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_14_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_14_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_14_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_14_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 16</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">89 620 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/14/14_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_15">
#             <div class="img_box product_img_box">
#                <a href="product/15/15_details.html" name="15_img">
#                <img src="images/Видеокарта ASUS nVidia GeForce RTX 4070 Ti TUF GAMING PCI-E 12288Mb GDDR6X 192 Bit Retail TUF-RTX4070TI-12G-GAMING.jpg" alt="Видеокарта ASUS nVidia GeForce RTX 4070 Ti TUF GAMING PCI-E 12288Mb GDDR6X 192 Bit Retail TUF-RTX4070TI-12G-GAMING">
#                </a>
#                <a href="product/15/15_details.html" name="15_name" class="name_item product_name">
#                Видеокарта ASUS nVidia GeForce RTX 4070 Ti TUF GAMING PCI-E 12288Mb GDDR6X 192 Bit Retail TUF-RTX4070TI-12G-GAMING
#                </a>
#                <div class="description product_description">
#                   <li id="item_15_brand" data-key="brand" class="description_detail">Бренд: ASUS</li>
#                   <li id="item_15_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_15_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_15_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4070 Ti</li>
#                   <li id="item_15_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 12288Mb</li>
#                   <li id="item_15_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6X</li>
#                   <li id="item_15_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 192 Bit</li>
#                   <li id="item_15_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_15_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_15_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_15_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_15_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 16</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">100 580 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/15/15_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_16">
#             <div class="img_box product_img_box">
#                <a href="product/16/16_details.html" name="16_img">
#                <img src="images/Видеокарта GigaByte nVidia GeForce RTX 4070 WINDFORCE OC PCI-E 12288Mb GDDR6X 192 Bit Retail GV-N4070WF3OC-12GD.jpg" alt="Видеокарта GigaByte nVidia GeForce RTX 4070 WINDFORCE OC PCI-E 12288Mb GDDR6X 192 Bit Retail GV-N4070WF3OC-12GD">
#                </a>
#                <a href="product/16/16_details.html" name="16_name" class="name_item product_name">
#                Видеокарта GigaByte nVidia GeForce RTX 4070 WINDFORCE OC PCI-E 12288Mb GDDR6X 192 Bit Retail GV-N4070WF3OC-12GD
#                </a>
#                <div class="description product_description">
#                   <li id="item_16_brand" data-key="brand" class="description_detail">Бренд: GigaByte</li>
#                   <li id="item_16_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_16_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_16_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4070</li>
#                   <li id="item_16_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 12288Mb</li>
#                   <li id="item_16_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6X</li>
#                   <li id="item_16_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 192 Bit</li>
#                   <li id="item_16_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_16_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_16_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_16_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_16_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">68 590 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/16/16_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_17">
#             <div class="img_box product_img_box">
#                <a href="product/17/17_details.html" name="17_img">
#                <img src="images/Видеокарта ASUS nVidia GeForce RTX 3060 Dual V2 OC Edition PCI-E 12288Mb GDDR6 192 Bit Retail.jpg" alt="Видеокарта ASUS nVidia GeForce RTX 3060 Dual V2 OC Edition PCI-E 12288Mb GDDR6 192 Bit Retail">
#                </a>
#                <a href="product/17/17_details.html" name="17_name" class="name_item product_name">
#                Видеокарта ASUS nVidia GeForce RTX 3060 Dual V2 OC Edition PCI-E 12288Mb GDDR6 192 Bit Retail
#                </a>
#                <div class="description product_description">
#                   <li id="item_17_brand" data-key="brand" class="description_detail">Бренд: ASUS</li>
#                   <li id="item_17_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_17_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_17_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 3060</li>
#                   <li id="item_17_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 12288Mb</li>
#                   <li id="item_17_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_17_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 192 Bit</li>
#                   <li id="item_17_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_17_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_17_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_17_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_17_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">41 350 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/17/17_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_18">
#             <div class="img_box product_img_box">
#                <a href="product/18/18_details.html" name="18_img">
#                <img src="images/Видеокарта Palit nVidia GeForce RTX 4070 Dual PCI-E 12288Mb GDDR6X 192 Bit Retail NED4070019K9-1047D.jpg" alt="Видеокарта Palit nVidia GeForce RTX 4070 Dual PCI-E 12288Mb GDDR6X 192 Bit Retail NED4070019K9-1047D">
#                </a>
#                <a href="product/18/18_details.html" name="18_name" class="name_item product_name">
#                Видеокарта Palit nVidia GeForce RTX 4070 Dual PCI-E 12288Mb GDDR6X 192 Bit Retail NED4070019K9-1047D
#                </a>
#                <div class="description product_description">
#                   <li id="item_18_brand" data-key="brand" class="description_detail">Бренд: Palit</li>
#                   <li id="item_18_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_18_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_18_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4070</li>
#                   <li id="item_18_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 12288Mb</li>
#                   <li id="item_18_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6X</li>
#                   <li id="item_18_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 192 Bit</li>
#                   <li id="item_18_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_18_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_18_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_18_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_18_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">62 500 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/18/18_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_19">
#             <div class="img_box product_img_box">
#                <a href="product/19/19_details.html" name="19_img">
#                <img src="images/Видеокарта ASUS Radeon RX 6700 XT DUAL PCI-E 12288Mb GDDR6 192 Bit Retail (DUAL-RX6700XT-12G).jpg" alt="Видеокарта ASUS Radeon RX 6700 XT DUAL PCI-E 12288Mb GDDR6 192 Bit Retail (DUAL-RX6700XT-12G)">
#                </a>
#                <a href="product/19/19_details.html" name="19_name" class="name_item product_name">
#                Видеокарта ASUS Radeon RX 6700 XT DUAL PCI-E 12288Mb GDDR6 192 Bit Retail (DUAL-RX6700XT-12G)
#                </a>
#                <div class="description product_description">
#                   <li id="item_19_brand" data-key="brand" class="description_detail">Бренд: ASUS</li>
#                   <li id="item_19_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_19_processor_series" data-key="processor_series" class="description_detail">Серия процессора: Radeon RX</li>
#                   <li id="item_19_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: Radeon RX 6700 XT</li>
#                   <li id="item_19_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 12288Mb</li>
#                   <li id="item_19_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_19_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 192 Bit</li>
#                   <li id="item_19_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_19_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_19_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_19_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_19_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8+6</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">44 210 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/19/19_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_20">
#             <div class="img_box product_img_box">
#                <a href="product/20/20_details.html" name="20_img">
#                <img src="images/Видеокарта GigaByte nVidia GeForce RTX 3070 GAMING OC LHR PCI-E 8192Mb GDDR6 256 Bit Retail (GV-N3070GAMING OC-8GD 2.0).jpg" alt="Видеокарта GigaByte nVidia GeForce RTX 3070 GAMING OC LHR PCI-E 8192Mb GDDR6 256 Bit Retail (GV-N3070GAMING OC-8GD 2.0)">
#                </a>
#                <a href="product/20/20_details.html" name="20_name" class="name_item product_name">
#                Видеокарта GigaByte nVidia GeForce RTX 3070 GAMING OC LHR PCI-E 8192Mb GDDR6 256 Bit Retail (GV-N3070GAMING OC-8GD 2.0)
#                </a>
#                <div class="description product_description">
#                   <li id="item_20_brand" data-key="brand" class="description_detail">Бренд: GigaByte</li>
#                   <li id="item_20_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_20_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_20_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 3070</li>
#                   <li id="item_20_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_20_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_20_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 256 Bit</li>
#                   <li id="item_20_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_20_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_20_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_20_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_20_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8+6</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">56 890 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/20/20_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_21">
#             <div class="img_box product_img_box">
#                <a href="product/21/21_details.html" name="21_img">
#                <img src="images/Видеокарта Palit nVidia GeForce RTX 4070 GamingPro OC PCI-E 12288Mb GDDR6X 192 Bit Retail NED4070H19K9-1043A.jpg" alt="Видеокарта Palit nVidia GeForce RTX 4070 GamingPro OC PCI-E 12288Mb GDDR6X 192 Bit Retail NED4070H19K9-1043A">
#                </a>
#                <a href="product/21/21_details.html" name="21_name" class="name_item product_name">
#                Видеокарта Palit nVidia GeForce RTX 4070 GamingPro OC PCI-E 12288Mb GDDR6X 192 Bit Retail NED4070H19K9-1043A
#                </a>
#                <div class="description product_description">
#                   <li id="item_21_brand" data-key="brand" class="description_detail">Бренд: Palit</li>
#                   <li id="item_21_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_21_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_21_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4070</li>
#                   <li id="item_21_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 12288Mb</li>
#                   <li id="item_21_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6X</li>
#                   <li id="item_21_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 192 Bit</li>
#                   <li id="item_21_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_21_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_21_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_21_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_21_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 16</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">70 020 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/21/21_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_22">
#             <div class="img_box product_img_box">
#                <a href="product/22/22_details.html" name="22_img">
#                <img src="images/Видеокарта MSI nVidia GeForce RTX 3050 AERO ITX 8G OC PCI-E 8192Mb GDDR6 128 Bit Retail.jpg" alt="Видеокарта MSI nVidia GeForce RTX 3050 AERO ITX 8G OC PCI-E 8192Mb GDDR6 128 Bit Retail">
#                </a>
#                <a href="product/22/22_details.html" name="22_name" class="name_item product_name">
#                Видеокарта MSI nVidia GeForce RTX 3050 AERO ITX 8G OC PCI-E 8192Mb GDDR6 128 Bit Retail
#                </a>
#                <div class="description product_description">
#                   <li id="item_22_brand" data-key="brand" class="description_detail">Бренд: MSI</li>
#                   <li id="item_22_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_22_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_22_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 3050</li>
#                   <li id="item_22_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_22_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_22_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_22_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_22_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_22_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_22_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_22_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">27 610 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/22/22_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_23">
#             <div class="img_box product_img_box">
#                <a href="product/23/23_details.html" name="23_img">
#                <img src="images/Видеокарта MSI nVidia GeForce RTX 3060 Ti VENTUS 2X OCV1 LHR PCI-E 8192Mb GDDR6 256 Bit Retail (3060 Ti VENTUS 2X 8G OCV1 LHR).jpg" alt="Видеокарта MSI nVidia GeForce RTX 3060 Ti VENTUS 2X OCV1 LHR PCI-E 8192Mb GDDR6 256 Bit Retail (3060 Ti VENTUS 2X 8G OCV1 LHR)">
#                </a>
#                <a href="product/23/23_details.html" name="23_name" class="name_item product_name">
#                Видеокарта MSI nVidia GeForce RTX 3060 Ti VENTUS 2X OCV1 LHR PCI-E 8192Mb GDDR6 256 Bit Retail (3060 Ti VENTUS 2X 8G OCV1 LHR)
#                </a>
#                <div class="description product_description">
#                   <li id="item_23_brand" data-key="brand" class="description_detail">Бренд: MSI</li>
#                   <li id="item_23_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_23_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_23_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 3060 Ti</li>
#                   <li id="item_23_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_23_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_23_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 256 Bit</li>
#                   <li id="item_23_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_23_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_23_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_23_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_23_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">46 000 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/23/23_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_24">
#             <div class="img_box product_img_box">
#                <a href="product/24/24_details.html" name="24_img">
#                <img src="images/Видеокарта GigaByte nVidia GeForce RTX 3060 WINDFORCE OC PCI-E 12288Mb GDDR6 192 Bit Retail GV-N3060WF2OC-12GD 2.0.jpg" alt="Видеокарта GigaByte nVidia GeForce RTX 3060 WINDFORCE OC PCI-E 12288Mb GDDR6 192 Bit Retail GV-N3060WF2OC-12GD 2.0">
#                </a>
#                <a href="product/24/24_details.html" name="24_name" class="name_item product_name">
#                Видеокарта GigaByte nVidia GeForce RTX 3060 WINDFORCE OC PCI-E 12288Mb GDDR6 192 Bit Retail GV-N3060WF2OC-12GD 2.0
#                </a>
#                <div class="description product_description">
#                   <li id="item_24_brand" data-key="brand" class="description_detail">Бренд: GigaByte</li>
#                   <li id="item_24_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_24_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_24_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 3060</li>
#                   <li id="item_24_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 12288Mb</li>
#                   <li id="item_24_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_24_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 192 Bit</li>
#                   <li id="item_24_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_24_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_24_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_24_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_24_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">32 310 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/24/24_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_25">
#             <div class="img_box product_img_box">
#                <a href="product/25/25_details.html" name="25_img">
#                <img src="images/Видеокарта CBR nVidia GeForce RTX 3060 Terminator T1 PCI-E 12288Mb GDDR6 192 Bit Retail VGA-MSRTX3060-12G-RTL.jpg" alt="Видеокарта CBR nVidia GeForce RTX 3060 Terminator T1 PCI-E 12288Mb GDDR6 192 Bit Retail VGA-MSRTX3060-12G-RTL">
#                </a>
#                <a href="product/25/25_details.html" name="25_name" class="name_item product_name">
#                Видеокарта CBR nVidia GeForce RTX 3060 Terminator T1 PCI-E 12288Mb GDDR6 192 Bit Retail VGA-MSRTX3060-12G-RTL
#                </a>
#                <div class="description product_description">
#                   <li id="item_25_brand" data-key="brand" class="description_detail">Бренд: CBR</li>
#                   <li id="item_25_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_25_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_25_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 3060</li>
#                   <li id="item_25_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 12288Mb</li>
#                   <li id="item_25_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_25_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 192 Bit</li>
#                   <li id="item_25_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_25_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_25_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_25_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_25_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">33 490 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/25/25_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_26">
#             <div class="img_box product_img_box">
#                <a href="product/26/26_details.html" name="26_img">
#                <img src="images/Видеокарта Palit nVidia GeForce RTX 3070 GamingPro LHR PCI-E 8192Mb GDDR6 256 Bit Retail (NE63070019P2-1041A V1).jpg" alt="Видеокарта Palit nVidia GeForce RTX 3070 GamingPro LHR PCI-E 8192Mb GDDR6 256 Bit Retail (NE63070019P2-1041A V1)">
#                </a>
#                <a href="product/26/26_details.html" name="26_name" class="name_item product_name">
#                Видеокарта Palit nVidia GeForce RTX 3070 GamingPro LHR PCI-E 8192Mb GDDR6 256 Bit Retail (NE63070019P2-1041A V1)
#                </a>
#                <div class="description product_description">
#                   <li id="item_26_brand" data-key="brand" class="description_detail">Бренд: Palit</li>
#                   <li id="item_26_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_26_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_26_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 3070</li>
#                   <li id="item_26_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_26_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_26_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 256 Bit</li>
#                   <li id="item_26_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_26_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_26_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_26_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_26_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8+8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">59 980 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/26/26_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_27">
#             <div class="img_box product_img_box">
#                <a href="product/27/27_details.html" name="27_img">
#                <img src="images/Видеокарта Palit nVidia GeForce RTX 4070 JetStream PCI-E 12288Mb GDDR6X 192 Bit Retail NED4070019K9-1047J.jpg" alt="Видеокарта Palit nVidia GeForce RTX 4070 JetStream PCI-E 12288Mb GDDR6X 192 Bit Retail NED4070019K9-1047J">
#                </a>
#                <a href="product/27/27_details.html" name="27_name" class="name_item product_name">
#                Видеокарта Palit nVidia GeForce RTX 4070 JetStream PCI-E 12288Mb GDDR6X 192 Bit Retail NED4070019K9-1047J
#                </a>
#                <div class="description product_description">
#                   <li id="item_27_brand" data-key="brand" class="description_detail">Бренд: Palit</li>
#                   <li id="item_27_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_27_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_27_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4070</li>
#                   <li id="item_27_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 12288Mb</li>
#                   <li id="item_27_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6X</li>
#                   <li id="item_27_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 192 Bit</li>
#                   <li id="item_27_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_27_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_27_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_27_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_27_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">66 900 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/27/27_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_28">
#             <div class="img_box product_img_box">
#                <a href="product/28/28_details.html" name="28_img">
#                <img src="images/Видеокарта Palit nVidia GeForce RTX 4060 Ti DUAL PCI-E 8192Mb GDDR6 128 Bit Retail NE6406T019P1-1060D.jpg" alt="Видеокарта Palit nVidia GeForce RTX 4060 Ti DUAL PCI-E 8192Mb GDDR6 128 Bit Retail NE6406T019P1-1060D">
#                </a>
#                <a href="product/28/28_details.html" name="28_name" class="name_item product_name">
#                Видеокарта Palit nVidia GeForce RTX 4060 Ti DUAL PCI-E 8192Mb GDDR6 128 Bit Retail NE6406T019P1-1060D
#                </a>
#                <div class="description product_description">
#                   <li id="item_28_brand" data-key="brand" class="description_detail">Бренд: Palit</li>
#                   <li id="item_28_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_28_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_28_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4060 Ti</li>
#                   <li id="item_28_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_28_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_28_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_28_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_28_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_28_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_28_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_28_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">47 190 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/28/28_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_29">
#             <div class="img_box product_img_box">
#                <a href="product/29/29_details.html" name="29_img">
#                <img src="images/Видеокарта MSI GeForce GT 710 GT 710 2GD3H LP PCI-E 2048Mb GDDR3 64 Bit Retail (GT 710 2GD3H LP).jpg" alt="Видеокарта MSI GeForce GT 710 GT 710 2GD3H LP PCI-E 2048Mb GDDR3 64 Bit Retail (GT 710 2GD3H LP)">
#                </a>
#                <a href="product/29/29_details.html" name="29_name" class="name_item product_name">
#                Видеокарта MSI GeForce GT 710 GT 710 2GD3H LP PCI-E 2048Mb GDDR3 64 Bit Retail (GT 710 2GD3H LP)
#                </a>
#                <div class="description product_description">
#                   <li id="item_29_brand" data-key="brand" class="description_detail">Бренд: MSI</li>
#                   <li id="item_29_card_type" data-key="card_type" class="description_detail">Тип видеокарты: офисная</li>
#                   <li id="item_29_processor_series" data-key="processor_series" class="description_detail">Серия процессора: GeForce GT 7xx</li>
#                   <li id="item_29_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: GeForce GT 710</li>
#                   <li id="item_29_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 2048Mb</li>
#                   <li id="item_29_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR3</li>
#                   <li id="item_29_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 64 Bit</li>
#                   <li id="item_29_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_29_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 2.0</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">4 960 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/29/29_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_30">
#             <div class="img_box product_img_box">
#                <a href="product/30/30_details.html" name="30_img">
#                <img src="images/Видеокарта GigaByte nVidia GeForce RTX 4060 EAGLE OC PCI-E 8192Mb GDDR6 128 Bit Retail GV-N4060EAGLE OC-8GD.jpg" alt="Видеокарта GigaByte nVidia GeForce RTX 4060 EAGLE OC PCI-E 8192Mb GDDR6 128 Bit Retail GV-N4060EAGLE OC-8GD">
#                </a>
#                <a href="product/30/30_details.html" name="30_name" class="name_item product_name">
#                Видеокарта GigaByte nVidia GeForce RTX 4060 EAGLE OC PCI-E 8192Mb GDDR6 128 Bit Retail GV-N4060EAGLE OC-8GD
#                </a>
#                <div class="description product_description">
#                   <li id="item_30_brand" data-key="brand" class="description_detail">Бренд: GigaByte</li>
#                   <li id="item_30_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_30_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_30_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4060</li>
#                   <li id="item_30_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_30_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_30_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_30_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_30_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_30_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_30_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_30_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">35 280 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/30/30_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_31">
#             <div class="img_box product_img_box">
#                <a href="product/31/31_details.html" name="31_img">
#                <img src="images/Видеокарта Palit nVidia GeForce RTX 3070 GAMINGPRO PCI-E 8192Mb GDDR6 256 Bit Retail.jpg" alt="Видеокарта Palit nVidia GeForce RTX 3070 GAMINGPRO PCI-E 8192Mb GDDR6 256 Bit Retail">
#                </a>
#                <a href="product/31/31_details.html" name="31_name" class="name_item product_name">
#                Видеокарта Palit nVidia GeForce RTX 3070 GAMINGPRO PCI-E 8192Mb GDDR6 256 Bit Retail
#                </a>
#                <div class="description product_description">
#                   <li id="item_31_brand" data-key="brand" class="description_detail">Бренд: Palit</li>
#                   <li id="item_31_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_31_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_31_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 3070</li>
#                   <li id="item_31_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_31_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_31_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 256 Bit</li>
#                   <li id="item_31_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_31_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_31_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_31_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_31_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8+8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">59 710 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/31/31_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_32">
#             <div class="img_box product_img_box">
#                <a href="product/32/32_details.html" name="32_img">
#                <img src="images/Видеокарта Afox GeForce GT 210 AF210-1024D2LG2 PCI-E 1024Mb DDR2 64 Bit Retail.jpg" alt="Видеокарта Afox GeForce GT 210 AF210-1024D2LG2 PCI-E 1024Mb DDR2 64 Bit Retail">
#                </a>
#                <a href="product/32/32_details.html" name="32_name" class="name_item product_name">
#                Видеокарта Afox GeForce GT 210 AF210-1024D2LG2 PCI-E 1024Mb DDR2 64 Bit Retail
#                </a>
#                <div class="description product_description">
#                   <li id="item_32_brand" data-key="brand" class="description_detail">Бренд: Afox</li>
#                   <li id="item_32_card_type" data-key="card_type" class="description_detail">Тип видеокарты: офисная</li>
#                   <li id="item_32_processor_series" data-key="processor_series" class="description_detail">Серия процессора: GeForce GT 2xx</li>
#                   <li id="item_32_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: GeForce GT 210</li>
#                   <li id="item_32_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 1024Mb</li>
#                   <li id="item_32_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: DDR2</li>
#                   <li id="item_32_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 64 Bit</li>
#                   <li id="item_32_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_32_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 2.0</li>
#                   <li id="item_32_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_32_Разъём DVI" data-key="Разъём DVI" class="description_detail">Разъём DVI: есть</li>
#                   <li id="item_32_Выход VGA" data-key="Выход VGA" class="description_detail">Выход VGA: есть</li>
#                   <li id="item_32_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 0 (нет)</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">2 640 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/32/32_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_33">
#             <div class="img_box product_img_box">
#                <a href="product/33/33_details.html" name="33_img">
#                <img src="images/Видеокарта GigaByte Radeon RX 7600 GAMING OC PCI-E 8192Mb GDDR6 128 Bit Retail GV-R76GAMING OC-8GD.jpg" alt="Видеокарта GigaByte Radeon RX 7600 GAMING OC PCI-E 8192Mb GDDR6 128 Bit Retail GV-R76GAMING OC-8GD">
#                </a>
#                <a href="product/33/33_details.html" name="33_name" class="name_item product_name">
#                Видеокарта GigaByte Radeon RX 7600 GAMING OC PCI-E 8192Mb GDDR6 128 Bit Retail GV-R76GAMING OC-8GD
#                </a>
#                <div class="description product_description">
#                   <li id="item_33_brand" data-key="brand" class="description_detail">Бренд: GigaByte</li>
#                   <li id="item_33_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_33_processor_series" data-key="processor_series" class="description_detail">Серия процессора: Radeon RX</li>
#                   <li id="item_33_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: Radeon RX 7600</li>
#                   <li id="item_33_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_33_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_33_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_33_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_33_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_33_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_33_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_33_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">34 440 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/33/33_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_34">
#             <div class="img_box product_img_box">
#                <a href="product/34/34_details.html" name="34_img">
#                <img src="images/Видеокарта Palit nVidia GeForce RTX 3060 Dual OC PCI-E 12288Mb GDDR6 192 Bit Retail (NE63060T19K9-190AD).jpg" alt="Видеокарта Palit nVidia GeForce RTX 3060 Dual OC PCI-E 12288Mb GDDR6 192 Bit Retail (NE63060T19K9-190AD)">
#                </a>
#                <a href="product/34/34_details.html" name="34_name" class="name_item product_name">
#                Видеокарта Palit nVidia GeForce RTX 3060 Dual OC PCI-E 12288Mb GDDR6 192 Bit Retail (NE63060T19K9-190AD)
#                </a>
#                <div class="description product_description">
#                   <li id="item_34_brand" data-key="brand" class="description_detail">Бренд: Palit</li>
#                   <li id="item_34_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_34_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_34_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 3060</li>
#                   <li id="item_34_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 12288Mb</li>
#                   <li id="item_34_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_34_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 192 Bit</li>
#                   <li id="item_34_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_34_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_34_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_34_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_34_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">33 260 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/34/34_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_35">
#             <div class="img_box product_img_box">
#                <a href="product/35/35_details.html" name="35_img">
#                <img src="images/Видеокарта Palit GeForce GTX 1650 GP PCI-E 4096Mb GDDR6 128 Bit Bulk (NE6165001BG1-1175A).jpg" alt="Видеокарта Palit GeForce GTX 1650 GP PCI-E 4096Mb GDDR6 128 Bit Bulk (NE6165001BG1-1175A)">
#                </a>
#                <a href="product/35/35_details.html" name="35_name" class="name_item product_name">
#                Видеокарта Palit GeForce GTX 1650 GP PCI-E 4096Mb GDDR6 128 Bit Bulk (NE6165001BG1-1175A)
#                </a>
#                <div class="description product_description">
#                   <li id="item_35_brand" data-key="brand" class="description_detail">Бренд: Palit</li>
#                   <li id="item_35_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_35_processor_series" data-key="processor_series" class="description_detail">Серия процессора: GeForce GTX 16хх</li>
#                   <li id="item_35_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: GeForce GTX 1650</li>
#                   <li id="item_35_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 4096Mb</li>
#                   <li id="item_35_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_35_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_35_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_35_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 3.0</li>
#                   <li id="item_35_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_35_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_35_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 6</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">20 280 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/35/35_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#       </div>
#
# </body></html>
# '''
#
# def get_html(html):
#     soup = BeautifulSoup(html, 'html.parser')
#
#     tags = soup.findAll('a', class_='name_item product_name')
#
#     for tag in tags:
#         str1 = str(tag.text)
#
#         print(str1.strip())  # Извлеките текст и обрежьте лишние пробелы
#
# get_html(html)

# __________________________________________
# Задача: Проанализируйте структуру сайта, найдите способ получить все цены с помощью .find_all(), затем суммируйте их.

# html = '''
# <html><head>
#       <title>Каталог продуктов</title>
#       <link rel="stylesheet" href="styles.css">
#       <meta charset="UTF-8">
#    </head>
#    <body>
#       <div class="item_card">
#          <div class="item product_item" id="item_1">
#             <div class="img_box product_img_box">
#                <a href="product/1/1_details.html" name="1_img">
#                <img src="images/Видеокарта MSI Radeon RX 6650 XT MECH 2X OC PCI-E 8192Mb GDDR6 128 Bit Retail.jpg" alt="Видеокарта MSI Radeon RX 6650 XT MECH 2X OC PCI-E 8192Mb GDDR6 128 Bit Retail">
#                </a>
#                <a href="product/1/1_details.html" name="1_name" class="name_item product_name">
#                Видеокарта MSI Radeon RX 6650 XT MECH 2X OC PCI-E 8192Mb GDDR6 128 Bit Retail
#                </a>
#                <div class="description product_description">
#                   <li id="item_1_brand" data-key="brand" class="description_detail">Бренд: MSI</li>
#                   <li id="item_1_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_1_processor_series" data-key="processor_series" class="description_detail">Серия процессора: Radeon RX</li>
#                   <li id="item_1_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: Radeon RX 6650 XT</li>
#                   <li id="item_1_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_1_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_1_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_1_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_1_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_1_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_1_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_1_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">29 040 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/1/1_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_2">
#             <div class="img_box product_img_box">
#                <a href="product/2/2_details.html" name="2_img">
#                <img src="images/Видеокарта GigaByte nVidia GeForce RTX 3050 WINDFORCE OC 8G PCI-E 8192Mb GDDR6 128 Bit Retail GV-N3050WF2OC-8GD.jpg" alt="Видеокарта GigaByte nVidia GeForce RTX 3050 WINDFORCE OC 8G PCI-E 8192Mb GDDR6 128 Bit Retail GV-N3050WF2OC-8GD">
#                </a>
#                <a href="product/2/2_details.html" name="2_name" class="name_item product_name">
#                Видеокарта GigaByte nVidia GeForce RTX 3050 WINDFORCE OC 8G PCI-E 8192Mb GDDR6 128 Bit Retail GV-N3050WF2OC-8GD
#                </a>
#                <div class="description product_description">
#                   <li id="item_2_brand" data-key="brand" class="description_detail">Бренд: GigaByte</li>
#                   <li id="item_2_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_2_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_2_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 3050</li>
#                   <li id="item_2_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_2_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_2_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_2_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_2_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_2_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_2_Разъём DVI" data-key="Разъём DVI" class="description_detail">Разъём DVI: есть</li>
#                   <li id="item_2_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_2_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">27 840 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/2/2_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_3">
#             <div class="img_box product_img_box">
#                <a href="product/3/3_details.html" name="3_img">
#                <img src="images/Видеокарта Palit nVidia GeForce RTX 4070 GamingPro PCI-E 12288Mb GDDR6X 192 Bit Retail NED4070019K9-1043A.jpg" alt="Видеокарта Palit nVidia GeForce RTX 4070 GamingPro PCI-E 12288Mb GDDR6X 192 Bit Retail NED4070019K9-1043A">
#                </a>
#                <a href="product/3/3_details.html" name="3_name" class="name_item product_name">
#                Видеокарта Palit nVidia GeForce RTX 4070 GamingPro PCI-E 12288Mb GDDR6X 192 Bit Retail NED4070019K9-1043A
#                </a>
#                <div class="description product_description">
#                   <li id="item_3_brand" data-key="brand" class="description_detail">Бренд: Palit</li>
#                   <li id="item_3_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_3_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_3_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4070</li>
#                   <li id="item_3_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 12288Mb</li>
#                   <li id="item_3_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6X</li>
#                   <li id="item_3_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 192 Bit</li>
#                   <li id="item_3_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_3_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_3_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_3_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_3_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 16</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">68 490 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/3/3_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_4">
#             <div class="img_box product_img_box">
#                <a href="product/4/4_details.html" name="4_img">
#                <img src="images/Видеокарта MSI nVidia GeForce RTX 3060 GAMING X LHR PCI-E 12288Mb GDDR6 192 Bit Retail (RTX 3060 GAMING X 12G).jpg" alt="Видеокарта MSI nVidia GeForce RTX 3060 GAMING X LHR PCI-E 12288Mb GDDR6 192 Bit Retail (RTX 3060 GAMING X 12G)">
#                </a>
#                <a href="product/4/4_details.html" name="4_name" class="name_item product_name">
#                Видеокарта MSI nVidia GeForce RTX 3060 GAMING X LHR PCI-E 12288Mb GDDR6 192 Bit Retail (RTX 3060 GAMING X 12G)
#                </a>
#                <div class="description product_description">
#                   <li id="item_4_brand" data-key="brand" class="description_detail">Бренд: MSI</li>
#                   <li id="item_4_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_4_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_4_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 3060</li>
#                   <li id="item_4_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 12288Mb</li>
#                   <li id="item_4_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_4_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 192 Bit</li>
#                   <li id="item_4_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_4_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_4_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_4_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_4_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8+6</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">41 280 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/4/4_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_5">
#             <div class="img_box product_img_box">
#                <a href="product/5/5_details.html" name="5_img">
#                <img src="images/Видеокарта MSI nVidia GeForce RTX 4060 Ti GAMING X PCI-E 8192Mb GDDR6 128 Bit Retail.jpg" alt="Видеокарта MSI nVidia GeForce RTX 4060 Ti GAMING X PCI-E 8192Mb GDDR6 128 Bit Retail">
#                </a>
#                <a href="product/5/5_details.html" name="5_name" class="name_item product_name">
#                Видеокарта MSI nVidia GeForce RTX 4060 Ti GAMING X PCI-E 8192Mb GDDR6 128 Bit Retail
#                </a>
#                <div class="description product_description">
#                   <li id="item_5_brand" data-key="brand" class="description_detail">Бренд: MSI</li>
#                   <li id="item_5_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_5_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_5_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4060 Ti</li>
#                   <li id="item_5_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_5_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_5_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_5_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_5_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_5_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_5_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_5_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">48 720 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/5/5_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_6">
#             <div class="img_box product_img_box">
#                <a href="product/6/6_details.html" name="6_img">
#                <img src="images/Видеокарта MSI nVidia GeForce RTX 4060 Ti GAMING X TRIO PCI-E 8192Mb GDDR6 128 Bit Retail.jpg" alt="Видеокарта MSI nVidia GeForce RTX 4060 Ti GAMING X TRIO PCI-E 8192Mb GDDR6 128 Bit Retail">
#                </a>
#                <a href="product/6/6_details.html" name="6_name" class="name_item product_name">
#                Видеокарта MSI nVidia GeForce RTX 4060 Ti GAMING X TRIO PCI-E 8192Mb GDDR6 128 Bit Retail
#                </a>
#                <div class="description product_description">
#                   <li id="item_6_brand" data-key="brand" class="description_detail">Бренд: MSI</li>
#                   <li id="item_6_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_6_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_6_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4060 Ti</li>
#                   <li id="item_6_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_6_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_6_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_6_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_6_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_6_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_6_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_6_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">52 500 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/6/6_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_7">
#             <div class="img_box product_img_box">
#                <a href="product/7/7_details.html" name="7_img">
#                <img src="images/Видеокарта Palit nVidia GeForce RTX 4060 Dual OC PCI-E 8192Mb GDDR6 128 Bit Retail NE64060T19P1-1070D.jpg" alt="Видеокарта Palit nVidia GeForce RTX 4060 Dual OC PCI-E 8192Mb GDDR6 128 Bit Retail NE64060T19P1-1070D">
#                </a>
#                <a href="product/7/7_details.html" name="7_name" class="name_item product_name">
#                Видеокарта Palit nVidia GeForce RTX 4060 Dual OC PCI-E 8192Mb GDDR6 128 Bit Retail NE64060T19P1-1070D
#                </a>
#                <div class="description product_description">
#                   <li id="item_7_brand" data-key="brand" class="description_detail">Бренд: Palit</li>
#                   <li id="item_7_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_7_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_7_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4060</li>
#                   <li id="item_7_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_7_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_7_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_7_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_7_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_7_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_7_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_7_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">35 520 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/7/7_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_8">
#             <div class="img_box product_img_box">
#                <a href="product/8/8_details.html" name="8_img">
#                <img src="images/Видеокарта Palit nVidia GeForce RTX 4060 StormX PCI-E 8192Mb GDDR6 128 Bit Retail NE64060019P1-1070F.jpg" alt="Видеокарта Palit nVidia GeForce RTX 4060 StormX PCI-E 8192Mb GDDR6 128 Bit Retail NE64060019P1-1070F">
#                </a>
#                <a href="product/8/8_details.html" name="8_name" class="name_item product_name">
#                Видеокарта Palit nVidia GeForce RTX 4060 StormX PCI-E 8192Mb GDDR6 128 Bit Retail NE64060019P1-1070F
#                </a>
#                <div class="description product_description">
#                   <li id="item_8_brand" data-key="brand" class="description_detail">Бренд: Palit</li>
#                   <li id="item_8_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_8_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_8_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4060</li>
#                   <li id="item_8_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_8_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_8_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_8_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_8_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_8_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_8_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_8_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">34 720 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/8/8_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_9">
#             <div class="img_box product_img_box">
#                <a href="product/9/9_details.html" name="9_img">
#                <img src="images/Видеокарта Palit nVidia GeForce RTX 4060 DUAL PCI-E 8192Mb GDDR6 128 Bit Retail NE64060019P1-1070D.jpg" alt="Видеокарта Palit nVidia GeForce RTX 4060 DUAL PCI-E 8192Mb GDDR6 128 Bit Retail NE64060019P1-1070D">
#                </a>
#                <a href="product/9/9_details.html" name="9_name" class="name_item product_name">
#                Видеокарта Palit nVidia GeForce RTX 4060 DUAL PCI-E 8192Mb GDDR6 128 Bit Retail NE64060019P1-1070D
#                </a>
#                <div class="description product_description">
#                   <li id="item_9_brand" data-key="brand" class="description_detail">Бренд: Palit</li>
#                   <li id="item_9_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_9_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_9_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4060</li>
#                   <li id="item_9_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_9_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_9_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_9_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_9_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_9_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_9_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_9_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">33 580 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/9/9_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_10">
#             <div class="img_box product_img_box">
#                <a href="product/10/10_details.html" name="10_img">
#                <img src="images/Видеокарта MSI nVidia GeForce RTX 4060 Ti GAMING X SLIM 16G PCI-E 16384Mb GDDR6 128 Bit Retail.jpg" alt="Видеокарта MSI nVidia GeForce RTX 4060 Ti GAMING X SLIM 16G PCI-E 16384Mb GDDR6 128 Bit Retail">
#                </a>
#                <a href="product/10/10_details.html" name="10_name" class="name_item product_name">
#                Видеокарта MSI nVidia GeForce RTX 4060 Ti GAMING X SLIM 16G PCI-E 16384Mb GDDR6 128 Bit Retail
#                </a>
#                <div class="description product_description">
#                   <li id="item_10_brand" data-key="brand" class="description_detail">Бренд: MSI</li>
#                   <li id="item_10_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_10_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_10_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4060 Ti</li>
#                   <li id="item_10_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 16384Mb</li>
#                   <li id="item_10_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_10_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_10_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_10_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_10_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_10_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_10_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">55 950 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/10/10_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_11">
#             <div class="img_box product_img_box">
#                <a href="product/11/11_details.html" name="11_img">
#                <img src="images/Видеокарта MSI nVidia GeForce RTX 4060 Ti VENTUS 3X 16G OC PCI-E 16384Mb GDDR6 128 Bit Retail.jpg" alt="Видеокарта MSI nVidia GeForce RTX 4060 Ti VENTUS 3X 16G OC PCI-E 16384Mb GDDR6 128 Bit Retail">
#                </a>
#                <a href="product/11/11_details.html" name="11_name" class="name_item product_name">
#                Видеокарта MSI nVidia GeForce RTX 4060 Ti VENTUS 3X 16G OC PCI-E 16384Mb GDDR6 128 Bit Retail
#                </a>
#                <div class="description product_description">
#                   <li id="item_11_brand" data-key="brand" class="description_detail">Бренд: MSI</li>
#                   <li id="item_11_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_11_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_11_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4060 Ti</li>
#                   <li id="item_11_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 16384Mb</li>
#                   <li id="item_11_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_11_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_11_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_11_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_11_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_11_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_11_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">52 260 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/11/11_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_12">
#             <div class="img_box product_img_box">
#                <a href="product/12/12_details.html" name="12_img">
#                <img src="images/Видеокарта Maxsun nVidia GeForce RTX 4060 Ti iCraft OC PCI-E 8192Mb GDDR6 128 Bit Retail.jpg" alt="Видеокарта Maxsun nVidia GeForce RTX 4060 Ti iCraft OC PCI-E 8192Mb GDDR6 128 Bit Retail">
#                </a>
#                <a href="product/12/12_details.html" name="12_name" class="name_item product_name">
#                Видеокарта Maxsun nVidia GeForce RTX 4060 Ti iCraft OC PCI-E 8192Mb GDDR6 128 Bit Retail
#                </a>
#                <div class="description product_description">
#                   <li id="item_12_brand" data-key="brand" class="description_detail">Бренд: Maxsun</li>
#                   <li id="item_12_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_12_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_12_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4060 Ti</li>
#                   <li id="item_12_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_12_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_12_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_12_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_12_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_12_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_12_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_12_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">45 350 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/12/12_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_13">
#             <div class="img_box product_img_box">
#                <a href="product/13/13_details.html" name="13_img">
#                <img src="images/Видеокарта GigaByte nVidia GeForce RTX 4070 Ti GAMING PCI-E 12288Mb GDDR6X 192 Bit Retail GV-N407TGAMING-12GD.jpg" alt="Видеокарта GigaByte nVidia GeForce RTX 4070 Ti GAMING PCI-E 12288Mb GDDR6X 192 Bit Retail GV-N407TGAMING-12GD">
#                </a>
#                <a href="product/13/13_details.html" name="13_name" class="name_item product_name">
#                Видеокарта GigaByte nVidia GeForce RTX 4070 Ti GAMING PCI-E 12288Mb GDDR6X 192 Bit Retail GV-N407TGAMING-12GD
#                </a>
#                <div class="description product_description">
#                   <li id="item_13_brand" data-key="brand" class="description_detail">Бренд: GigaByte</li>
#                   <li id="item_13_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_13_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_13_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4070 Ti</li>
#                   <li id="item_13_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 12288Mb</li>
#                   <li id="item_13_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6X</li>
#                   <li id="item_13_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 192 Bit</li>
#                   <li id="item_13_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_13_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_13_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_13_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_13_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 16</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">89 040 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/13/13_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_14">
#             <div class="img_box product_img_box">
#                <a href="product/14/14_details.html" name="14_img">
#                <img src="images/Видеокарта Palit nVidia GeForce RTX 4070 Ti GamingPro White OC PCI-E 12288Mb GDDR6X 192 Bit Retail NED407TV19K9-1043W.jpg" alt="Видеокарта Palit nVidia GeForce RTX 4070 Ti GamingPro White OC PCI-E 12288Mb GDDR6X 192 Bit Retail NED407TV19K9-1043W">
#                </a>
#                <a href="product/14/14_details.html" name="14_name" class="name_item product_name">
#                Видеокарта Palit nVidia GeForce RTX 4070 Ti GamingPro White OC PCI-E 12288Mb GDDR6X 192 Bit Retail NED407TV19K9-1043W
#                </a>
#                <div class="description product_description">
#                   <li id="item_14_brand" data-key="brand" class="description_detail">Бренд: Palit</li>
#                   <li id="item_14_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_14_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_14_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4070 Ti</li>
#                   <li id="item_14_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 12288Mb</li>
#                   <li id="item_14_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6X</li>
#                   <li id="item_14_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 192 Bit</li>
#                   <li id="item_14_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_14_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_14_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_14_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_14_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 16</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">89 620 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/14/14_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_15">
#             <div class="img_box product_img_box">
#                <a href="product/15/15_details.html" name="15_img">
#                <img src="images/Видеокарта ASUS nVidia GeForce RTX 4070 Ti TUF GAMING PCI-E 12288Mb GDDR6X 192 Bit Retail TUF-RTX4070TI-12G-GAMING.jpg" alt="Видеокарта ASUS nVidia GeForce RTX 4070 Ti TUF GAMING PCI-E 12288Mb GDDR6X 192 Bit Retail TUF-RTX4070TI-12G-GAMING">
#                </a>
#                <a href="product/15/15_details.html" name="15_name" class="name_item product_name">
#                Видеокарта ASUS nVidia GeForce RTX 4070 Ti TUF GAMING PCI-E 12288Mb GDDR6X 192 Bit Retail TUF-RTX4070TI-12G-GAMING
#                </a>
#                <div class="description product_description">
#                   <li id="item_15_brand" data-key="brand" class="description_detail">Бренд: ASUS</li>
#                   <li id="item_15_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_15_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_15_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4070 Ti</li>
#                   <li id="item_15_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 12288Mb</li>
#                   <li id="item_15_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6X</li>
#                   <li id="item_15_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 192 Bit</li>
#                   <li id="item_15_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_15_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_15_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_15_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_15_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 16</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">100 580 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/15/15_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_16">
#             <div class="img_box product_img_box">
#                <a href="product/16/16_details.html" name="16_img">
#                <img src="images/Видеокарта GigaByte nVidia GeForce RTX 4070 WINDFORCE OC PCI-E 12288Mb GDDR6X 192 Bit Retail GV-N4070WF3OC-12GD.jpg" alt="Видеокарта GigaByte nVidia GeForce RTX 4070 WINDFORCE OC PCI-E 12288Mb GDDR6X 192 Bit Retail GV-N4070WF3OC-12GD">
#                </a>
#                <a href="product/16/16_details.html" name="16_name" class="name_item product_name">
#                Видеокарта GigaByte nVidia GeForce RTX 4070 WINDFORCE OC PCI-E 12288Mb GDDR6X 192 Bit Retail GV-N4070WF3OC-12GD
#                </a>
#                <div class="description product_description">
#                   <li id="item_16_brand" data-key="brand" class="description_detail">Бренд: GigaByte</li>
#                   <li id="item_16_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_16_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_16_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4070</li>
#                   <li id="item_16_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 12288Mb</li>
#                   <li id="item_16_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6X</li>
#                   <li id="item_16_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 192 Bit</li>
#                   <li id="item_16_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_16_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_16_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_16_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_16_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">68 590 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/16/16_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_17">
#             <div class="img_box product_img_box">
#                <a href="product/17/17_details.html" name="17_img">
#                <img src="images/Видеокарта ASUS nVidia GeForce RTX 3060 Dual V2 OC Edition PCI-E 12288Mb GDDR6 192 Bit Retail.jpg" alt="Видеокарта ASUS nVidia GeForce RTX 3060 Dual V2 OC Edition PCI-E 12288Mb GDDR6 192 Bit Retail">
#                </a>
#                <a href="product/17/17_details.html" name="17_name" class="name_item product_name">
#                Видеокарта ASUS nVidia GeForce RTX 3060 Dual V2 OC Edition PCI-E 12288Mb GDDR6 192 Bit Retail
#                </a>
#                <div class="description product_description">
#                   <li id="item_17_brand" data-key="brand" class="description_detail">Бренд: ASUS</li>
#                   <li id="item_17_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_17_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_17_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 3060</li>
#                   <li id="item_17_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 12288Mb</li>
#                   <li id="item_17_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_17_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 192 Bit</li>
#                   <li id="item_17_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_17_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_17_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_17_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_17_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">41 350 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/17/17_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_18">
#             <div class="img_box product_img_box">
#                <a href="product/18/18_details.html" name="18_img">
#                <img src="images/Видеокарта Palit nVidia GeForce RTX 4070 Dual PCI-E 12288Mb GDDR6X 192 Bit Retail NED4070019K9-1047D.jpg" alt="Видеокарта Palit nVidia GeForce RTX 4070 Dual PCI-E 12288Mb GDDR6X 192 Bit Retail NED4070019K9-1047D">
#                </a>
#                <a href="product/18/18_details.html" name="18_name" class="name_item product_name">
#                Видеокарта Palit nVidia GeForce RTX 4070 Dual PCI-E 12288Mb GDDR6X 192 Bit Retail NED4070019K9-1047D
#                </a>
#                <div class="description product_description">
#                   <li id="item_18_brand" data-key="brand" class="description_detail">Бренд: Palit</li>
#                   <li id="item_18_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_18_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_18_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4070</li>
#                   <li id="item_18_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 12288Mb</li>
#                   <li id="item_18_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6X</li>
#                   <li id="item_18_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 192 Bit</li>
#                   <li id="item_18_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_18_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_18_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_18_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_18_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">62 500 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/18/18_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_19">
#             <div class="img_box product_img_box">
#                <a href="product/19/19_details.html" name="19_img">
#                <img src="images/Видеокарта ASUS Radeon RX 6700 XT DUAL PCI-E 12288Mb GDDR6 192 Bit Retail (DUAL-RX6700XT-12G).jpg" alt="Видеокарта ASUS Radeon RX 6700 XT DUAL PCI-E 12288Mb GDDR6 192 Bit Retail (DUAL-RX6700XT-12G)">
#                </a>
#                <a href="product/19/19_details.html" name="19_name" class="name_item product_name">
#                Видеокарта ASUS Radeon RX 6700 XT DUAL PCI-E 12288Mb GDDR6 192 Bit Retail (DUAL-RX6700XT-12G)
#                </a>
#                <div class="description product_description">
#                   <li id="item_19_brand" data-key="brand" class="description_detail">Бренд: ASUS</li>
#                   <li id="item_19_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_19_processor_series" data-key="processor_series" class="description_detail">Серия процессора: Radeon RX</li>
#                   <li id="item_19_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: Radeon RX 6700 XT</li>
#                   <li id="item_19_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 12288Mb</li>
#                   <li id="item_19_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_19_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 192 Bit</li>
#                   <li id="item_19_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_19_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_19_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_19_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_19_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8+6</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">44 210 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/19/19_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_20">
#             <div class="img_box product_img_box">
#                <a href="product/20/20_details.html" name="20_img">
#                <img src="images/Видеокарта GigaByte nVidia GeForce RTX 3070 GAMING OC LHR PCI-E 8192Mb GDDR6 256 Bit Retail (GV-N3070GAMING OC-8GD 2.0).jpg" alt="Видеокарта GigaByte nVidia GeForce RTX 3070 GAMING OC LHR PCI-E 8192Mb GDDR6 256 Bit Retail (GV-N3070GAMING OC-8GD 2.0)">
#                </a>
#                <a href="product/20/20_details.html" name="20_name" class="name_item product_name">
#                Видеокарта GigaByte nVidia GeForce RTX 3070 GAMING OC LHR PCI-E 8192Mb GDDR6 256 Bit Retail (GV-N3070GAMING OC-8GD 2.0)
#                </a>
#                <div class="description product_description">
#                   <li id="item_20_brand" data-key="brand" class="description_detail">Бренд: GigaByte</li>
#                   <li id="item_20_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_20_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_20_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 3070</li>
#                   <li id="item_20_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_20_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_20_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 256 Bit</li>
#                   <li id="item_20_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_20_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_20_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_20_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_20_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8+6</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">56 890 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/20/20_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_21">
#             <div class="img_box product_img_box">
#                <a href="product/21/21_details.html" name="21_img">
#                <img src="images/Видеокарта Palit nVidia GeForce RTX 4070 GamingPro OC PCI-E 12288Mb GDDR6X 192 Bit Retail NED4070H19K9-1043A.jpg" alt="Видеокарта Palit nVidia GeForce RTX 4070 GamingPro OC PCI-E 12288Mb GDDR6X 192 Bit Retail NED4070H19K9-1043A">
#                </a>
#                <a href="product/21/21_details.html" name="21_name" class="name_item product_name">
#                Видеокарта Palit nVidia GeForce RTX 4070 GamingPro OC PCI-E 12288Mb GDDR6X 192 Bit Retail NED4070H19K9-1043A
#                </a>
#                <div class="description product_description">
#                   <li id="item_21_brand" data-key="brand" class="description_detail">Бренд: Palit</li>
#                   <li id="item_21_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_21_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_21_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4070</li>
#                   <li id="item_21_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 12288Mb</li>
#                   <li id="item_21_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6X</li>
#                   <li id="item_21_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 192 Bit</li>
#                   <li id="item_21_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_21_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_21_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_21_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_21_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 16</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">70 020 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/21/21_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_22">
#             <div class="img_box product_img_box">
#                <a href="product/22/22_details.html" name="22_img">
#                <img src="images/Видеокарта MSI nVidia GeForce RTX 3050 AERO ITX 8G OC PCI-E 8192Mb GDDR6 128 Bit Retail.jpg" alt="Видеокарта MSI nVidia GeForce RTX 3050 AERO ITX 8G OC PCI-E 8192Mb GDDR6 128 Bit Retail">
#                </a>
#                <a href="product/22/22_details.html" name="22_name" class="name_item product_name">
#                Видеокарта MSI nVidia GeForce RTX 3050 AERO ITX 8G OC PCI-E 8192Mb GDDR6 128 Bit Retail
#                </a>
#                <div class="description product_description">
#                   <li id="item_22_brand" data-key="brand" class="description_detail">Бренд: MSI</li>
#                   <li id="item_22_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_22_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_22_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 3050</li>
#                   <li id="item_22_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_22_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_22_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_22_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_22_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_22_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_22_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_22_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">27 610 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/22/22_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_23">
#             <div class="img_box product_img_box">
#                <a href="product/23/23_details.html" name="23_img">
#                <img src="images/Видеокарта MSI nVidia GeForce RTX 3060 Ti VENTUS 2X OCV1 LHR PCI-E 8192Mb GDDR6 256 Bit Retail (3060 Ti VENTUS 2X 8G OCV1 LHR).jpg" alt="Видеокарта MSI nVidia GeForce RTX 3060 Ti VENTUS 2X OCV1 LHR PCI-E 8192Mb GDDR6 256 Bit Retail (3060 Ti VENTUS 2X 8G OCV1 LHR)">
#                </a>
#                <a href="product/23/23_details.html" name="23_name" class="name_item product_name">
#                Видеокарта MSI nVidia GeForce RTX 3060 Ti VENTUS 2X OCV1 LHR PCI-E 8192Mb GDDR6 256 Bit Retail (3060 Ti VENTUS 2X 8G OCV1 LHR)
#                </a>
#                <div class="description product_description">
#                   <li id="item_23_brand" data-key="brand" class="description_detail">Бренд: MSI</li>
#                   <li id="item_23_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_23_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_23_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 3060 Ti</li>
#                   <li id="item_23_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_23_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_23_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 256 Bit</li>
#                   <li id="item_23_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_23_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_23_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_23_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_23_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">46 000 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/23/23_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_24">
#             <div class="img_box product_img_box">
#                <a href="product/24/24_details.html" name="24_img">
#                <img src="images/Видеокарта GigaByte nVidia GeForce RTX 3060 WINDFORCE OC PCI-E 12288Mb GDDR6 192 Bit Retail GV-N3060WF2OC-12GD 2.0.jpg" alt="Видеокарта GigaByte nVidia GeForce RTX 3060 WINDFORCE OC PCI-E 12288Mb GDDR6 192 Bit Retail GV-N3060WF2OC-12GD 2.0">
#                </a>
#                <a href="product/24/24_details.html" name="24_name" class="name_item product_name">
#                Видеокарта GigaByte nVidia GeForce RTX 3060 WINDFORCE OC PCI-E 12288Mb GDDR6 192 Bit Retail GV-N3060WF2OC-12GD 2.0
#                </a>
#                <div class="description product_description">
#                   <li id="item_24_brand" data-key="brand" class="description_detail">Бренд: GigaByte</li>
#                   <li id="item_24_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_24_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_24_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 3060</li>
#                   <li id="item_24_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 12288Mb</li>
#                   <li id="item_24_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_24_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 192 Bit</li>
#                   <li id="item_24_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_24_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_24_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_24_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_24_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">32 310 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/24/24_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_25">
#             <div class="img_box product_img_box">
#                <a href="product/25/25_details.html" name="25_img">
#                <img src="images/Видеокарта CBR nVidia GeForce RTX 3060 Terminator T1 PCI-E 12288Mb GDDR6 192 Bit Retail VGA-MSRTX3060-12G-RTL.jpg" alt="Видеокарта CBR nVidia GeForce RTX 3060 Terminator T1 PCI-E 12288Mb GDDR6 192 Bit Retail VGA-MSRTX3060-12G-RTL">
#                </a>
#                <a href="product/25/25_details.html" name="25_name" class="name_item product_name">
#                Видеокарта CBR nVidia GeForce RTX 3060 Terminator T1 PCI-E 12288Mb GDDR6 192 Bit Retail VGA-MSRTX3060-12G-RTL
#                </a>
#                <div class="description product_description">
#                   <li id="item_25_brand" data-key="brand" class="description_detail">Бренд: CBR</li>
#                   <li id="item_25_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_25_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_25_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 3060</li>
#                   <li id="item_25_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 12288Mb</li>
#                   <li id="item_25_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_25_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 192 Bit</li>
#                   <li id="item_25_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_25_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_25_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_25_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_25_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">33 490 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/25/25_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_26">
#             <div class="img_box product_img_box">
#                <a href="product/26/26_details.html" name="26_img">
#                <img src="images/Видеокарта Palit nVidia GeForce RTX 3070 GamingPro LHR PCI-E 8192Mb GDDR6 256 Bit Retail (NE63070019P2-1041A V1).jpg" alt="Видеокарта Palit nVidia GeForce RTX 3070 GamingPro LHR PCI-E 8192Mb GDDR6 256 Bit Retail (NE63070019P2-1041A V1)">
#                </a>
#                <a href="product/26/26_details.html" name="26_name" class="name_item product_name">
#                Видеокарта Palit nVidia GeForce RTX 3070 GamingPro LHR PCI-E 8192Mb GDDR6 256 Bit Retail (NE63070019P2-1041A V1)
#                </a>
#                <div class="description product_description">
#                   <li id="item_26_brand" data-key="brand" class="description_detail">Бренд: Palit</li>
#                   <li id="item_26_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_26_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_26_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 3070</li>
#                   <li id="item_26_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_26_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_26_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 256 Bit</li>
#                   <li id="item_26_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_26_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_26_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_26_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_26_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8+8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">59 980 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/26/26_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_27">
#             <div class="img_box product_img_box">
#                <a href="product/27/27_details.html" name="27_img">
#                <img src="images/Видеокарта Palit nVidia GeForce RTX 4070 JetStream PCI-E 12288Mb GDDR6X 192 Bit Retail NED4070019K9-1047J.jpg" alt="Видеокарта Palit nVidia GeForce RTX 4070 JetStream PCI-E 12288Mb GDDR6X 192 Bit Retail NED4070019K9-1047J">
#                </a>
#                <a href="product/27/27_details.html" name="27_name" class="name_item product_name">
#                Видеокарта Palit nVidia GeForce RTX 4070 JetStream PCI-E 12288Mb GDDR6X 192 Bit Retail NED4070019K9-1047J
#                </a>
#                <div class="description product_description">
#                   <li id="item_27_brand" data-key="brand" class="description_detail">Бренд: Palit</li>
#                   <li id="item_27_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_27_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_27_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4070</li>
#                   <li id="item_27_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 12288Mb</li>
#                   <li id="item_27_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6X</li>
#                   <li id="item_27_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 192 Bit</li>
#                   <li id="item_27_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_27_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_27_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_27_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_27_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">66 900 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/27/27_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_28">
#             <div class="img_box product_img_box">
#                <a href="product/28/28_details.html" name="28_img">
#                <img src="images/Видеокарта Palit nVidia GeForce RTX 4060 Ti DUAL PCI-E 8192Mb GDDR6 128 Bit Retail NE6406T019P1-1060D.jpg" alt="Видеокарта Palit nVidia GeForce RTX 4060 Ti DUAL PCI-E 8192Mb GDDR6 128 Bit Retail NE6406T019P1-1060D">
#                </a>
#                <a href="product/28/28_details.html" name="28_name" class="name_item product_name">
#                Видеокарта Palit nVidia GeForce RTX 4060 Ti DUAL PCI-E 8192Mb GDDR6 128 Bit Retail NE6406T019P1-1060D
#                </a>
#                <div class="description product_description">
#                   <li id="item_28_brand" data-key="brand" class="description_detail">Бренд: Palit</li>
#                   <li id="item_28_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_28_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_28_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4060 Ti</li>
#                   <li id="item_28_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_28_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_28_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_28_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_28_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_28_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_28_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_28_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">47 190 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/28/28_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_29">
#             <div class="img_box product_img_box">
#                <a href="product/29/29_details.html" name="29_img">
#                <img src="images/Видеокарта MSI GeForce GT 710 GT 710 2GD3H LP PCI-E 2048Mb GDDR3 64 Bit Retail (GT 710 2GD3H LP).jpg" alt="Видеокарта MSI GeForce GT 710 GT 710 2GD3H LP PCI-E 2048Mb GDDR3 64 Bit Retail (GT 710 2GD3H LP)">
#                </a>
#                <a href="product/29/29_details.html" name="29_name" class="name_item product_name">
#                Видеокарта MSI GeForce GT 710 GT 710 2GD3H LP PCI-E 2048Mb GDDR3 64 Bit Retail (GT 710 2GD3H LP)
#                </a>
#                <div class="description product_description">
#                   <li id="item_29_brand" data-key="brand" class="description_detail">Бренд: MSI</li>
#                   <li id="item_29_card_type" data-key="card_type" class="description_detail">Тип видеокарты: офисная</li>
#                   <li id="item_29_processor_series" data-key="processor_series" class="description_detail">Серия процессора: GeForce GT 7xx</li>
#                   <li id="item_29_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: GeForce GT 710</li>
#                   <li id="item_29_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 2048Mb</li>
#                   <li id="item_29_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR3</li>
#                   <li id="item_29_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 64 Bit</li>
#                   <li id="item_29_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_29_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 2.0</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">4 960 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/29/29_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_30">
#             <div class="img_box product_img_box">
#                <a href="product/30/30_details.html" name="30_img">
#                <img src="images/Видеокарта GigaByte nVidia GeForce RTX 4060 EAGLE OC PCI-E 8192Mb GDDR6 128 Bit Retail GV-N4060EAGLE OC-8GD.jpg" alt="Видеокарта GigaByte nVidia GeForce RTX 4060 EAGLE OC PCI-E 8192Mb GDDR6 128 Bit Retail GV-N4060EAGLE OC-8GD">
#                </a>
#                <a href="product/30/30_details.html" name="30_name" class="name_item product_name">
#                Видеокарта GigaByte nVidia GeForce RTX 4060 EAGLE OC PCI-E 8192Mb GDDR6 128 Bit Retail GV-N4060EAGLE OC-8GD
#                </a>
#                <div class="description product_description">
#                   <li id="item_30_brand" data-key="brand" class="description_detail">Бренд: GigaByte</li>
#                   <li id="item_30_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_30_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_30_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4060</li>
#                   <li id="item_30_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_30_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_30_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_30_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_30_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_30_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_30_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_30_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">35 280 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/30/30_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_31">
#             <div class="img_box product_img_box">
#                <a href="product/31/31_details.html" name="31_img">
#                <img src="images/Видеокарта Palit nVidia GeForce RTX 3070 GAMINGPRO PCI-E 8192Mb GDDR6 256 Bit Retail.jpg" alt="Видеокарта Palit nVidia GeForce RTX 3070 GAMINGPRO PCI-E 8192Mb GDDR6 256 Bit Retail">
#                </a>
#                <a href="product/31/31_details.html" name="31_name" class="name_item product_name">
#                Видеокарта Palit nVidia GeForce RTX 3070 GAMINGPRO PCI-E 8192Mb GDDR6 256 Bit Retail
#                </a>
#                <div class="description product_description">
#                   <li id="item_31_brand" data-key="brand" class="description_detail">Бренд: Palit</li>
#                   <li id="item_31_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_31_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_31_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 3070</li>
#                   <li id="item_31_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_31_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_31_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 256 Bit</li>
#                   <li id="item_31_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_31_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_31_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_31_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_31_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8+8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">59 710 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/31/31_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_32">
#             <div class="img_box product_img_box">
#                <a href="product/32/32_details.html" name="32_img">
#                <img src="images/Видеокарта Afox GeForce GT 210 AF210-1024D2LG2 PCI-E 1024Mb DDR2 64 Bit Retail.jpg" alt="Видеокарта Afox GeForce GT 210 AF210-1024D2LG2 PCI-E 1024Mb DDR2 64 Bit Retail">
#                </a>
#                <a href="product/32/32_details.html" name="32_name" class="name_item product_name">
#                Видеокарта Afox GeForce GT 210 AF210-1024D2LG2 PCI-E 1024Mb DDR2 64 Bit Retail
#                </a>
#                <div class="description product_description">
#                   <li id="item_32_brand" data-key="brand" class="description_detail">Бренд: Afox</li>
#                   <li id="item_32_card_type" data-key="card_type" class="description_detail">Тип видеокарты: офисная</li>
#                   <li id="item_32_processor_series" data-key="processor_series" class="description_detail">Серия процессора: GeForce GT 2xx</li>
#                   <li id="item_32_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: GeForce GT 210</li>
#                   <li id="item_32_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 1024Mb</li>
#                   <li id="item_32_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: DDR2</li>
#                   <li id="item_32_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 64 Bit</li>
#                   <li id="item_32_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_32_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 2.0</li>
#                   <li id="item_32_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_32_Разъём DVI" data-key="Разъём DVI" class="description_detail">Разъём DVI: есть</li>
#                   <li id="item_32_Выход VGA" data-key="Выход VGA" class="description_detail">Выход VGA: есть</li>
#                   <li id="item_32_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 0 (нет)</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">2 640 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/32/32_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_33">
#             <div class="img_box product_img_box">
#                <a href="product/33/33_details.html" name="33_img">
#                <img src="images/Видеокарта GigaByte Radeon RX 7600 GAMING OC PCI-E 8192Mb GDDR6 128 Bit Retail GV-R76GAMING OC-8GD.jpg" alt="Видеокарта GigaByte Radeon RX 7600 GAMING OC PCI-E 8192Mb GDDR6 128 Bit Retail GV-R76GAMING OC-8GD">
#                </a>
#                <a href="product/33/33_details.html" name="33_name" class="name_item product_name">
#                Видеокарта GigaByte Radeon RX 7600 GAMING OC PCI-E 8192Mb GDDR6 128 Bit Retail GV-R76GAMING OC-8GD
#                </a>
#                <div class="description product_description">
#                   <li id="item_33_brand" data-key="brand" class="description_detail">Бренд: GigaByte</li>
#                   <li id="item_33_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_33_processor_series" data-key="processor_series" class="description_detail">Серия процессора: Radeon RX</li>
#                   <li id="item_33_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: Radeon RX 7600</li>
#                   <li id="item_33_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_33_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_33_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_33_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_33_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_33_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_33_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_33_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">34 440 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/33/33_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_34">
#             <div class="img_box product_img_box">
#                <a href="product/34/34_details.html" name="34_img">
#                <img src="images/Видеокарта Palit nVidia GeForce RTX 3060 Dual OC PCI-E 12288Mb GDDR6 192 Bit Retail (NE63060T19K9-190AD).jpg" alt="Видеокарта Palit nVidia GeForce RTX 3060 Dual OC PCI-E 12288Mb GDDR6 192 Bit Retail (NE63060T19K9-190AD)">
#                </a>
#                <a href="product/34/34_details.html" name="34_name" class="name_item product_name">
#                Видеокарта Palit nVidia GeForce RTX 3060 Dual OC PCI-E 12288Mb GDDR6 192 Bit Retail (NE63060T19K9-190AD)
#                </a>
#                <div class="description product_description">
#                   <li id="item_34_brand" data-key="brand" class="description_detail">Бренд: Palit</li>
#                   <li id="item_34_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_34_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_34_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 3060</li>
#                   <li id="item_34_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 12288Mb</li>
#                   <li id="item_34_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_34_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 192 Bit</li>
#                   <li id="item_34_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_34_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_34_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_34_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_34_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">33 260 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/34/34_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_35">
#             <div class="img_box product_img_box">
#                <a href="product/35/35_details.html" name="35_img">
#                <img src="images/Видеокарта Palit GeForce GTX 1650 GP PCI-E 4096Mb GDDR6 128 Bit Bulk (NE6165001BG1-1175A).jpg" alt="Видеокарта Palit GeForce GTX 1650 GP PCI-E 4096Mb GDDR6 128 Bit Bulk (NE6165001BG1-1175A)">
#                </a>
#                <a href="product/35/35_details.html" name="35_name" class="name_item product_name">
#                Видеокарта Palit GeForce GTX 1650 GP PCI-E 4096Mb GDDR6 128 Bit Bulk (NE6165001BG1-1175A)
#                </a>
#                <div class="description product_description">
#                   <li id="item_35_brand" data-key="brand" class="description_detail">Бренд: Palit</li>
#                   <li id="item_35_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_35_processor_series" data-key="processor_series" class="description_detail">Серия процессора: GeForce GTX 16хх</li>
#                   <li id="item_35_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: GeForce GTX 1650</li>
#                   <li id="item_35_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 4096Mb</li>
#                   <li id="item_35_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_35_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_35_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_35_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 3.0</li>
#                   <li id="item_35_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_35_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_35_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 6</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">20 280 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/35/35_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#       </div>
#
# </body></html>
# '''
#
# def get_html(html):
#     soup = BeautifulSoup(html, 'html.parser')
#
#     prices = soup.find_all('p', attrs={'class': 'price product_price'})
#
#     count = 0
#     for price in prices:
#         str1 = str(price.text).replace("руб", "").replace(" ", "")
#         count += int(str1)
#
#     return count
# print(get_html(html))

# __________________________________________
# Задача: Проанализируйте страницу и найдите способ извлечь все ID из каждого тега <li>(используйте select() или find_all()).

# html = '''
# <html><head>
#       <title>Каталог продуктов</title>
#       <link rel="stylesheet" href="styles.css">
#       <meta charset="UTF-8">
#    </head>
#    <body>
#       <div class="item_card">
#          <div class="item product_item" id="item_1">
#             <div class="img_box product_img_box">
#                <a href="product/1/1_details.html" name="1_img">
#                <img src="images/Видеокарта MSI Radeon RX 6650 XT MECH 2X OC PCI-E 8192Mb GDDR6 128 Bit Retail.jpg" alt="Видеокарта MSI Radeon RX 6650 XT MECH 2X OC PCI-E 8192Mb GDDR6 128 Bit Retail">
#                </a>
#                <a href="product/1/1_details.html" name="1_name" class="name_item product_name">
#                Видеокарта MSI Radeon RX 6650 XT MECH 2X OC PCI-E 8192Mb GDDR6 128 Bit Retail
#                </a>
#                <div class="description product_description">
#                   <li id="item_1_brand" data-key="brand" class="description_detail">Бренд: MSI</li>
#                   <li id="item_1_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_1_processor_series" data-key="processor_series" class="description_detail">Серия процессора: Radeon RX</li>
#                   <li id="item_1_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: Radeon RX 6650 XT</li>
#                   <li id="item_1_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_1_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_1_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_1_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_1_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_1_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_1_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_1_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">29 040 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/1/1_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_2">
#             <div class="img_box product_img_box">
#                <a href="product/2/2_details.html" name="2_img">
#                <img src="images/Видеокарта GigaByte nVidia GeForce RTX 3050 WINDFORCE OC 8G PCI-E 8192Mb GDDR6 128 Bit Retail GV-N3050WF2OC-8GD.jpg" alt="Видеокарта GigaByte nVidia GeForce RTX 3050 WINDFORCE OC 8G PCI-E 8192Mb GDDR6 128 Bit Retail GV-N3050WF2OC-8GD">
#                </a>
#                <a href="product/2/2_details.html" name="2_name" class="name_item product_name">
#                Видеокарта GigaByte nVidia GeForce RTX 3050 WINDFORCE OC 8G PCI-E 8192Mb GDDR6 128 Bit Retail GV-N3050WF2OC-8GD
#                </a>
#                <div class="description product_description">
#                   <li id="item_2_brand" data-key="brand" class="description_detail">Бренд: GigaByte</li>
#                   <li id="item_2_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_2_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_2_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 3050</li>
#                   <li id="item_2_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_2_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_2_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_2_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_2_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_2_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_2_Разъём DVI" data-key="Разъём DVI" class="description_detail">Разъём DVI: есть</li>
#                   <li id="item_2_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_2_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">27 840 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/2/2_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_3">
#             <div class="img_box product_img_box">
#                <a href="product/3/3_details.html" name="3_img">
#                <img src="images/Видеокарта Palit nVidia GeForce RTX 4070 GamingPro PCI-E 12288Mb GDDR6X 192 Bit Retail NED4070019K9-1043A.jpg" alt="Видеокарта Palit nVidia GeForce RTX 4070 GamingPro PCI-E 12288Mb GDDR6X 192 Bit Retail NED4070019K9-1043A">
#                </a>
#                <a href="product/3/3_details.html" name="3_name" class="name_item product_name">
#                Видеокарта Palit nVidia GeForce RTX 4070 GamingPro PCI-E 12288Mb GDDR6X 192 Bit Retail NED4070019K9-1043A
#                </a>
#                <div class="description product_description">
#                   <li id="item_3_brand" data-key="brand" class="description_detail">Бренд: Palit</li>
#                   <li id="item_3_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_3_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_3_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4070</li>
#                   <li id="item_3_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 12288Mb</li>
#                   <li id="item_3_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6X</li>
#                   <li id="item_3_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 192 Bit</li>
#                   <li id="item_3_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_3_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_3_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_3_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_3_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 16</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">68 490 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/3/3_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_4">
#             <div class="img_box product_img_box">
#                <a href="product/4/4_details.html" name="4_img">
#                <img src="images/Видеокарта MSI nVidia GeForce RTX 3060 GAMING X LHR PCI-E 12288Mb GDDR6 192 Bit Retail (RTX 3060 GAMING X 12G).jpg" alt="Видеокарта MSI nVidia GeForce RTX 3060 GAMING X LHR PCI-E 12288Mb GDDR6 192 Bit Retail (RTX 3060 GAMING X 12G)">
#                </a>
#                <a href="product/4/4_details.html" name="4_name" class="name_item product_name">
#                Видеокарта MSI nVidia GeForce RTX 3060 GAMING X LHR PCI-E 12288Mb GDDR6 192 Bit Retail (RTX 3060 GAMING X 12G)
#                </a>
#                <div class="description product_description">
#                   <li id="item_4_brand" data-key="brand" class="description_detail">Бренд: MSI</li>
#                   <li id="item_4_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_4_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_4_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 3060</li>
#                   <li id="item_4_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 12288Mb</li>
#                   <li id="item_4_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_4_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 192 Bit</li>
#                   <li id="item_4_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_4_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_4_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_4_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_4_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8+6</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">41 280 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/4/4_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_5">
#             <div class="img_box product_img_box">
#                <a href="product/5/5_details.html" name="5_img">
#                <img src="images/Видеокарта MSI nVidia GeForce RTX 4060 Ti GAMING X PCI-E 8192Mb GDDR6 128 Bit Retail.jpg" alt="Видеокарта MSI nVidia GeForce RTX 4060 Ti GAMING X PCI-E 8192Mb GDDR6 128 Bit Retail">
#                </a>
#                <a href="product/5/5_details.html" name="5_name" class="name_item product_name">
#                Видеокарта MSI nVidia GeForce RTX 4060 Ti GAMING X PCI-E 8192Mb GDDR6 128 Bit Retail
#                </a>
#                <div class="description product_description">
#                   <li id="item_5_brand" data-key="brand" class="description_detail">Бренд: MSI</li>
#                   <li id="item_5_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_5_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_5_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4060 Ti</li>
#                   <li id="item_5_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_5_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_5_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_5_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_5_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_5_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_5_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_5_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">48 720 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/5/5_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_6">
#             <div class="img_box product_img_box">
#                <a href="product/6/6_details.html" name="6_img">
#                <img src="images/Видеокарта MSI nVidia GeForce RTX 4060 Ti GAMING X TRIO PCI-E 8192Mb GDDR6 128 Bit Retail.jpg" alt="Видеокарта MSI nVidia GeForce RTX 4060 Ti GAMING X TRIO PCI-E 8192Mb GDDR6 128 Bit Retail">
#                </a>
#                <a href="product/6/6_details.html" name="6_name" class="name_item product_name">
#                Видеокарта MSI nVidia GeForce RTX 4060 Ti GAMING X TRIO PCI-E 8192Mb GDDR6 128 Bit Retail
#                </a>
#                <div class="description product_description">
#                   <li id="item_6_brand" data-key="brand" class="description_detail">Бренд: MSI</li>
#                   <li id="item_6_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_6_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_6_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4060 Ti</li>
#                   <li id="item_6_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_6_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_6_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_6_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_6_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_6_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_6_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_6_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">52 500 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/6/6_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_7">
#             <div class="img_box product_img_box">
#                <a href="product/7/7_details.html" name="7_img">
#                <img src="images/Видеокарта Palit nVidia GeForce RTX 4060 Dual OC PCI-E 8192Mb GDDR6 128 Bit Retail NE64060T19P1-1070D.jpg" alt="Видеокарта Palit nVidia GeForce RTX 4060 Dual OC PCI-E 8192Mb GDDR6 128 Bit Retail NE64060T19P1-1070D">
#                </a>
#                <a href="product/7/7_details.html" name="7_name" class="name_item product_name">
#                Видеокарта Palit nVidia GeForce RTX 4060 Dual OC PCI-E 8192Mb GDDR6 128 Bit Retail NE64060T19P1-1070D
#                </a>
#                <div class="description product_description">
#                   <li id="item_7_brand" data-key="brand" class="description_detail">Бренд: Palit</li>
#                   <li id="item_7_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_7_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_7_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4060</li>
#                   <li id="item_7_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_7_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_7_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_7_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_7_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_7_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_7_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_7_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">35 520 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/7/7_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_8">
#             <div class="img_box product_img_box">
#                <a href="product/8/8_details.html" name="8_img">
#                <img src="images/Видеокарта Palit nVidia GeForce RTX 4060 StormX PCI-E 8192Mb GDDR6 128 Bit Retail NE64060019P1-1070F.jpg" alt="Видеокарта Palit nVidia GeForce RTX 4060 StormX PCI-E 8192Mb GDDR6 128 Bit Retail NE64060019P1-1070F">
#                </a>
#                <a href="product/8/8_details.html" name="8_name" class="name_item product_name">
#                Видеокарта Palit nVidia GeForce RTX 4060 StormX PCI-E 8192Mb GDDR6 128 Bit Retail NE64060019P1-1070F
#                </a>
#                <div class="description product_description">
#                   <li id="item_8_brand" data-key="brand" class="description_detail">Бренд: Palit</li>
#                   <li id="item_8_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_8_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_8_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4060</li>
#                   <li id="item_8_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_8_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_8_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_8_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_8_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_8_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_8_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_8_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">34 720 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/8/8_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_9">
#             <div class="img_box product_img_box">
#                <a href="product/9/9_details.html" name="9_img">
#                <img src="images/Видеокарта Palit nVidia GeForce RTX 4060 DUAL PCI-E 8192Mb GDDR6 128 Bit Retail NE64060019P1-1070D.jpg" alt="Видеокарта Palit nVidia GeForce RTX 4060 DUAL PCI-E 8192Mb GDDR6 128 Bit Retail NE64060019P1-1070D">
#                </a>
#                <a href="product/9/9_details.html" name="9_name" class="name_item product_name">
#                Видеокарта Palit nVidia GeForce RTX 4060 DUAL PCI-E 8192Mb GDDR6 128 Bit Retail NE64060019P1-1070D
#                </a>
#                <div class="description product_description">
#                   <li id="item_9_brand" data-key="brand" class="description_detail">Бренд: Palit</li>
#                   <li id="item_9_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_9_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_9_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4060</li>
#                   <li id="item_9_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_9_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_9_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_9_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_9_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_9_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_9_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_9_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">33 580 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/9/9_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_10">
#             <div class="img_box product_img_box">
#                <a href="product/10/10_details.html" name="10_img">
#                <img src="images/Видеокарта MSI nVidia GeForce RTX 4060 Ti GAMING X SLIM 16G PCI-E 16384Mb GDDR6 128 Bit Retail.jpg" alt="Видеокарта MSI nVidia GeForce RTX 4060 Ti GAMING X SLIM 16G PCI-E 16384Mb GDDR6 128 Bit Retail">
#                </a>
#                <a href="product/10/10_details.html" name="10_name" class="name_item product_name">
#                Видеокарта MSI nVidia GeForce RTX 4060 Ti GAMING X SLIM 16G PCI-E 16384Mb GDDR6 128 Bit Retail
#                </a>
#                <div class="description product_description">
#                   <li id="item_10_brand" data-key="brand" class="description_detail">Бренд: MSI</li>
#                   <li id="item_10_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_10_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_10_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4060 Ti</li>
#                   <li id="item_10_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 16384Mb</li>
#                   <li id="item_10_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_10_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_10_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_10_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_10_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_10_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_10_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">55 950 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/10/10_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_11">
#             <div class="img_box product_img_box">
#                <a href="product/11/11_details.html" name="11_img">
#                <img src="images/Видеокарта MSI nVidia GeForce RTX 4060 Ti VENTUS 3X 16G OC PCI-E 16384Mb GDDR6 128 Bit Retail.jpg" alt="Видеокарта MSI nVidia GeForce RTX 4060 Ti VENTUS 3X 16G OC PCI-E 16384Mb GDDR6 128 Bit Retail">
#                </a>
#                <a href="product/11/11_details.html" name="11_name" class="name_item product_name">
#                Видеокарта MSI nVidia GeForce RTX 4060 Ti VENTUS 3X 16G OC PCI-E 16384Mb GDDR6 128 Bit Retail
#                </a>
#                <div class="description product_description">
#                   <li id="item_11_brand" data-key="brand" class="description_detail">Бренд: MSI</li>
#                   <li id="item_11_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_11_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_11_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4060 Ti</li>
#                   <li id="item_11_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 16384Mb</li>
#                   <li id="item_11_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_11_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_11_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_11_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_11_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_11_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_11_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">52 260 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/11/11_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_12">
#             <div class="img_box product_img_box">
#                <a href="product/12/12_details.html" name="12_img">
#                <img src="images/Видеокарта Maxsun nVidia GeForce RTX 4060 Ti iCraft OC PCI-E 8192Mb GDDR6 128 Bit Retail.jpg" alt="Видеокарта Maxsun nVidia GeForce RTX 4060 Ti iCraft OC PCI-E 8192Mb GDDR6 128 Bit Retail">
#                </a>
#                <a href="product/12/12_details.html" name="12_name" class="name_item product_name">
#                Видеокарта Maxsun nVidia GeForce RTX 4060 Ti iCraft OC PCI-E 8192Mb GDDR6 128 Bit Retail
#                </a>
#                <div class="description product_description">
#                   <li id="item_12_brand" data-key="brand" class="description_detail">Бренд: Maxsun</li>
#                   <li id="item_12_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_12_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_12_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4060 Ti</li>
#                   <li id="item_12_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_12_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_12_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_12_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_12_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_12_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_12_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_12_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">45 350 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/12/12_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_13">
#             <div class="img_box product_img_box">
#                <a href="product/13/13_details.html" name="13_img">
#                <img src="images/Видеокарта GigaByte nVidia GeForce RTX 4070 Ti GAMING PCI-E 12288Mb GDDR6X 192 Bit Retail GV-N407TGAMING-12GD.jpg" alt="Видеокарта GigaByte nVidia GeForce RTX 4070 Ti GAMING PCI-E 12288Mb GDDR6X 192 Bit Retail GV-N407TGAMING-12GD">
#                </a>
#                <a href="product/13/13_details.html" name="13_name" class="name_item product_name">
#                Видеокарта GigaByte nVidia GeForce RTX 4070 Ti GAMING PCI-E 12288Mb GDDR6X 192 Bit Retail GV-N407TGAMING-12GD
#                </a>
#                <div class="description product_description">
#                   <li id="item_13_brand" data-key="brand" class="description_detail">Бренд: GigaByte</li>
#                   <li id="item_13_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_13_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_13_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4070 Ti</li>
#                   <li id="item_13_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 12288Mb</li>
#                   <li id="item_13_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6X</li>
#                   <li id="item_13_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 192 Bit</li>
#                   <li id="item_13_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_13_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_13_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_13_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_13_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 16</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">89 040 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/13/13_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_14">
#             <div class="img_box product_img_box">
#                <a href="product/14/14_details.html" name="14_img">
#                <img src="images/Видеокарта Palit nVidia GeForce RTX 4070 Ti GamingPro White OC PCI-E 12288Mb GDDR6X 192 Bit Retail NED407TV19K9-1043W.jpg" alt="Видеокарта Palit nVidia GeForce RTX 4070 Ti GamingPro White OC PCI-E 12288Mb GDDR6X 192 Bit Retail NED407TV19K9-1043W">
#                </a>
#                <a href="product/14/14_details.html" name="14_name" class="name_item product_name">
#                Видеокарта Palit nVidia GeForce RTX 4070 Ti GamingPro White OC PCI-E 12288Mb GDDR6X 192 Bit Retail NED407TV19K9-1043W
#                </a>
#                <div class="description product_description">
#                   <li id="item_14_brand" data-key="brand" class="description_detail">Бренд: Palit</li>
#                   <li id="item_14_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_14_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_14_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4070 Ti</li>
#                   <li id="item_14_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 12288Mb</li>
#                   <li id="item_14_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6X</li>
#                   <li id="item_14_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 192 Bit</li>
#                   <li id="item_14_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_14_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_14_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_14_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_14_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 16</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">89 620 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/14/14_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_15">
#             <div class="img_box product_img_box">
#                <a href="product/15/15_details.html" name="15_img">
#                <img src="images/Видеокарта ASUS nVidia GeForce RTX 4070 Ti TUF GAMING PCI-E 12288Mb GDDR6X 192 Bit Retail TUF-RTX4070TI-12G-GAMING.jpg" alt="Видеокарта ASUS nVidia GeForce RTX 4070 Ti TUF GAMING PCI-E 12288Mb GDDR6X 192 Bit Retail TUF-RTX4070TI-12G-GAMING">
#                </a>
#                <a href="product/15/15_details.html" name="15_name" class="name_item product_name">
#                Видеокарта ASUS nVidia GeForce RTX 4070 Ti TUF GAMING PCI-E 12288Mb GDDR6X 192 Bit Retail TUF-RTX4070TI-12G-GAMING
#                </a>
#                <div class="description product_description">
#                   <li id="item_15_brand" data-key="brand" class="description_detail">Бренд: ASUS</li>
#                   <li id="item_15_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_15_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_15_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4070 Ti</li>
#                   <li id="item_15_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 12288Mb</li>
#                   <li id="item_15_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6X</li>
#                   <li id="item_15_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 192 Bit</li>
#                   <li id="item_15_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_15_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_15_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_15_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_15_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 16</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">100 580 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/15/15_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_16">
#             <div class="img_box product_img_box">
#                <a href="product/16/16_details.html" name="16_img">
#                <img src="images/Видеокарта GigaByte nVidia GeForce RTX 4070 WINDFORCE OC PCI-E 12288Mb GDDR6X 192 Bit Retail GV-N4070WF3OC-12GD.jpg" alt="Видеокарта GigaByte nVidia GeForce RTX 4070 WINDFORCE OC PCI-E 12288Mb GDDR6X 192 Bit Retail GV-N4070WF3OC-12GD">
#                </a>
#                <a href="product/16/16_details.html" name="16_name" class="name_item product_name">
#                Видеокарта GigaByte nVidia GeForce RTX 4070 WINDFORCE OC PCI-E 12288Mb GDDR6X 192 Bit Retail GV-N4070WF3OC-12GD
#                </a>
#                <div class="description product_description">
#                   <li id="item_16_brand" data-key="brand" class="description_detail">Бренд: GigaByte</li>
#                   <li id="item_16_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_16_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_16_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4070</li>
#                   <li id="item_16_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 12288Mb</li>
#                   <li id="item_16_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6X</li>
#                   <li id="item_16_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 192 Bit</li>
#                   <li id="item_16_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_16_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_16_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_16_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_16_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">68 590 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/16/16_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_17">
#             <div class="img_box product_img_box">
#                <a href="product/17/17_details.html" name="17_img">
#                <img src="images/Видеокарта ASUS nVidia GeForce RTX 3060 Dual V2 OC Edition PCI-E 12288Mb GDDR6 192 Bit Retail.jpg" alt="Видеокарта ASUS nVidia GeForce RTX 3060 Dual V2 OC Edition PCI-E 12288Mb GDDR6 192 Bit Retail">
#                </a>
#                <a href="product/17/17_details.html" name="17_name" class="name_item product_name">
#                Видеокарта ASUS nVidia GeForce RTX 3060 Dual V2 OC Edition PCI-E 12288Mb GDDR6 192 Bit Retail
#                </a>
#                <div class="description product_description">
#                   <li id="item_17_brand" data-key="brand" class="description_detail">Бренд: ASUS</li>
#                   <li id="item_17_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_17_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_17_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 3060</li>
#                   <li id="item_17_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 12288Mb</li>
#                   <li id="item_17_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_17_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 192 Bit</li>
#                   <li id="item_17_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_17_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_17_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_17_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_17_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">41 350 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/17/17_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_18">
#             <div class="img_box product_img_box">
#                <a href="product/18/18_details.html" name="18_img">
#                <img src="images/Видеокарта Palit nVidia GeForce RTX 4070 Dual PCI-E 12288Mb GDDR6X 192 Bit Retail NED4070019K9-1047D.jpg" alt="Видеокарта Palit nVidia GeForce RTX 4070 Dual PCI-E 12288Mb GDDR6X 192 Bit Retail NED4070019K9-1047D">
#                </a>
#                <a href="product/18/18_details.html" name="18_name" class="name_item product_name">
#                Видеокарта Palit nVidia GeForce RTX 4070 Dual PCI-E 12288Mb GDDR6X 192 Bit Retail NED4070019K9-1047D
#                </a>
#                <div class="description product_description">
#                   <li id="item_18_brand" data-key="brand" class="description_detail">Бренд: Palit</li>
#                   <li id="item_18_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_18_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_18_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4070</li>
#                   <li id="item_18_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 12288Mb</li>
#                   <li id="item_18_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6X</li>
#                   <li id="item_18_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 192 Bit</li>
#                   <li id="item_18_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_18_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_18_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_18_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_18_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">62 500 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/18/18_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_19">
#             <div class="img_box product_img_box">
#                <a href="product/19/19_details.html" name="19_img">
#                <img src="images/Видеокарта ASUS Radeon RX 6700 XT DUAL PCI-E 12288Mb GDDR6 192 Bit Retail (DUAL-RX6700XT-12G).jpg" alt="Видеокарта ASUS Radeon RX 6700 XT DUAL PCI-E 12288Mb GDDR6 192 Bit Retail (DUAL-RX6700XT-12G)">
#                </a>
#                <a href="product/19/19_details.html" name="19_name" class="name_item product_name">
#                Видеокарта ASUS Radeon RX 6700 XT DUAL PCI-E 12288Mb GDDR6 192 Bit Retail (DUAL-RX6700XT-12G)
#                </a>
#                <div class="description product_description">
#                   <li id="item_19_brand" data-key="brand" class="description_detail">Бренд: ASUS</li>
#                   <li id="item_19_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_19_processor_series" data-key="processor_series" class="description_detail">Серия процессора: Radeon RX</li>
#                   <li id="item_19_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: Radeon RX 6700 XT</li>
#                   <li id="item_19_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 12288Mb</li>
#                   <li id="item_19_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_19_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 192 Bit</li>
#                   <li id="item_19_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_19_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_19_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_19_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_19_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8+6</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">44 210 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/19/19_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_20">
#             <div class="img_box product_img_box">
#                <a href="product/20/20_details.html" name="20_img">
#                <img src="images/Видеокарта GigaByte nVidia GeForce RTX 3070 GAMING OC LHR PCI-E 8192Mb GDDR6 256 Bit Retail (GV-N3070GAMING OC-8GD 2.0).jpg" alt="Видеокарта GigaByte nVidia GeForce RTX 3070 GAMING OC LHR PCI-E 8192Mb GDDR6 256 Bit Retail (GV-N3070GAMING OC-8GD 2.0)">
#                </a>
#                <a href="product/20/20_details.html" name="20_name" class="name_item product_name">
#                Видеокарта GigaByte nVidia GeForce RTX 3070 GAMING OC LHR PCI-E 8192Mb GDDR6 256 Bit Retail (GV-N3070GAMING OC-8GD 2.0)
#                </a>
#                <div class="description product_description">
#                   <li id="item_20_brand" data-key="brand" class="description_detail">Бренд: GigaByte</li>
#                   <li id="item_20_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_20_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_20_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 3070</li>
#                   <li id="item_20_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_20_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_20_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 256 Bit</li>
#                   <li id="item_20_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_20_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_20_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_20_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_20_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8+6</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">56 890 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/20/20_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_21">
#             <div class="img_box product_img_box">
#                <a href="product/21/21_details.html" name="21_img">
#                <img src="images/Видеокарта Palit nVidia GeForce RTX 4070 GamingPro OC PCI-E 12288Mb GDDR6X 192 Bit Retail NED4070H19K9-1043A.jpg" alt="Видеокарта Palit nVidia GeForce RTX 4070 GamingPro OC PCI-E 12288Mb GDDR6X 192 Bit Retail NED4070H19K9-1043A">
#                </a>
#                <a href="product/21/21_details.html" name="21_name" class="name_item product_name">
#                Видеокарта Palit nVidia GeForce RTX 4070 GamingPro OC PCI-E 12288Mb GDDR6X 192 Bit Retail NED4070H19K9-1043A
#                </a>
#                <div class="description product_description">
#                   <li id="item_21_brand" data-key="brand" class="description_detail">Бренд: Palit</li>
#                   <li id="item_21_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_21_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_21_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4070</li>
#                   <li id="item_21_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 12288Mb</li>
#                   <li id="item_21_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6X</li>
#                   <li id="item_21_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 192 Bit</li>
#                   <li id="item_21_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_21_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_21_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_21_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_21_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 16</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">70 020 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/21/21_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_22">
#             <div class="img_box product_img_box">
#                <a href="product/22/22_details.html" name="22_img">
#                <img src="images/Видеокарта MSI nVidia GeForce RTX 3050 AERO ITX 8G OC PCI-E 8192Mb GDDR6 128 Bit Retail.jpg" alt="Видеокарта MSI nVidia GeForce RTX 3050 AERO ITX 8G OC PCI-E 8192Mb GDDR6 128 Bit Retail">
#                </a>
#                <a href="product/22/22_details.html" name="22_name" class="name_item product_name">
#                Видеокарта MSI nVidia GeForce RTX 3050 AERO ITX 8G OC PCI-E 8192Mb GDDR6 128 Bit Retail
#                </a>
#                <div class="description product_description">
#                   <li id="item_22_brand" data-key="brand" class="description_detail">Бренд: MSI</li>
#                   <li id="item_22_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_22_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_22_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 3050</li>
#                   <li id="item_22_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_22_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_22_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_22_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_22_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_22_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_22_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_22_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">27 610 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/22/22_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_23">
#             <div class="img_box product_img_box">
#                <a href="product/23/23_details.html" name="23_img">
#                <img src="images/Видеокарта MSI nVidia GeForce RTX 3060 Ti VENTUS 2X OCV1 LHR PCI-E 8192Mb GDDR6 256 Bit Retail (3060 Ti VENTUS 2X 8G OCV1 LHR).jpg" alt="Видеокарта MSI nVidia GeForce RTX 3060 Ti VENTUS 2X OCV1 LHR PCI-E 8192Mb GDDR6 256 Bit Retail (3060 Ti VENTUS 2X 8G OCV1 LHR)">
#                </a>
#                <a href="product/23/23_details.html" name="23_name" class="name_item product_name">
#                Видеокарта MSI nVidia GeForce RTX 3060 Ti VENTUS 2X OCV1 LHR PCI-E 8192Mb GDDR6 256 Bit Retail (3060 Ti VENTUS 2X 8G OCV1 LHR)
#                </a>
#                <div class="description product_description">
#                   <li id="item_23_brand" data-key="brand" class="description_detail">Бренд: MSI</li>
#                   <li id="item_23_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_23_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_23_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 3060 Ti</li>
#                   <li id="item_23_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_23_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_23_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 256 Bit</li>
#                   <li id="item_23_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_23_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_23_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_23_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_23_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">46 000 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/23/23_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_24">
#             <div class="img_box product_img_box">
#                <a href="product/24/24_details.html" name="24_img">
#                <img src="images/Видеокарта GigaByte nVidia GeForce RTX 3060 WINDFORCE OC PCI-E 12288Mb GDDR6 192 Bit Retail GV-N3060WF2OC-12GD 2.0.jpg" alt="Видеокарта GigaByte nVidia GeForce RTX 3060 WINDFORCE OC PCI-E 12288Mb GDDR6 192 Bit Retail GV-N3060WF2OC-12GD 2.0">
#                </a>
#                <a href="product/24/24_details.html" name="24_name" class="name_item product_name">
#                Видеокарта GigaByte nVidia GeForce RTX 3060 WINDFORCE OC PCI-E 12288Mb GDDR6 192 Bit Retail GV-N3060WF2OC-12GD 2.0
#                </a>
#                <div class="description product_description">
#                   <li id="item_24_brand" data-key="brand" class="description_detail">Бренд: GigaByte</li>
#                   <li id="item_24_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_24_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_24_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 3060</li>
#                   <li id="item_24_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 12288Mb</li>
#                   <li id="item_24_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_24_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 192 Bit</li>
#                   <li id="item_24_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_24_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_24_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_24_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_24_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">32 310 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/24/24_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_25">
#             <div class="img_box product_img_box">
#                <a href="product/25/25_details.html" name="25_img">
#                <img src="images/Видеокарта CBR nVidia GeForce RTX 3060 Terminator T1 PCI-E 12288Mb GDDR6 192 Bit Retail VGA-MSRTX3060-12G-RTL.jpg" alt="Видеокарта CBR nVidia GeForce RTX 3060 Terminator T1 PCI-E 12288Mb GDDR6 192 Bit Retail VGA-MSRTX3060-12G-RTL">
#                </a>
#                <a href="product/25/25_details.html" name="25_name" class="name_item product_name">
#                Видеокарта CBR nVidia GeForce RTX 3060 Terminator T1 PCI-E 12288Mb GDDR6 192 Bit Retail VGA-MSRTX3060-12G-RTL
#                </a>
#                <div class="description product_description">
#                   <li id="item_25_brand" data-key="brand" class="description_detail">Бренд: CBR</li>
#                   <li id="item_25_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_25_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_25_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 3060</li>
#                   <li id="item_25_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 12288Mb</li>
#                   <li id="item_25_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_25_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 192 Bit</li>
#                   <li id="item_25_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_25_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_25_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_25_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_25_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">33 490 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/25/25_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_26">
#             <div class="img_box product_img_box">
#                <a href="product/26/26_details.html" name="26_img">
#                <img src="images/Видеокарта Palit nVidia GeForce RTX 3070 GamingPro LHR PCI-E 8192Mb GDDR6 256 Bit Retail (NE63070019P2-1041A V1).jpg" alt="Видеокарта Palit nVidia GeForce RTX 3070 GamingPro LHR PCI-E 8192Mb GDDR6 256 Bit Retail (NE63070019P2-1041A V1)">
#                </a>
#                <a href="product/26/26_details.html" name="26_name" class="name_item product_name">
#                Видеокарта Palit nVidia GeForce RTX 3070 GamingPro LHR PCI-E 8192Mb GDDR6 256 Bit Retail (NE63070019P2-1041A V1)
#                </a>
#                <div class="description product_description">
#                   <li id="item_26_brand" data-key="brand" class="description_detail">Бренд: Palit</li>
#                   <li id="item_26_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_26_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_26_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 3070</li>
#                   <li id="item_26_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_26_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_26_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 256 Bit</li>
#                   <li id="item_26_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_26_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_26_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_26_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_26_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8+8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">59 980 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/26/26_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_27">
#             <div class="img_box product_img_box">
#                <a href="product/27/27_details.html" name="27_img">
#                <img src="images/Видеокарта Palit nVidia GeForce RTX 4070 JetStream PCI-E 12288Mb GDDR6X 192 Bit Retail NED4070019K9-1047J.jpg" alt="Видеокарта Palit nVidia GeForce RTX 4070 JetStream PCI-E 12288Mb GDDR6X 192 Bit Retail NED4070019K9-1047J">
#                </a>
#                <a href="product/27/27_details.html" name="27_name" class="name_item product_name">
#                Видеокарта Palit nVidia GeForce RTX 4070 JetStream PCI-E 12288Mb GDDR6X 192 Bit Retail NED4070019K9-1047J
#                </a>
#                <div class="description product_description">
#                   <li id="item_27_brand" data-key="brand" class="description_detail">Бренд: Palit</li>
#                   <li id="item_27_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_27_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_27_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4070</li>
#                   <li id="item_27_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 12288Mb</li>
#                   <li id="item_27_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6X</li>
#                   <li id="item_27_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 192 Bit</li>
#                   <li id="item_27_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_27_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_27_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_27_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_27_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">66 900 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/27/27_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_28">
#             <div class="img_box product_img_box">
#                <a href="product/28/28_details.html" name="28_img">
#                <img src="images/Видеокарта Palit nVidia GeForce RTX 4060 Ti DUAL PCI-E 8192Mb GDDR6 128 Bit Retail NE6406T019P1-1060D.jpg" alt="Видеокарта Palit nVidia GeForce RTX 4060 Ti DUAL PCI-E 8192Mb GDDR6 128 Bit Retail NE6406T019P1-1060D">
#                </a>
#                <a href="product/28/28_details.html" name="28_name" class="name_item product_name">
#                Видеокарта Palit nVidia GeForce RTX 4060 Ti DUAL PCI-E 8192Mb GDDR6 128 Bit Retail NE6406T019P1-1060D
#                </a>
#                <div class="description product_description">
#                   <li id="item_28_brand" data-key="brand" class="description_detail">Бренд: Palit</li>
#                   <li id="item_28_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_28_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_28_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4060 Ti</li>
#                   <li id="item_28_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_28_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_28_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_28_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_28_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_28_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_28_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_28_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">47 190 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/28/28_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_29">
#             <div class="img_box product_img_box">
#                <a href="product/29/29_details.html" name="29_img">
#                <img src="images/Видеокарта MSI GeForce GT 710 GT 710 2GD3H LP PCI-E 2048Mb GDDR3 64 Bit Retail (GT 710 2GD3H LP).jpg" alt="Видеокарта MSI GeForce GT 710 GT 710 2GD3H LP PCI-E 2048Mb GDDR3 64 Bit Retail (GT 710 2GD3H LP)">
#                </a>
#                <a href="product/29/29_details.html" name="29_name" class="name_item product_name">
#                Видеокарта MSI GeForce GT 710 GT 710 2GD3H LP PCI-E 2048Mb GDDR3 64 Bit Retail (GT 710 2GD3H LP)
#                </a>
#                <div class="description product_description">
#                   <li id="item_29_brand" data-key="brand" class="description_detail">Бренд: MSI</li>
#                   <li id="item_29_card_type" data-key="card_type" class="description_detail">Тип видеокарты: офисная</li>
#                   <li id="item_29_processor_series" data-key="processor_series" class="description_detail">Серия процессора: GeForce GT 7xx</li>
#                   <li id="item_29_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: GeForce GT 710</li>
#                   <li id="item_29_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 2048Mb</li>
#                   <li id="item_29_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR3</li>
#                   <li id="item_29_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 64 Bit</li>
#                   <li id="item_29_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_29_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 2.0</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">4 960 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/29/29_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_30">
#             <div class="img_box product_img_box">
#                <a href="product/30/30_details.html" name="30_img">
#                <img src="images/Видеокарта GigaByte nVidia GeForce RTX 4060 EAGLE OC PCI-E 8192Mb GDDR6 128 Bit Retail GV-N4060EAGLE OC-8GD.jpg" alt="Видеокарта GigaByte nVidia GeForce RTX 4060 EAGLE OC PCI-E 8192Mb GDDR6 128 Bit Retail GV-N4060EAGLE OC-8GD">
#                </a>
#                <a href="product/30/30_details.html" name="30_name" class="name_item product_name">
#                Видеокарта GigaByte nVidia GeForce RTX 4060 EAGLE OC PCI-E 8192Mb GDDR6 128 Bit Retail GV-N4060EAGLE OC-8GD
#                </a>
#                <div class="description product_description">
#                   <li id="item_30_brand" data-key="brand" class="description_detail">Бренд: GigaByte</li>
#                   <li id="item_30_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_30_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_30_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 4060</li>
#                   <li id="item_30_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_30_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_30_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_30_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_30_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_30_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_30_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_30_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">35 280 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/30/30_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_31">
#             <div class="img_box product_img_box">
#                <a href="product/31/31_details.html" name="31_img">
#                <img src="images/Видеокарта Palit nVidia GeForce RTX 3070 GAMINGPRO PCI-E 8192Mb GDDR6 256 Bit Retail.jpg" alt="Видеокарта Palit nVidia GeForce RTX 3070 GAMINGPRO PCI-E 8192Mb GDDR6 256 Bit Retail">
#                </a>
#                <a href="product/31/31_details.html" name="31_name" class="name_item product_name">
#                Видеокарта Palit nVidia GeForce RTX 3070 GAMINGPRO PCI-E 8192Mb GDDR6 256 Bit Retail
#                </a>
#                <div class="description product_description">
#                   <li id="item_31_brand" data-key="brand" class="description_detail">Бренд: Palit</li>
#                   <li id="item_31_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_31_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_31_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 3070</li>
#                   <li id="item_31_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_31_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_31_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 256 Bit</li>
#                   <li id="item_31_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_31_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_31_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_31_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_31_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8+8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">59 710 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/31/31_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_32">
#             <div class="img_box product_img_box">
#                <a href="product/32/32_details.html" name="32_img">
#                <img src="images/Видеокарта Afox GeForce GT 210 AF210-1024D2LG2 PCI-E 1024Mb DDR2 64 Bit Retail.jpg" alt="Видеокарта Afox GeForce GT 210 AF210-1024D2LG2 PCI-E 1024Mb DDR2 64 Bit Retail">
#                </a>
#                <a href="product/32/32_details.html" name="32_name" class="name_item product_name">
#                Видеокарта Afox GeForce GT 210 AF210-1024D2LG2 PCI-E 1024Mb DDR2 64 Bit Retail
#                </a>
#                <div class="description product_description">
#                   <li id="item_32_brand" data-key="brand" class="description_detail">Бренд: Afox</li>
#                   <li id="item_32_card_type" data-key="card_type" class="description_detail">Тип видеокарты: офисная</li>
#                   <li id="item_32_processor_series" data-key="processor_series" class="description_detail">Серия процессора: GeForce GT 2xx</li>
#                   <li id="item_32_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: GeForce GT 210</li>
#                   <li id="item_32_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 1024Mb</li>
#                   <li id="item_32_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: DDR2</li>
#                   <li id="item_32_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 64 Bit</li>
#                   <li id="item_32_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_32_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 2.0</li>
#                   <li id="item_32_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_32_Разъём DVI" data-key="Разъём DVI" class="description_detail">Разъём DVI: есть</li>
#                   <li id="item_32_Выход VGA" data-key="Выход VGA" class="description_detail">Выход VGA: есть</li>
#                   <li id="item_32_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 0 (нет)</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">2 640 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/32/32_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_33">
#             <div class="img_box product_img_box">
#                <a href="product/33/33_details.html" name="33_img">
#                <img src="images/Видеокарта GigaByte Radeon RX 7600 GAMING OC PCI-E 8192Mb GDDR6 128 Bit Retail GV-R76GAMING OC-8GD.jpg" alt="Видеокарта GigaByte Radeon RX 7600 GAMING OC PCI-E 8192Mb GDDR6 128 Bit Retail GV-R76GAMING OC-8GD">
#                </a>
#                <a href="product/33/33_details.html" name="33_name" class="name_item product_name">
#                Видеокарта GigaByte Radeon RX 7600 GAMING OC PCI-E 8192Mb GDDR6 128 Bit Retail GV-R76GAMING OC-8GD
#                </a>
#                <div class="description product_description">
#                   <li id="item_33_brand" data-key="brand" class="description_detail">Бренд: GigaByte</li>
#                   <li id="item_33_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_33_processor_series" data-key="processor_series" class="description_detail">Серия процессора: Radeon RX</li>
#                   <li id="item_33_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: Radeon RX 7600</li>
#                   <li id="item_33_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 8192Mb</li>
#                   <li id="item_33_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_33_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_33_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_33_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_33_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_33_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_33_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">34 440 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/33/33_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_34">
#             <div class="img_box product_img_box">
#                <a href="product/34/34_details.html" name="34_img">
#                <img src="images/Видеокарта Palit nVidia GeForce RTX 3060 Dual OC PCI-E 12288Mb GDDR6 192 Bit Retail (NE63060T19K9-190AD).jpg" alt="Видеокарта Palit nVidia GeForce RTX 3060 Dual OC PCI-E 12288Mb GDDR6 192 Bit Retail (NE63060T19K9-190AD)">
#                </a>
#                <a href="product/34/34_details.html" name="34_name" class="name_item product_name">
#                Видеокарта Palit nVidia GeForce RTX 3060 Dual OC PCI-E 12288Mb GDDR6 192 Bit Retail (NE63060T19K9-190AD)
#                </a>
#                <div class="description product_description">
#                   <li id="item_34_brand" data-key="brand" class="description_detail">Бренд: Palit</li>
#                   <li id="item_34_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_34_processor_series" data-key="processor_series" class="description_detail">Серия процессора: nVidia GeForce RTX</li>
#                   <li id="item_34_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: nVidia GeForce RTX 3060</li>
#                   <li id="item_34_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 12288Mb</li>
#                   <li id="item_34_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_34_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 192 Bit</li>
#                   <li id="item_34_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_34_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 4.0</li>
#                   <li id="item_34_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_34_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_34_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 8</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">33 260 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/34/34_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#          <div class="item product_item" id="item_35">
#             <div class="img_box product_img_box">
#                <a href="product/35/35_details.html" name="35_img">
#                <img src="images/Видеокарта Palit GeForce GTX 1650 GP PCI-E 4096Mb GDDR6 128 Bit Bulk (NE6165001BG1-1175A).jpg" alt="Видеокарта Palit GeForce GTX 1650 GP PCI-E 4096Mb GDDR6 128 Bit Bulk (NE6165001BG1-1175A)">
#                </a>
#                <a href="product/35/35_details.html" name="35_name" class="name_item product_name">
#                Видеокарта Palit GeForce GTX 1650 GP PCI-E 4096Mb GDDR6 128 Bit Bulk (NE6165001BG1-1175A)
#                </a>
#                <div class="description product_description">
#                   <li id="item_35_brand" data-key="brand" class="description_detail">Бренд: Palit</li>
#                   <li id="item_35_card_type" data-key="card_type" class="description_detail">Тип видеокарты: игровая</li>
#                   <li id="item_35_processor_series" data-key="processor_series" class="description_detail">Серия процессора: GeForce GTX 16хх</li>
#                   <li id="item_35_graphic_processor" data-key="graphic_processor" class="description_detail">Графический процессор: GeForce GTX 1650</li>
#                   <li id="item_35_memory_size" data-key="memory_size" class="description_detail">Объем видеопамяти: 4096Mb</li>
#                   <li id="item_35_memory_type" data-key="memory_type" class="description_detail">Тип видеопамяти: GDDR6</li>
#                   <li id="item_35_memory_bus" data-key="memory_bus" class="description_detail">Разрядность шины видеопамяти: 128 Bit</li>
#                   <li id="item_35_connection_type" data-key="connection_type" class="description_detail">Тип подключения: PCI-E</li>
#                   <li id="item_35_interface" data-key="interface" class="description_detail">Интерфейс подключения: PCI-E 16x 3.0</li>
#                   <li id="item_35_hdmi_port" data-key="hdmi_port" class="description_detail">Разъём HDMI: есть</li>
#                   <li id="item_35_displayport" data-key="displayport" class="description_detail">Выход DisplayPort: есть</li>
#                   <li id="item_35_power_pins" data-key="power_pins" class="description_detail">Разъёмы дополнительного питания видеокарты, pin: 6</li>
#                </div>
#                <div class="container product_container">
#                   <div class="price_box">
#                      <p class="price product_price">20 280 руб</p>
#                   </div>
#                   <div class="sale_button product_sale_button">
#                      <a href="product/35/35_details.html">
#                         <p>Подробнее</p>
#                      </a>
#                   </div>
#                </div>
#             </div>
#          </div>
#       </div>
#
# </body></html>
# '''
# def get_html(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     tags_li = soup.select('li')
#
#     for tag in tags_li:
#         print(tag['id'])
#
#
# get_html(html)

# __________________________________________
# Задача: Проанализируйте HTML на странице и извлеките из него текст находящийся после третьего раздела.

# html = '''
# <html lang="en"><head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Моя веб-страница</title>
# </head>
# <body>
#
#     <header>
#         <h1 align="center" class="main-heading">Заголовок страницы</h1>
#         <nav>
#             <ul>
#                 <li><a href="#section1" title="Перейти к разделу 1" class="nav-link">Раздел 1</a></li>
#                 <li><a href="#section2" title="Перейти к разделу 2" class="nav-link">Раздел 2</a></li>
#                 <li><a href="#section3" title="Перейти к разделу 3" class="nav-link">Раздел 3</a></li>
#             </ul>
#         </nav>
#     </header>
#
#     <main>
#         <section id="section1" class="content-section">
#             <h2 class="section-heading">Раздел 1</h2>
#             <div class="section-content">
#                 <p class="section-text">Текст раздела 1</p>
#                 Дополнительный текст рядом с разделом 1.
#             </div>
#         </section>
#
#         <section id="section2" class="content-section">
#             <h2 class="section-heading">Раздел 2</h2>
#             <div class="section-content">
#                 <p class="section-text">Текст раздела 2</p>
#                 Дополнительный текст рядом с разделом 2.
#             </div>
#         </section>
#
#         <section id="section3" class="content-section">
#             <h2 class="section-heading">Раздел 3</h2>
#             <div class="section-content">
#                 <p class="section-text">Текст раздела 3</p>
#                 Дополнительный текст рядом с разделом 3.
#             </div>
#         </section>
#     </main>
#
#     <footer>
#         <p class="copyright">© 2023 Моя веб-страница. Все права защищены.</p>
#     </footer>
#
#
#
# </body></html>
# '''
#
# def get_html(html):
#     soup = BeautifulSoup(html, 'html.parser')
#
#     sibling = soup.findAll('p')
#     str1 = str(sibling[2].next_sibling).strip()
#     sibling = str1
#     return sibling
#
# print(get_html(html))

# __________________________________________
# Задача: Проанализируйте предоставленный HTML-код страницы. Ваша задача - обнаружить и извлечь все email-адреса,
# которые находятся вне стандартных тегов.

html = '''
<html lang="ru"><head>
    <meta charset="UTF-8">
    <title>Информация о студентах</title>
    <link rel="stylesheet" href="style5.css">  <!-- Подключаем CSS -->
</head>
<body>

    <div class="student">
        <img src="student_avatar/student_1.svg" alt="Поликарп Кашин">
        <h2>Поликарп Кашин</h2>
        <p><strong>Дата рождения:</strong> 2000-10-27</p>
        <p><strong>Контактный телефон:</strong> +7-(933)-547-90-83</p>
        <div class="email_field">
        <strong>Электронная почта:</strong> keep2036@duck.com
    </div>
        <p><strong>Специальность:</strong> Психология</p>
        <p><strong>Курс обучения:</strong> 1</p>
        <p><strong>Увлечения и хобби:</strong> Роликовый спорт, Гольф, Парусный спорт</p>
        <p><strong>Опыт работы:</strong> Прораб</p>
        <p><strong>Языки:</strong> Украинский</p>
        <p><strong>Ожидания от курса:</strong> Синтаксис ядра Python минималистичен.</p>
        <p><strong>Сильные стороны в учебе:</strong> Python — высокоуровневый язык программирования общего назначения, ориентированный на повышение производительности разработчика и читаемости кода.</p>
        <p><strong>Любимые предметы:</strong> География, Биология, Инженерия, Химия, Экология</p>
    </div>
    
    <div class="student">
        <img src="student_avatar/student_2.svg" alt="Таяна Белобоцкий">
        <h2>Таяна Белобоцкий</h2>
        <p><strong>Дата рождения:</strong> 1996-12-02</p>
        <p><strong>Контактный телефон:</strong> +7-(964)-577-98-62</p>
        <div class="email_field">
        <strong>Электронная почта:</strong> andrea1837@example.org
    </div>
        <p><strong>Специальность:</strong> Химия</p>
        <p><strong>Курс обучения:</strong> 3</p>
        <p><strong>Увлечения и хобби:</strong> Чтение, Путешествия, Боулинг</p>
        <p><strong>Опыт работы:</strong> Онколог</p>
        <p><strong>Языки:</strong> Непальский</p>
        <p><strong>Ожидания от курса:</strong> Полнотиповое программирование — стиль программирования, отличающийся обширным использованием информации о типах с тем, чтобы механизм проверки согласования типов обеспечил раннее выявление максимального количества всевозможных разновидностей багов.</p>
        <p><strong>Сильные стороны в учебе:</strong> Например, определение функции, которое использует сопоставление с образцом, для выбора одного из вариантов вычисления или извлечения элемента данных из составной структуры, напоминает уравнение.</p>
        <p><strong>Любимые предметы:</strong> Математика, Экономика, Журналистика, Мифология, География</p>
    </div>
    
    <div class="student">
        <img src="student_avatar/student_3.svg" alt="Сергей Дубин">
        <h2>Сергей Дубин</h2>
        <p><strong>Дата рождения:</strong> 2001-03-18</p>
        <p><strong>Контактный телефон:</strong> +7-(999)-103-37-50</p>
        <div class="email_field">
        <strong>Электронная почта:</strong> libs1815@live.com
    </div>
        <p><strong>Специальность:</strong> Архитектура</p>
        <p><strong>Курс обучения:</strong> 2</p>
        <p><strong>Увлечения и хобби:</strong> Садоводство, Походы, Писательство</p>
        <p><strong>Опыт работы:</strong> Библиограф</p>
        <p><strong>Языки:</strong> Арабский</p>
        <p><strong>Ожидания от курса:</strong> Java — строго типизированный объектно-ориентированный язык программирования, разработанный компанией Sun Microsystems.</p>
        <p><strong>Сильные стороны в учебе:</strong> Это способ концептуализации, определяющий организацию вычислений и структурирование работы, выполняемой компьютером.</p>
        <p><strong>Любимые предметы:</strong> Химия, Международные отношения, Компьютерные науки, Реклама, Машиностроение</p>
    </div>
    
    <div class="student">
        <img src="student_avatar/student_4.svg" alt="Василий Санаева">
        <h2>Василий Санаева</h2>
        <p><strong>Дата рождения:</strong> 1998-11-04</p>
        <p><strong>Контактный телефон:</strong> +7-(999)-053-13-25</p>
        <div class="email_field">
        <strong>Электронная почта:</strong> travels1859@example.com
    </div>
        <p><strong>Специальность:</strong> Информатика</p>
        <p><strong>Курс обучения:</strong> 1</p>
        <p><strong>Увлечения и хобби:</strong> Игра на музыкальных инструментах, Серфинг, Моделирование</p>
        <p><strong>Опыт работы:</strong> Монтажник</p>
        <p><strong>Языки:</strong> Панджаби</p>
        <p><strong>Ожидания от курса:</strong> Свой синтаксис и некоторые концепции Erlang унаследовал от языка логического программирования Пролог.</p>
        <p><strong>Сильные стороны в учебе:</strong> Полнотиповое программирование может поддерживаться на уровне системы типов языка или вводиться программистом идиоматически.</p>
        <p><strong>Любимые предметы:</strong> Инженерия, Психология, Журналистика, Океанология, Физкультура</p>
    </div>
    
    <div class="student">
        <img src="student_avatar/student_5.svg" alt="Тора Куликова">
        <h2>Тора Куликова</h2>
        <p><strong>Дата рождения:</strong> 1999-10-14</p>
        <p><strong>Контактный телефон:</strong> +7-(968)-176-07-34</p>
        <div class="email_field">
        <strong>Электронная почта:</strong> extended1928@protonmail.com
    </div>
        <p><strong>Специальность:</strong> Философия</p>
        <p><strong>Курс обучения:</strong> 1</p>
        <p><strong>Увлечения и хобби:</strong> Коллекционирование, Роликовый спорт, Выпечка</p>
        <p><strong>Опыт работы:</strong> Киномеханик</p>
        <p><strong>Языки:</strong> Марвари</p>
        <p><strong>Ожидания от курса:</strong> Является одним из самых распространённых языков программирования с поддержкой отложенных вычислений.</p>
        <p><strong>Сильные стороны в учебе:</strong> REPL — форма организации простой интерактивной среды программирования в рамках средств интерфейса командной строки.</p>
        <p><strong>Любимые предметы:</strong> Инженерия, Электроника, Социология, Музыка, Право</p>
    </div>
    
    <div class="student">
        <img src="student_avatar/student_6.svg" alt="Сальма Алейникова">
        <h2>Сальма Алейникова</h2>
        <p><strong>Дата рождения:</strong> 1998-01-27</p>
        <p><strong>Контактный телефон:</strong> +7-(917)-826-57-16</p>
        <div class="email_field">
        <strong>Электронная почта:</strong> correctly1802@gmail.com
    </div>
        <p><strong>Специальность:</strong> Математика</p>
        <p><strong>Курс обучения:</strong> 1</p>
        <p><strong>Увлечения и хобби:</strong> Серфинг, Плавание, Бадминтон</p>
        <p><strong>Опыт работы:</strong> Бармен</p>
        <p><strong>Языки:</strong> Оромо</p>
        <p><strong>Ожидания от курса:</strong> Erlang — функциональный язык программирования с сильной динамической типизацией, предназначенный для создания распределённых вычислительных систем.</p>
        <p><strong>Сильные стороны в учебе:</strong> Erlang является декларативным языком программирования, который скорее используется для описания того, что должно быть вычислено нежели как.</p>
        <p><strong>Любимые предметы:</strong> Инженерия, Театр, Религиоведение, Иностранные языки, Экология</p>
    </div>
    
    <div class="student">
        <img src="student_avatar/student_7.svg" alt="Ираклий Коклюшкин">
        <h2>Ираклий Коклюшкин</h2>
        <p><strong>Дата рождения:</strong> 2000-02-16</p>
        <p><strong>Контактный телефон:</strong> +7-(939)-173-78-83</p>
        <div class="email_field">
        <strong>Электронная почта:</strong> strict2037@outlook.com
    </div>
        <p><strong>Специальность:</strong> Физика</p>
        <p><strong>Курс обучения:</strong> 4</p>
        <p><strong>Увлечения и хобби:</strong> Шахматы, Альпинизм, Путешествия</p>
        <p><strong>Опыт работы:</strong> Страховой агент</p>
        <p><strong>Языки:</strong> Фула</p>
        <p><strong>Ожидания от курса:</strong> Python поддерживает несколько парадигм программирования, в том числе структурное, объектно-ориентированное, функциональное, императивное и аспектно-ориентированное.</p>
        <p><strong>Сильные стороны в учебе:</strong> Язык включает в себя средства порождения параллельных легковесных процессов и их взаимодействия через обмен асинхронными сообщениями в соответствии с моделью акторов.</p>
        <p><strong>Любимые предметы:</strong> Менеджмент, Экономика, Реклама, Журналистика, История</p>
    </div>
    
    <div class="student">
        <img src="student_avatar/student_8.svg" alt="Айнур Пьецух">
        <h2>Айнур Пьецух</h2>
        <p><strong>Дата рождения:</strong> 2002-04-17</p>
        <p><strong>Контактный телефон:</strong> +7-(932)-870-69-00</p>
        <div class="email_field">
        <strong>Электронная почта:</strong> allen1886@outlook.com
    </div>
        <p><strong>Специальность:</strong> Литература</p>
        <p><strong>Курс обучения:</strong> 2</p>
        <p><strong>Увлечения и хобби:</strong> Бадминтон, Программирование, Игра на музыкальных инструментах</p>
        <p><strong>Опыт работы:</strong> Повар</p>
        <p><strong>Языки:</strong> Малагасийский</p>
        <p><strong>Ожидания от курса:</strong> В наш век информации слишком много, чтобы понять кто прав, а кто лукавит.</p>
        <p><strong>Сильные стороны в учебе:</strong> Разработан и поддерживается компанией Ericsson.</p>
        <p><strong>Любимые предметы:</strong> Русский язык, Политология, Психология, Ветеринария, Музыка</p>
    </div>
    
    <div class="student">
        <img src="student_avatar/student_9.svg" alt="Сажида Авченко">
        <h2>Сажида Авченко</h2>
        <p><strong>Дата рождения:</strong> 1998-08-02</p>
        <p><strong>Контактный телефон:</strong> +7-(930)-274-56-88</p>
        <div class="email_field">
        <strong>Электронная почта:</strong> weekends1961@example.com
    </div>
        <p><strong>Специальность:</strong> Философия</p>
        <p><strong>Курс обучения:</strong> 3</p>
        <p><strong>Увлечения и хобби:</strong> Волейбол, Дегустация вин, Изготовление украшений</p>
        <p><strong>Опыт работы:</strong> Орнитолог</p>
        <p><strong>Языки:</strong> Английский</p>
        <p><strong>Ожидания от курса:</strong> Сопоставление с образцом распространено даже на битовые строки, что упрощает реализацию телекоммуникационных протоколов.</p>
        <p><strong>Сильные стороны в учебе:</strong> Haskell — стандартизированный чистый функциональный язык программирования общего назначения.</p>
        <p><strong>Любимые предметы:</strong> Международные отношения, Статистика, Культурология, Геология, Физика</p>
    </div>
    
    <div class="student">
        <img src="student_avatar/student_10.svg" alt="Генриетта Астафьев">
        <h2>Генриетта Астафьев</h2>
        <p><strong>Дата рождения:</strong> 2002-08-14</p>
        <p><strong>Контактный телефон:</strong> +7-(993)-690-82-31</p>
        <div class="email_field">
        <strong>Электронная почта:</strong> sorted2073@yandex.com
    </div>
        <p><strong>Специальность:</strong> Биология</p>
        <p><strong>Курс обучения:</strong> 3</p>
        <p><strong>Увлечения и хобби:</strong> Фотография, Блоггинг, Танцы</p>
        <p><strong>Опыт работы:</strong> Литейщик</p>
        <p><strong>Языки:</strong> Малайский</p>
        <p><strong>Ожидания от курса:</strong> Например, определение функции, которое использует сопоставление с образцом, для выбора одного из вариантов вычисления или извлечения элемента данных из составной структуры, напоминает уравнение.</p>
        <p><strong>Сильные стороны в учебе:</strong> Erlang является декларативным языком программирования, который скорее используется для описания того, что должно быть вычислено нежели как.</p>
        <p><strong>Любимые предметы:</strong> Менеджмент, Аудит, Лесное хозяйство, Информатика, Кинематография</p>
    </div>
    


</body></html>
'''

def get_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    # Допишите поиск и извлечение email
    emails = soup.findAll('strong', string='Электронная почта:')

    list1= []
    for email in emails:
        str1 = str(email.next_sibling).strip()
        list1.append(str1)
    emails = list1
    return emails

print(get_html(html))