class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "汪汪！"


class Cat(Animal):
    def speak(self):
        return "喵喵！"


class Duck(Animal):
    def speak(self):
        return "嘎嘎！"


# 使用多态
def make_animal_speak(animal: Animal):
    print(animal.speak())


animals = [Dog(), Cat(), Duck()]

for a in animals:
    make_animal_speak(a)
