'''
callable 用来判定是否是一个函数，如果是则返回True，反之返回False
'''
print(callable(len))
print(callable(1))
print(callable([1,2]))
print(callable(lambda: 1))

print("-------------------------")
class A:
    def __init__(self):
        print("123")
        pass
    # 因为__call__是一个实例方法，所以只有实例化对象后调用才会生效
    def __call__(self): 
        print("__main__")

print(callable(type(A)))
print(callable(A))
a = A()
a() # 调用实例化对象的__call__()函数

print("=============使用__call__函数来创建类似js中的高阶函数=============")
class Adder:
    def __init__(self,n):
        self.n = n

    def __call__(self,n2):
        return self.n + n2

adder = Adder(2)
print(adder(3))