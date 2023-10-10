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
        a = float(input("введите первое число: "))
        c = input("введите операцию (+, -, *, / : ")
        b = float(input("введите второе число: "))

        if c == "+":
            print("ответ: ", a + b)
        elif c == "-":
            print("ответ: ", a - b)
        elif c == "*":
            print("ответ: ", a * b)
        elif c == "/":
            try:
                print("ответ: ", a / b)
            except ZeroDivisionError:
                print('на 0 делить нельзя')



    except ValueError as err:
        print(f' ой, ошибочка {err}')


