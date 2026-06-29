'''生成器：拥有yield关键字的函数就是生成器，它返回一个迭代器'''
def simple_generator():
    print("123")
    yield 1
    print("456")
    yield 2
    print("789")
g = simple_generator()
#每次执行next方法时会直行到下一个yield关键字的地方并返回仅跟在yield后面的值
print(g.__next__())
val = next(g)
print(val)
# print(g.__next__()) # 当没有下一个yield关键字后就会抛出StopIteration，表示迭代器已经停止

# 改造Countdown迭代对象
class Countdown:
    def __init__(self,start):
        self.start = start
    
    def __iter__(self):
        def simple_gen():
            while self.start > 0:
                count = self.start
                self.start -= 1
                yield count
            raise StopIteration
        return simple_gen()
print("--------改造Countdown迭代对象--------")
cd = iter(Countdown(10))
print(type(cd))
print(type(Countdown(10)))
print(cd.__next__())
print(cd.__next__())
print(cd.__next__())
print(cd.__next__())
print(cd.__next__())
print(cd.__next__())
print(cd.__next__())

def countdown(start):
    while start > 0:
        yield start
        start -= 1
g = countdown(3)
print(next(g))
print(next(g))
print(next(g))
print("------发送数据------")
def calculator():
    total = 0
    while True:
        x = yield total
        if x is None:
            break
        total += x

c = calculator()
print(next(c))
num = c.send(10)
print(num)
