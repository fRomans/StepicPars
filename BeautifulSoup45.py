from bs4 import BeautifulSoup

# __________________________________________
# Задача: Необходимо написать код, который будет обрабатывать HTML-структуру с карточками товаров (в данном случае — книг).
# Код должен вычислять общую сумму, которую можно получить при продаже всех книг на складе.


# html = '''<!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Онлайн Магазин Книг</title>
# </head>
# <body>
#     <div class="book-card">
#         <img src="1.png" alt="Обложка книги 1" class="book-cover book-cover_hard">
#         <h2 class="book pages">Название Книги 1</h2>
#         <p class="book-author">Автор: Автор 1</p>
#         <p class="book-isbn">ISBN: 978-1234567890</p>
#         <p class="book-cover-type">Обложка: Твердая</p>
#         <p class="count price">Цена: $20.00</p>
#         <p class="book-format">Формат: Мягкая обложка</p>
#         <p class="count pages">Количество страниц: 300</p>
#         <p class="count stock">Количество на складе: 75</p>
#         <p class="book-publisher">Издательство: Издательство 1</p>
#         <p class="book-publication-date">Дата публикации: 01.01.2023</p>
#         <p class="count rating">Рейтинг: 4.5</p>
#         <p class="book-genre">Жанр: Роман</p>
#         <p class="book-language">Язык: Английский</p>
#         <p class="book-availability">Доступность: В наличии</p>
#         <p class="book-description">Описание: Краткое описание книги 1.</p>
#         <button class="book-purchase-btn">Добавить в корзину</button>
#     </div>
#     <div class="book-card">
#         <img src="2.png" alt="Обложка книги 2" class="book-cover book-cover_hard">
#         <h2 class="book pages">Название Книги 2</h2>
#         <p class="book-author">Автор: Автор 2</p>
#         <p class="book-isbn">ISBN: 978-9876543210</p>
#         <p class="book-cover-type">Обложка: Мягкая</p>
#         <p class="count price">Цена: $18.50</p>
#         <p class="book-format">Формат: Электронная версия (e-book)</p>
#         <p class="count pages">Количество страниц: 250</p>
#         <p class="count stock">Количество на складе: 119</p>
#         <p class="book-publisher">Издательство: Издательство 3</p>
#         <p class="book-publication-date">Дата публикации: 20.03.2023</p>
#         <p class="count rating">Рейтинг: 4.7</p>
#         <p class="book-genre">Жанр: Детская литература</p>
#         <p class="book-language">Язык: Французский</p>
#         <p class="book-availability">Доступность: В наличии</p>
#         <p class="book-description">Описание: Краткое описание книги 2.</p>
#          <button class="book-purchase-btn">Добавить в корзину</button>
#     </div>
#     <div class="book-card">
#         <img src="3.png" alt="Обложка книги 3" class="book-cover book-cover_hard">
#         <h2 class="book pages">Название Книги 3</h2>
#         <p class="book-author">Автор: Автор 3</p>
#         <p class="book-isbn">ISBN: 978-0987654321</p>
#         <p class="book-cover-type">Обложка: Твердая</p>
#         <p class="count price">Цена: $25.00</p>
#         <p class="book-format">Формат: Мягкая обложка</p>
#         <p class="count pages">Количество страниц: 400</p>
#         <p class="count stock">Количество на складе: 216</p>
#         <p class="book-publisher">Издательство: Издательство 2</p>
#         <p class="book-publication-date">Дата публикации: 15.02.2023</p>
#         <p class="count rating">Рейтинг: 4.8</p>
#         <p class="book-genre">Жанр: Фантастика</p>
#         <p class="book-language">Язык: Русский</p>
#         <p class="book-availability">Доступность: В наличии</p>
#         <p class="book-description">Описание: Краткое описание книги 3.</p>
#         <button class="book-purchase-btn">Добавить в корзину</button>
#     </div>
#     <div class="book-card">
#         <img src="4.png" alt="Обложка книги 4" class="book-cover book-cover_hard">
#         <h2 class="book pages">Название Книги 4</h2>
#         <p class="book-author">Автор: Автор 4</p>
#         <p class="book-isbn">ISBN: 978-5432109876</p>
#         <p class="book-cover-type">Обложка: Твердая</p>
#         <p class="count price">Цена: $22.00</p>
#         <p class="book-format">Формат: Мягкая обложка</p>
#         <p class="count pages">Количество страниц: 350</p>
#         <p class="count stock">Количество на складе: 17</p>
#         <p class="book-publisher">Издательство: Издательство 4</p>
#         <p class="book-publication-date">Дата публикации: 10.04.2023</p>
#         <p class="count rating">Рейтинг: 4.9</p>
#         <p class="book-genre">Жанр: Детектив</p>
#         <p class="book-language">Язык: Английский</p>
#         <p class="book-availability">Доступность: В наличии</p>
#         <p class="book-description">Описание: Краткое описание книги 4.</p>
#         <button class="book-purchase-btn">Добавить в корзину</button>
#     </div>
#     <div class="book-card">
#         <img src="5.png" alt="Обложка книги 5" class="book-cover book-cover_hard">
#         <h2 class="book pages">Название Книги 5</h2>
#         <p class="book-author">Автор: Автор 5</p>
#         <p class="book-isbn">ISBN: 978-8765432109</p>
#         <p class="book-cover-type">Обложка: Мягкая</p>
#         <p class="count price">Цена: $19.50</p>
#         <p class="book-format">Формат: Мягкая обложка</p>
#         <p class="count pages">Количество страниц: 280</p>
#         <p class="count stock">Количество на складе: 63</p>
#         <p class="book-publisher">Издательство: Издательство 5</p>
#         <p class="book-publication-date">Дата публикации: 05.05.2023</p>
#         <p class="count rating">Рейтинг: 4.6</p>
#         <p class="book-genre">Жанр: Фэнтези</p>
#         <p class="book-language">Язык: Испанский</p>
#         <p class="book-availability">Доступность: В наличии</p>
#         <p class="book-description">Описание: Краткое описание книги 5.</p>
#         <button class="book-purchase-btn">Добавить в корзину</button>
#     </div>
# </body>
# </html>
# '''

