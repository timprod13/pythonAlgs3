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
    def get_time():
        start_time = time()
        function()
        print(time() - start_time)
        return function()
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
def pop_list():
    my_list.pop(1)
    my_list.pop(2)
    my_list.pop(3)
    my_list.pop(4)
    my_list.pop(5)
    my_list.pop(6)
    my_list.pop(7)
    my_list.pop(8)
    my_list.pop(9)
    my_list.pop(10)
    return my_list


@count_time
def del_list():
    my_list.clear()
    return my_list


@count_time
def add_dict():
    new_dict = {a: a for a in range(0, 100000)}
    return new_dict


@count_time
def copy_dict():
    a = my_dict.copy()
    return a


@count_time
def pop_dict():
    my_dict.popitem()
    my_dict.popitem()
    my_dict.popitem()
    my_dict.popitem()
    my_dict.popitem()
    my_dict.popitem()
    my_dict.popitem()
    my_dict.popitem()
    my_dict.popitem()
    my_dict.popitem()
    return my_dict


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
print("Popping list, then dict")
pop_list()
pop_dict()
print("Deleting list, then dict")
del_list()
del_dict()
# Время работы со словарем больше, потому что словарь - это по сути хеш-таблица и для работы с ним требуется больше
# памяти
