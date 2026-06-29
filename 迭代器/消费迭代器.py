class Countdown:
    '''可迭代对象：倒数'''

    def __init__(self,start):
        self.num = start

    def __iter__(self):
        return CountdownIter(self.num)

class CountdownIter:
    '''迭代器'''
    def __init__(self,num):
        self.count = num
    def __iter__(self):
        return self
    def __next__(self):
        if self.count < 0:
            raise StopIteration("没有变量可再迭代了")
        num = self.count
        self.count -= 1
        return num
it = iter(Countdown(3))

# 消费迭代器,for在消费迭代器的时候实际上是在调用迭代器的__next__方法
print("-----------消费迭代器------------")
for num in it:
    print(num)
    # 上面for循环已经把迭代器it给消费完了，所以下面的for再去消费it迭代器时就只
for num in it:
    print(num)

print("-----------消费可迭代对象------------")
# 消费可迭代对象，for在消费可迭代对象的时候每次都会调用可迭代对象的__iter__方法返回一个新的迭代器
cd = Countdown(3)
for num in cd:
    print(num)
for num in cd:
    print(num)

arr = list(Countdown(3))
tuple1 = tuple(Countdown(3))
set1 = set(Countdown(3))
print(arr,tuple1,set1)


first, *rest = Countdown(3)
print(first,rest)
print([*Countdown(3)])

print(all([1,2,0,4]))

'''
param1：开始数字 param2：结束数字（遵从左闭右开原则param2最大值是param2-1） param3：步长
range(param1,param2,param3)
'''
for i in range(10):
    print(i,end=" ")
print("")
for i in range(3,10):
    print(i,end=" ")
print("")
for i in range(0,10,2):
    print(i,end=" ")
print("")
# 负数步长（倒序），当步长为-1时，param1必须大于param2才能执行
for i in range(5,0,-1):
    print(i,end=" ")