# def calculate_total_price(html: str) -> float:
#     # Инициализация BeautifulSoup.
#     soup = BeautifulSoup(html, 'html.parser')
#     tags = soup.findAll('div', class_='book-card')
#
#     total = 0.0
#     for tag in tags:
#         str1 = str(tag.find('p', class_='count price').text).replace('Цена: $', "")
#         price = float(str1)
#         str2 = str(tag.find('p', class_='count stock').text).replace('Количество на складе: ', "")
#         count = float(str2)
#         vsego = price*count
#         total += vsego
#
#     print(f"Общая стоимость в случае продажи всех товаров: ${total}")
#
# calculate_total_price(html)

# __________________________________________
# Задача:Извлекаем при помощи bs4 данные о стоимости часов (всего 8 шт)
# Складываем все числа

# html = '''
# <html lang="en"><head>
# 	<link rel="stylesheet" href="../style/style.css">
# 	<meta charset="UTF-8">
# 	<meta name="viewport" content="width=device-width, initial-scale=1.0">
# 	<title>WEB Парсинг на Python</title>
# </head>
# <body>
# <div class="headers">
# 	<div class="p_headers"><a href="https://stepik.org/z/104774/?utm_source=html">WEB Парсинг на Python</a></div>
# </div>
#
# 				<div class="pagen">
#
#   						<a href="index1_page_1.html">1</a>
#  						<a href="index1_page_2.html">2</a>
#  						<a href="index1_page_3.html">3</a>
#   						<a href="index1_page_4.html">4</a>
#
#
# 				</div>
# 	<div class="main">
#
#
#
# 				<div class="nav_menu">
# 						<a href="index1_page_1.html"><div id="watch">ЧАСЫ</div></a>
# 						<a href="index2_page_1.html"><div id="mobile">ТЕЛЕФОНЫ</div></a>
# 						<a href="index3_page_1.html"><div id="mouse">МЫШИ</div></a>
# 						<a href="index4_page_1.html"><div id="hdd">HDD</div></a>
# 						<a href="index5_page_1.html"><div id="headphones">НАУШНИКИ</div></a>
# 				</div>
#
#
# 			<div class="item_card">
# 					<div class="item">
# 						<div class="img_box">
# 							<a href="watch/1/1_1.html" name="1_1"><img src="https://parsinger.ru/img/1/1.jpg" alt=""></a>
# 							<a href="watch/1/1_1.html" name="1_1" class="name_item">Jet Kid Start blue Умные детские часы</a>
#
#
#
# 								<div class="description">
# 								<li>Бренд: Jet</li>
# 								<li>Тип: умные часы</li>
# 								<li>Материал корпуса: пластик</li>
# 								<li>Технология экрана: Монохромный</li>
#
# 								</div>
#
#
#
#
# 							<div class="container">
#
# 								<div class="price_box"><p class="price">2310 руб</p></div>
# 								<div class="sale_button"><a href="watch/1/1_1.html"><p>Подробнее</p></a></div>
#
# 							</div>
#
# 						</div></div>
# 					<div class="item">
# 						<div class="img_box">
# 							<a href="watch/1/1_2.html" name="1_2"><img src="https://parsinger.ru/img/1/2.jpg" alt=""></a>
# 							<a href="watch/1/1_2.html" name="1_2" class="name_item">BAND 6 FOREST GREEN FARA-B19 HUAWEI</a>
#
#
#
# 								<div class="description">
# 								<li>Бренд: Huawei</li>
# 								<li>Тип: фитнес браслет</li>
# 								<li>Материал корпуса: полимер</li>
# 								<li>Технология экрана: AMOLED</li>
#
# 								</div>
#
#
#
#
# 							<div class="container">
#
# 								<div class="price_box"><p class="price">5480 руб</p></div>
# 								<div class="sale_button"><a href="watch/1/1_2.html"><p>Подробнее</p></a></div>
#
# 							</div>
#
# 						</div></div>
# 					<div class="item">
# 						<div class="img_box">
# 							<a href="watch/1/1_3.html" name="1_3"><img src="https://parsinger.ru/img/1/3.jpg" alt=""></a>
# 							<a href="watch/1/1_3.html" name="1_3" class="name_item">Умные часы GT 3 MIL-B19S BLACK HUAWEI</a>
#
#
#
# 								<div class="description">
# 								<li>Бренд: Huawei</li>
# 								<li>Тип: умные часы</li>
# 								<li>Материал корпуса: пластик</li>
# 								<li>Технология экрана: Монохромный</li>
#
# 								</div>
#
#
#
#
# 							<div class="container">
#
# 								<div class="price_box"><p class="price">21810 руб</p></div>
# 								<div class="sale_button"><a href="watch/1/1_3.html"><p>Подробнее</p></a></div>
#
# 							</div>
#
# 						</div></div>
# 					<div class="item">
# 						<div class="img_box">
# 							<a href="watch/1/1_4.html" name="1_4"><img src="https://parsinger.ru/img/1/4.jpg" alt=""></a>
# 							<a href="watch/1/1_4.html" name="1_4" class="name_item">Умные часы GT 3 MIL-B19V BROWN HUAWEI</a>
#
#
#
# 								<div class="description">
# 								<li>Бренд: Huawei</li>
# 								<li>Тип: умные часы</li>
# 								<li>Материал корпуса: нержавеющая сталь</li>
# 								<li>Технология экрана: AMOLED</li>
#
# 								</div>
#
#
#
#
# 							<div class="container">
#
# 								<div class="price_box"><p class="price">21810 руб</p></div>
# 								<div class="sale_button"><a href="watch/1/1_4.html"><p>Подробнее</p></a></div>
#
# 							</div>
#
# 						</div></div>
# 					<div class="item">
# 						<div class="img_box">
# 							<a href="watch/1/1_5.html" name="1_5"><img src="https://parsinger.ru/img/1/5.jpg" alt=""></a>
# 							<a href="watch/1/1_5.html" name="1_5" class="name_item">GT RUNNER-B19S BLACK HUAWEI</a>
#
#
#
# 								<div class="description">
# 								<li>Бренд: Huawei</li>
# 								<li>Тип: умные часы</li>
# 								<li>Материал корпуса: пластик</li>
# 								<li>Технология экрана: AMOLED</li>
#
# 								</div>
#
#
#
#
# 							<div class="container">
#
# 								<div class="price_box"><p class="price">27770 руб</p></div>
# 								<div class="sale_button"><a href="watch/1/1_5.html"><p>Подробнее</p></a></div>
#
# 							</div>
#
# 						</div></div>
# 					<div class="item">
# 						<div class="img_box">
# 							<a href="watch/1/1_6.html" name="1_6"><img src="https://parsinger.ru/img/1/6.jpg" alt=""></a>
# 							<a href="watch/1/1_6.html" name="1_6" class="name_item">GT RUNNER-B19A GREY HUAWEI</a>
#
#
#
# 								<div class="description">
# 								<li>Бренд: Huawei</li>
# 								<li>Тип: умные часы</li>
# 								<li>Материал корпуса: пластик</li>
# 								<li>Технология экрана: AMOLED</li>
#
# 								</div>
#
#
#
#
# 							<div class="container">
#
# 								<div class="price_box"><p class="price">27770 руб</p></div>
# 								<div class="sale_button"><a href="watch/1/1_6.html"><p>Подробнее</p></a></div>
#
# 							</div>
#
# 						</div></div>
# 					<div class="item">
# 						<div class="img_box">
# 							<a href="watch/1/1_7.html" name="1_7"><img src="https://parsinger.ru/img/1/7.jpg" alt=""></a>
# 							<a href="watch/1/1_7.html" name="1_7" class="name_item">Умные часы GT 3 MIL-B19 GOLD HUAWEI</a>
#
#
#
# 								<div class="description">
# 								<li>Бренд: Huawei</li>
# 								<li>Тип: умные часы</li>
# 								<li>Материал корпуса: нержавеющая сталь, пластик</li>
# 								<li>Технология экрана: AMOLED</li>
#
# 								</div>
#
#
#
#
# 							<div class="container">
#
# 								<div class="price_box"><p class="price">24230 руб</p></div>
# 								<div class="sale_button"><a href="watch/1/1_7.html"><p>Подробнее</p></a></div>
#
# 							</div>
#
# 						</div></div>
# 					<div class="item">
# 						<div class="img_box">
# 							<a href="watch/1/1_8.html" name="1_8"><img src="https://parsinger.ru/img/1/8.jpg" alt=""></a>
# 							<a href="watch/1/1_8.html" name="1_8" class="name_item">Умные часы WATCH 3 GALILEO-L11 STEEL</a>
#
#
#
# 								<div class="description">
# 								<li>Бренд:  Huawei</li>
# 								<li>Тип: умные часы</li>
# 								<li>Материал корпуса: металл, керамика</li>
# 								<li>Технология экрана:  AMOLED</li>
#
# 								</div>
#
#
#
#
# 							<div class="container">
#
# 								<div class="price_box"><p class="price">32600 руб</p></div>
# 								<div class="sale_button"><a href="watch/1/1_8.html"><p>Подробнее</p></a></div>
#
# 							</div>
#
# 						</div></div>
#
#
#
#
#
#
#
#
#
# </div>
# 	</div>
# 			<div class="pagen">
#
#   						<a href="index1_page_1.html">1</a>
#  						<a href="index1_page_2.html">2</a>
#  						<a href="index1_page_3.html">3</a>
#   						<a href="index1_page_4.html">4</a>
#
# 		</div>
# <div class="bottom"></div>
#
#
#
# </body></html>
# '''
#
# soup = BeautifulSoup(html, 'html.parser')
# tags = soup.findAll('p', class_='price')
#
# total = 0.0
# for tag in tags:
#     str1 = str(tag.text).replace(' руб', "")
#     price = float(str1)
#     total += price
# print(total)

