class DataClass:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def static_method():
        print("это статикметод")

    @classmethod
    def class_method(cls):
        print("это классметод")


DataClass.static_method()

DataClass.class_method()

class MetaClass(type):
    def __new__(cls, name, bases, attrs):
        attrs['new_atribute'] = "добавление нового атрибута в метакласс"
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=MetaClass):
    pass

obj2 = MyClass()

print(obj2.new_atribute)