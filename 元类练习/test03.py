# 创建一个元类，由元类创建的自定义类在调用成员变量之前打印'LOG [成员变量名称]'，不可被调用的成员变量不需要打印
class LogMeta(type):
    def __new__(mcs,name,bases,namespace):
        
        for key,value in namespace.items():
            # key不以下划线开头且还要是能被调用的对象
            if not key.startswith("_") and callable(value):
                # 使用一个新函数包装以前的旧的函数后返回一个新的包装后的函数
                namespace[key] = mcs.log_wrapper(value)
        cls = super().__new__(mcs,name,bases,namespace)
        return cls
    
    @staticmethod
    def log_wrapper(func):
        def wrapper(*args,**kwargs):
            print(f"[LOG] 调用 {func.__name__}")
            return func(*args,**kwargs)
        return wrapper
class Calculator(metaclass=LogMeta):
    def add(self, a, b):
        return a + b
    
    def sub(self, a, b):
        return a - b

calc = Calculator()
print(calc.add(3, 5))
print(calc.sub(10, 4))
