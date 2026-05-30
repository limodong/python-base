class Animal:
    count = 0

    def __init__(slef, name):
        Animal.count += 1
        slef.name = name

    def eat(slef):
        print("eat food ...")

    def speak(slef):
        print(f"{slef.name} 在叫...")

    @classmethod
    def hello(cls):
        print("hello world!!!")

    @classmethod
    def get_count(cls):
        return cls.count


class Dog(Animal):
    def __init__(self):
        super().__init__("狗")


class Cat(Animal):
    def __init__():
        super().__init__("猫")


print(type(Animal))
_animal = Animal("动物")
print(type(_animal))
_animal.eat()
_animal.hello()
print(Animal.get_count())
dog = Dog()
print(Dog.get_count())
dog.speak()
print(isinstance(dog, object))
print(Dog.__base__, dog.__class__)
print(vars(dog.__class__))
