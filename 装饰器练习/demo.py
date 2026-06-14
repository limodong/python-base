import time

'''
装饰器：装饰器是一个可调用对象，且接受一个可调用对象。
        只要是一个可调用对象就可以作为参数传递给装饰器。（函数是一个可调用对象，类也是，所以类也可以作为参数传递给装饰器）
'''
def decorator(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time() - start
        # 在格式化文本中使用:.4来确定数字的精度，下面表示总共保留4个精度，从第一个数字开始（不是从小数位开始）
        print(f"消耗时间：{end:.2}秒")
    return wrapper
    

@decorator
def speak():
    print("Agent Loading")

speak()