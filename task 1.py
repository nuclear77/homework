#  первое задание
# sentence = input("Введите предложение: ")
#
# new_sentence = "!{} {}!".format(sentence.split()[1], sentence.split()[0])
# print(new_sentence)
#
# new_sentence = "!{1} {0}!".format(sentence.split()[0], sentence.split()[1])
# print(new_sentence)
#
# sentence = f"!{sentence.split()[1]} {sentence.split()[0]}!"
# print(new_sentence)


# второе задание
# name = input("Введите имя: ")
# age = input("Введите возраст: ")
#
# try:
#     age = int(age)
#     if age <= 0:
#         print("Ошибка, повторите ввод")
#     elif age < 10:
#         print("Привет, шкет", name)
#     elif age <= 18:
#         print("Как жизнь", name, "?")
#     elif age < 100:
#         print("Что желаете", name, "?")
#     else:
#         print(name, ", вы лжете - в наше время столько не живут...")
# except ValueError:
#     print("Ошибка, повторите ввод")

# третье задание
# while True:
#     name = input("Введите имя: ")
#     age = int(input("Введите возраст: "))
#
#     if age < 0 or age == 0 or not isinstance(age, int):
#         print("Ошибка, повторите ввод")
#     elif age < 10:
#         print("Привет, шкет {}!".format(name))
#     elif age <= 18:
#         print("Как жизнь, {}?".format(name))
#     elif age < 100:
#         print("Что желаете, {}?".format(name))
#     else:
#         print("{}, вы лжете - в наше время столько не живут...".format(name))


# четвертое задание
# цикл while
# n = int(input("Введите целое число n: "))
# sum_cubes = 0
# i = 1
#
# while i <= n:
#     sum_cubes += i ** 3
#     i += 1
#
# print("Сумма кубов чисел от 1 до {} равна {}".format(n, sum_cubes))

# цикл for
# n = int(input("Введите целое число n: "))
# sum_cubes = 0
#
# for i in range(1, n+1):
#     sum_cubes += i ** 3
#
# print("Сумма кубов чисел от 1 до {} равна {}".format(n, sum_cubes))


# пятое задание
import random

number = random.randint(1, 10)
guess = 0


print("Угадайте число от 1 до 10.")

while guess != number:
    guess = int(input("Введите вашу догадку: "))


    if guess < number:
        print("Загаданное число больше.")
    elif guess > number:
        print("Загаданное число меньше.")

print("Поздравляю! Вы угадали число {}".format(number))