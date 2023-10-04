# задание 1
# class Soda:
#     def __init__(self, adder):
#         self.adder = adder
#
#     def Show_my_drink(self):
#         if self.adder:
#             print('газировка с ', self.adder)
#         else:
#             print('обычкая газировка')
#
# soda2 = Soda("lime")
# soda2.Show_my_drink()


# задание 2
# class TriangleChecker:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def is_triangle(self):
#         if self.a + self.b >= self.c:
#             print('треугольник можно построить')
#         elif self.a or self.b or self.c < 0:
#             print('с отрицательными нельзя')
#         elif self.a or self.b or self.c == str:
#             print('строку нельзя')
#         else:
#             self.a + self.b < self.c
#             print('нельзя построить')
#
#
# triangle1 = TriangleChecker(2, 3, 4)
#
# print(triangle1.is_triangle())


# задание 3
class KgToPounds:
    def __init__(self, kg):
        self.__kg = kg
    @property
    def kg(self):
        return self.__kg
    @kg.setter
    def kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            raise ValueError('килограммы задаются числами')

    def to_pounds(self):
        return self.__kg * 2.205

kgtopd1 = KgToPounds(10)
print(kgtopd1.kg)
kgtopd1.kg = 5
print(kgtopd1.kg)
print(kgtopd1.to_pounds())