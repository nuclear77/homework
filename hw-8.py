# задача 1
# class Auto:
#     def __init__(self, brand, age, color, mark, weight):
#         self.brand = brand
#         self.age = age
#         self.color = color
#         self.mark = mark
#         self.weight = weight
#
#     def move(self):
#         print("move")
#
#     def birthday(self):
#         self.age += 1
#
#     def stop(self):
#         print("stop")
#
#
# # задача 2
# class Truck(Auto):
#     def __init__(self, brand, age, color, mark, weight, max_load):
#         super().__init__(brand, age, color, mark, weight)
#         self.max_load = max_load
#
#     def move(self):
#         print("attention")
#         super().move()
#
#     def load(self):
#         import time
#         time.sleep(1)
#         print("load")
#         time.sleep(1)

# class Car(Auto):
#     def __init__(self, brand, age, color, mark, weight, max_speed):
#         super().__init__(brand, age, color, mark, weight)
#         self.max_speed = max_speed
#
#     def move(self):
#         super().move()
#         print("max speed is", self.max_speed)
#
#
# truck1 = Truck("Mercedes", 5, "Red", "Truck", 2000, 5000)
# truck2 = Truck("Mini", 3, "Blue", "Truck", 3000, 7000)
# truck1.move()
# truck1.birthday()
# print(truck1.age)
# truck1.load()
#
# truck2.stop()
# print(truck2.brand)
# print(truck2.color)
# print(truck2.max_load)
#
# car1 = Car("Toyota", 2, "Black", "Car", 1500, 200)
# car2 = Car("BMW", 4, "White", "Car", 1800, 250)
# car1.move()
# car1.birthday()
# print(car1.age)
#
# car2.stop()
# print(car2.mark)
# print(car2.max_speed)


# задача 3
class Circle:
    def __init__(self, a):
        self.radius = a

    def circle_area(self):
        return 3.14 * self.radius ** 2


class Figure:

    def sub(self):
        a = [c.circle_area(), c_1.circle_area()]
        x = a[0] - a[1]
        print(x)

    def sub_m(self):
        a = [c.radius, c_1.radius]

        if a[0] == a[1]:
            print(p.Point())
        else:
            x = a[0] - a[1]
            modul = x + 1
            z = x % modul
            if z > modul:
                z -= modul
            print(z)


class Point:
    def Point(self):
        return '.'


p = Point()
number_1 = int(input('введите первый радиус'))
number_2 = int(input('введите второй радиус'))
c = Circle(number_1)
c_1 = Circle(number_2)

f = Figure()
f.sub()
f.sub_m()
