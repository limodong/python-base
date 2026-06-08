'''
callable 用来判定是否是一个函数，如果是则返回True，反之返回False
'''
print(callable(len))
print(callable(1))
print(callable([1,2]))
print(callable(lambda: 1))

print("-------------------------")
class A:
    def __call__(self):
        print("__main__")

print(callable(type(A)))
print(callable(A))