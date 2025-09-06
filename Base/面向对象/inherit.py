class Base:
    name = None

    def __init__(self, _name='111'):
        self.name = _name

    def func(self):
        print(f"name is {self.name}")


def __f():
    print("This is a private method")


class Son(Base):
    age = None

    def __init__(self, name, age):
        super().__init__(name)  # 推荐用 super 调父类构造函数
        self.age = age

    def func(self):
        print(f"Son name is {self.name}, Son age is {self.age}")


base = Base('222')
son = Son(name='wo', age=12)

base.func()  # → name is 222
son.func()  # → Son name is wo, Son age is 12
super(Son, son).func()  # → name is wo  (调用父类方法)
#son._Son__f()  # → This is a private method
