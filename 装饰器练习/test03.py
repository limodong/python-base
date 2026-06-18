# 定义一个生成装饰器的函数
def repeat(n):
    # func是被装饰器包装的原函数（say_hello）
    def repeat_decorator(func):
        i = 0
        # 最终执行的函数
        def wrapper(*args,**kwargs):
            nonlocal i
            while(i < n):
                func(*args,**kwargs)
                i += 1
        return wrapper
    #返回装饰器
    return repeat_decorator

@repeat(3)
def say_hello(s):
    print(s)


say_hello(1)  # 输出: 1 1 1