"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Допускаются любые усложения задания - валидация, подключение к БД, передача данных в файл
"""
import hashlib
import sqlite3


def compare_users(u):
    cursor.execute(f"SELECT password FROM users where name = '{u}';")
    passwd_from_login = cursor.fetchone()  # passwd является кортежем
    if passwd_from_login:
        existed_user(u, passwd_from_login)
    else:
        new_user(u)


#   Заместо соли я использую логины
#   По сути можно было хранить генерируемую соль в программе при создании нового пользователя в виде списка
def existed_user(u, p):
    password = input("Enter the password: ")
    hash_password = hashlib.sha256(u.encode() + password.encode()).hexdigest()
    # либо hash_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), u, 100000)
    if hash_password == p[0]:
        print(f"Login is successful! Hello, {u}")
    else:
        print("Password is incorrect")


def new_user(u):
    password = input("You are newbie! Please enter a password for your login: ")
    hash_password = hashlib.sha256(u.encode() + password.encode()).hexdigest()
    cursor.execute(f"INSERT INTO users(name, password) VALUES('{u}','{hash_password}');")
    conn.commit()
    print("User was added")


conn = sqlite3.connect("up.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users(name TEXT NOT NULL, password TEXT NOT NULL);")
conn.commit()
username = input("Enter the login: ")
compare_users(username)
