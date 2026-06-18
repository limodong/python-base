import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    # @property装饰器可以将一个函数变成一个只读的属性描述符
    @property
    def radius(self):
        return self._radius
    
    # @<属性名>.setter 可以让只读的属性变得可以修改 
    @radius.setter
    def radius(self,value):
        if (value < 0):
            raise AttributeError("radius半径不能为负数")
        self._radius = value

    # @<属性名>.deleter 可以让属性被删除（属性名必须和@property修饰的可调用对象名称保持一致）
    @radius.deleter
    def radius(self):
        raise AttributeError("radius半径不能被删除")
    
    @property
    def area(self):
        return self._radius**2 * math.pi
    
    @property
    def diameter(self):
        return self._radius * 2
    
circle = Circle(10)
print(circle.radius,circle.area,circle.diameter)