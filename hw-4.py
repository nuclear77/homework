# задача 1
# b = b'r\xc3\xa9sum\xc3\xa9'
# s = b.decode('utf-8')
# print(s)
# latin1 = s.encode('latin1')
# print(latin1)


# задача 2
# input1 = input("Введите первую строку: ")
# input2 = input("Введите вторую строку: ")
# input3 = input("Введите третью строку: ")
# input4 = input("Введите четвертую строку: ")
#
# file = open("file.txt", "w")
# file.write(input1 + "\n" + input2)
# file.close()
#
# file = open("file.txt", "a")
# file.write("\n" + input3 + "\n" + input4)
# file.close()

# задача 3
# import json
# dictionary = {
#     123456: ("Иван", 25),
#     789012: ("Мария", 30),
#     345678: ("Алексей", 42),
#     901234: ("Елена", 19),
#     567890: ("Николай", 36)
# }
#
# with open("data.json", "w") as file:
#     json.dump(dictionary, file)

# задача 4
# import json
# import csv
#
# with open("data.json", "r") as json_file:
#     data = json.load(json_file)
#
# with open("data.csv", "w", newline="") as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(["id", "name", "age"])
#     for id, (name, age) in data.items():
#         writer.writerow([id, name, age, ""])

# задача 5 под вопросом
import pandas as pd

data = pd.read_csv('data.csv')
data.drop(['age'], axis=1, inplace=True)
data.to_excel('data.xlsx', index=False)
