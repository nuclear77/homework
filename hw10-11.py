# 11
#1 генератор геометрической прогресии
# def geometric_generator(a, r, n):
#     current_term = a
#     for _ in range(n):
#         yield current_term
#         current_term *= r
#
# generator = geometric_generator(2, 3, 6)
# for term in generator:
#     print(term)


# 3 функция для фильтрации имейла(регуляркой)
# import re
#
#
# def filter_emails(emails):
#     pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
#     filtered_emails = []
#     for email in emails:
#         if re.match(pattern, email):
#             filtered_emails.append(email)
#
#     return filtered_emails
#
#
# emails = ['user@example.com', 'invalid.email', 'another_user@example.com', 'dota2@steam.com']
# filtered_emails = filter_emails(emails)
# print(filtered_emails)




#10
while True:
    try:
        class CustomErr(Exception):
            def __init__(self, *args):
                if args:
                    self.message = args[0]
                else:
                    self.message = None

            def __str__(self):
                print('былла введена строка')
                if self.message:
                    return 'CustomErr, {0} '.format(self.message)
                else:
                    return 'CustomErr была вызвана'


        a = input("Введите первое число: ")
        if not a.isdigit():
            raise CustomErr("a должна быть числом")

        c = input("Введите операцию (+, -, *, /): ")
        if not any([c == '+', c == '-', c == '*', c == '/']):
            raise CustomErr("c должна быть одной из операций: +, -, *, /")

        b = input("Введите второе число: ")
        if not b.isdigit():
            raise CustomErr("b должна быть числом")

        a = float(a)
        b = float(b)

        if c == "+":
            print("Ответ: ", a + b)
        elif c == "-":
            print("Ответ: ", a - b)
        elif c == "*":
            print("Ответ: ", a * b)
        elif c == "/":
            try:
                print("Ответ: ", a / b)
            except ZeroDivisionError:
                print('На 0 делить нельзя')

        raise CustomErr

    except ValueError:
        print('Ошибка')
