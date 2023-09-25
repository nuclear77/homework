def convert():
    string = input("Введите строку: ")

    string = string.strip()

    negative = False
    if string.startswith('-'):
        negative = True
        string = string[1:]

    has_decimal = False
    if '.' in string:
        has_decimal = True

    for char in string:
        if not (char.isdigit() or (has_decimal and char == '.')):
            return None

    number = float(string) if has_decimal else int(string)

    if negative:
        number *= -1

    return number


result = convert()
if result is None:
    print("Неверный формат числа")
else:
    print("Результат:", result)
