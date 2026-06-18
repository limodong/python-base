import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        print(f"{func.__name__}执行时间：{(time.time() - start):.5}秒")
    return wrapper
    

@timer
def slow_function():
    time.sleep(1)
    return "Done"
slow_function()