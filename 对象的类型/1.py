def a():
    pass


b = lambda: None


class A:
    @classmethod
    def foo(cls):
        pass


function = type(lambda: None)

print(type(A))  # <class 'type'>

print(isinstance(function, object))


# 普通函数
def func():
    pass


print("type(func)", type(func))  # <class 'function'>
print("isinstance(func, object)", isinstance(func, object))  # True
print("isinstance(func, type)", isinstance(func, type))  # True
print("isinstance(func, function)", isinstance(func, function))  # True
