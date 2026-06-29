# 迭代器
'''
首先得是一个对象，且对象拥有__iter__方法和__next__方法那么它就是一个迭代器，__iter__方法返回的是自身
'''
class FibonaccicIter:
    def __init__(self):
        self.a = 1
        self.b = 1
    def __iter__(self):
        return self
    def __next__(self):
        current = self.a
        self.a = self.b
        self.b = current + self.b
        return current
fibo = FibonaccicIter()
print(fibo.__next__())
print(fibo.__next__())
print(fibo.__next__())
print(fibo.__next__())
print(fibo.__next__())
print(fibo.__next__())
print(fibo.__next__())
print(fibo.__next__())


# 可迭代对象
'''
一个对象拥有__iter__方法，且返回一个迭代器，那么就是一个可迭代对象
'''
class FibonaccicObj:
    def __iter__(self):
        return FibonaccicIter()

print("---------------------------------------")
fb = FibonaccicObj()
it = iter(fb) # 通过内置的iter方法，把可迭代对象传入就可以得到一个新的迭代器
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print("======================================")
it2 = iter(fb)
print(it2.__next__())
print(it2.__next__())
print(it2.__next__())
print(it2.__next__())
print(it2.__next__())
print(it2.__next__())
