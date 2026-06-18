class LazyProperty:
    
    def __init__(self,func):
        self.func = func
        self.name = func.__name__

    def __get__(self, instance, owner):
        print("执行非数据型描述符 __get__")
        if instance is None:
            return self
        if self.name in instance.__dict__:
            return instance.__dict__[self.name]
        value = self.func(instance)
        instance.__dict__[self.name] = value
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        print(f"__set__{value}")
        instance.__dict__[self.name] = value
    def __delete__(self, instance):
        del instance.__dict__[self.name]

class Test:
    def __init__(self):
        pass

    @LazyProperty
    def data(self):
        print("做只需要一次计算，后续可以反复使用的业务")
        return (1,2,3,4,5)

test = Test()

print(test.data)
print("=============================")
print(test.data,Test.data)
# del test.data
test.data = (4,5,6,7,8,9)
print(test.data)