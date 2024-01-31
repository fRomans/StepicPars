import os.path

import requests


# Выполняем GET-запрос к указанному URL с параметром stream=True.
# Параметр stream=True гарантирует, что соединение будет удерживаться, пока не будут получены все данные.
response = requests.get(url="https://parsinger.ru/video_downloads/videoplayback.mp4", stream=True)
response.encoding = "UTF-8"

# Открываем (или создаем) файл 'file.mp4' в режиме 'wb' (write binary),
# чтобы сохранить в него бинарные данные.
# R:\AProgr\Python/ - место куда копирую файл file.mp4
with open('R:\AProgr\Python/file.mp4', 'wb') as file:

    # Записываем содержимое ответа (response.content) в файл.
    # Этот метод подходит для относительно небольших файлов,
    # так как все содержимое файла сначала загружается в оперативную память.
           # file.write(response.content)

    # Если файл очень большой или вы не хотите ждать, пока он полностью скачается,
    # рекомендуется использовать .iter_content()

    for piece in response.iter_content(chunk_size=10000):
        file.write(piece)

    print(os.path.getsize('R:\AProgr\Python/file.mp4'))

