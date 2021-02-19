"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""

import hashlib
import os   # вычитал на coderoad, что random - это псевдорандом, рекомендуют использовать os.urandom()


class DictClass:
    def __init__(self):
        self.my_dict = {}

    def checking_for_existence(self, url):
        return self.my_dict.get(url) is not None

    def add_url(self, url):
        print("URL was not found")
        salt = os.urandom(32)  # создаём рандомную соль для нового URL
        key = hashlib.pbkdf2_hmac('sha256', url.encode('utf-8'), salt, 100000)
        # либо key = hashlib.sha256(url.encode() + salt.encode()).hexdigest()
        self.my_dict[url] = {'salt': salt, 'key': key}  # храним соль и ключ в словаре
        print(f"{url} has been added to cache")


my_obj_url = DictClass()
while True:
    user_url = input('Enter URL (blank space for exit): ')
    if user_url == '':
        print(f"Final dictionary: {my_obj_url.my_dict}")    # выдаём все введённые URL с солью и ключом
        break
    if not my_obj_url.checking_for_existence(user_url):
        my_obj_url.add_url(user_url)
    else:
        print('URL is already in the cache! Please enter new URL')
