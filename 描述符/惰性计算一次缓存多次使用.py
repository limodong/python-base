class LazyProperty:
    # func就是Test类中的data函数
    def __init__(self,func):
        self.func = func
        self.name = func.__name__ # 就是Test类中的data函数的名称也就是"data"
    def __get__(self, instance, owner):
        # 如果是通过类直接去调用就直接返回LazyProperty（也就是说直接用Test.data 去访问直接返回描述符）
        if instance is None:
            return self
        value = self.func(instance)
        # 往实例对象中的__dict__中添加属性data，且data的值是value
        setattr(instance,self.name,value)
        return value

class Test:

    # 使用@LazyProperty标记后，data就是一个描述符属性了，后面可以直接使用数据的方式去调用。instance.data即可
    @LazyProperty
    def data(self):
        print("这里可以做一些只需要执行一次的处理，后续可以直接调用缓存的数据")
        catch = (1,2,3,4,5)
        return catch
    
test = Test()
print(test.data)
print("----------------------")
# 因为LazyProperty中只有__get__所以它是一个非数据型属性描述符，它在属性查找时会优先从实例属性__dict__中查找，如果存在就直接返回
print(test.data)