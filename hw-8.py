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


# задача 2
# class Truck(Auto):
#     def __init__(self, brand, age, color, mark, weight, max_load):
#         super().__init__ (brand, age, color, mark, weight)
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
#
# class Car(Auto):
#     def __init__(self, brand, age, color, mark, weight, max_speed):
#         super().__init__(brand, age, color, mark, weight)
#         self.max_speed = max_speed
#
#     def move(self):
#         super().move()
#         print("max speed is", self.max_speed)
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
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def subtract(self, other_circle):
        if self.radius != other_circle.radius:
            new_radius = abs(self.radius - other_circle.radius)
            return Circle(self.x, self.y, new_radius)
        else:
            return Point(self.x, self.y)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

circle1 = Circle(0, 0, 5)
circle2 = Circle(0, 0, 3)
circle3 = Circle(0, 0, 5)

result1 = circle1.subtract(circle2)
result2 = circle1.subtract(circle3)

print(result1.radius)
print(result2.x, result2.y)