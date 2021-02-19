"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря программно,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
"""
from time import time


def count_time(function):
    def get_time(*args, **kwargs):
        start_time = time()
        function(*args, **kwargs)
        print(time() - start_time)
        return function(*args, **kwargs)
    return get_time


@count_time
def add_list():
    new_list = [i for i in range(0, 100000)]
    return new_list


@count_time
def copy_list():
    a = my_list.copy()
    return a


@count_time
def fetch_list_index():
    for i in range(len(my_list)):
        if i == 10000:
            return i


@count_time
def fetch_list_value():
    for i in my_list:
        if i == 10000:
            return i


@count_time
def del_list():
    my_list.clear()
    return my_list


@count_time
def add_dict():
    new_dict = {a: a for a in range(0, 1000000)}
    return new_dict


@count_time
def copy_dict():
    a = my_dict.copy()
    return a


@count_time
def fetch_dict_key():
    i = my_dict[10000]
    return i


@count_time
def fetch_dict_value():
    for i in my_dict.values():
        if i == "10000":
            return i


@count_time
def del_dict():
    my_dict.clear()
    return my_dict


print("Filling list, then dict")
my_list = add_list()
my_dict = add_dict()
print("Copying list, then dict")
copy_list()
copy_dict()
print("Finding in list by index, then dict by key")
fetch_list_index()
fetch_dict_key()
print("Finding in list, then dict by value")
fetch_list_value()
fetch_dict_value()
print("Deleting list, then dict")
del_list()
del_dict()
# Время работы добавления, копирования и удаления словаря больше, потому что словарь - это по сути хеш-таблица и для
# работы с хэшами требуется больше памяти.
# Для выборки элементов в списке потребовалось больше времени, чем для словаря, потому что словарь использует
# таблицу для реализации упорядочения.
# По значениям же поиск проводится дольше в словаре.
