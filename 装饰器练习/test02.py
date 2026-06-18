# 需要返回一个装饰器
def wraps(originFunc):
    # wraps_decroator是一个装饰器
    def wraps_decroator(func):
        # wrapper是最终需要执行的函数（最终装饰say_hello的函数）
        def wrapper(*args,**kwargs):
            print("11111111111",func.__name__,originFunc.__name__)
            return func(*args,**kwargs)
        # 把原函数的名称和注释赋值给新函数的名称和注释
        wrapper.__name__ = originFunc.__name__
        wrapper.__doc__ = originFunc.__doc__
        return wrapper
        
    return wraps_decroator

def my_decorator(func):
    # @wraps(func) 这个是一个函数调用，返回一个装饰器
    @wraps(func)
    def wrapper():
        print("函数执行前")
        func()
        print("函数执行后")
    # wrapper.__name__ = func.__name__
    # wrapper.__doc__ = func.__doc__
    return wrapper

@my_decorator
def say_hello():
    '''打招呼'''
    print("Hello!")

say_hello()
print("name ",say_hello.__name__)
print("doc ",say_hello.__doc__)
