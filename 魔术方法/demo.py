# 魔术方法：没有显示调用的方法，例如python中的__str__,__repr__等方法都是自动执行的，这类方法是魔术方法

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    ''' 在变量后添加!r后返回的结果会明确体现出该变量是一个什么类型 '''

    def __str__(self):
        ''' 面相用户的，友好的可读格式 '''
        return f"Point({self.x},{self.y})"
    
    def __repr__(self):
        ''' 面相开发者，返回的结果能一眼看出是什么类型的 '''
        return f"Point({self.x!r},{self.y!r})"
p = Point('1',2)
print(p)
print(str(p))
print(repr(p))
print(type(str(p)))
print(type(repr(p)))
print(type(eval(str(p))))
print(type(eval(repr(p))))