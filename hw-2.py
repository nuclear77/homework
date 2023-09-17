# первое задание
# dict = {"key1": "value1", "key2": "value2"}
# new_dict = {value: key for key, value in dict.items()}
# print(new_dict)


# второе задание
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# num = int(input("Введите число: "))
# result = factorial(num)
# print("Факториал числа {} равен {}".format(num, result))


# третье задание
# num = [1, 2, 3, 2, 1, 4, 5, 3, 2, 1]
# count = {}
#
# for number in num:
#     count[number] = count.get(number, 0) + 1
#
# for key, value in count.items():
#     print("Число {} встречается {} раза".format(key, value))


# четвертое задание
from datetime import datetime
import time

def get_time():
    time.sleep(1)
    return datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')

number_of_elements = int(input("Введите количество элементов списка: "))
new_list = [get_time() for _ in range(number_of_elements)]
print(new_list)