# __________________________________________
# Задача:Получаем данные при помощи bs4 о старой цене и новой цене
# По формуле высчитываем процент скидки
# Формула (старая цена - новая цена) * 100 / старая цена)
# Вставьте получившийся результат в поле ответа
# Ответ должен быть числом с 1 знаком после запятой.

html = '''
<html lang="en"><head>

	<link rel="stylesheet" href="https://parsinger.ru/style/style_page.css">

	<meta charset="UTF-8">

	<meta name="viewport" content="width=device-width, initial-scale=1.0">

	<title>&gt;WEB Парсинг на Python</title>

</head>

<body>

<div class="headers">

	<div class="p_headers"><a href="https://stepik.org/z/104774/?utm_source=html">WEB Парсинг на Python</a></div>

</div>

	<a href="https://parsinger.ru/html/index4_page_1.html#4_1" id="a_back"><div class="back">На главную</div></a>

	<div class="main">

		<div class="item_card">



				<div class="image_box">



					<img src="https://parsinger.ru/img/4/4/4_1.jpg" alt="" class="img_size">



				</div>

				<div class="description">

					<p id="p_header">Жесткий диск 3.5 2 Tb 5900 rpmrpm 64 MbMb cache Seagate ST2000VX008 SATA III 6 Gb/s </p>

					<p class="article">Артикул: 8958218</p>

					<ul id="description">



						<li id="brand">Бренд: Seagate</li>

						<li id="model">Модель: G102 LIGHTSYNC</li>



						<li id="form-factor">Форм-фактор: 3.5</li>

						<li id="capacity">Ёмкость: 2 Tb </li>

						<li id="buffer-memory">Объем буферной памяти: 64 Mb</li>





						<li id="rotational-speed">Скорость вращения об/мин: 5900 rpm</li>

						<li id="power-usage">Энергопотребление: 5.60 Вт </li>

						



						<li id="connection-interface">Интерфейс подключения: SATA III 6 Gb/s</li>

						<li id="site">Сайт производителя: www.seagate.com</li>

						

					</ul>





						<span id="in_stock">В наличии: 37</span>

					<div class="sale">

	

						<span id="price">12240 руб</span>

						<span id="old_price">15240 руб</span>

						<button id="sale_button">Купить</button>

					</div>

				</div>

				

		</div>

	</div>	

<div class="bottom"></div></body></html>
'''

def calculate_total_price(html: str) -> float:
    # Инициализация BeautifulSoup.
    soup = BeautifulSoup(html, 'html.parser')
    str1 = str(soup.find('span', id='price').text).replace(' руб', "")
    price = float(str1)
    str2 = str(soup.find('span', id='old_price').text).replace(' руб', "")
    old_price = float(str2)
    procent = (old_price-price)*100/old_price
    procent = round(procent, 1) # округление

    print(f"Процент скидки: {procent}")

calculate_total_price(html)
