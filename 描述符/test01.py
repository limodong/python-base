#编写一个类 `ImmutablePoint`，创建后不能修改坐标

class ImmutablePoint:
    @property
    def x(self):
        return self.__dict__["x"]
    @x.setter
    def x(self,value):
        if "x" in self.__dict__:
            raise AttributeError("AttributeError! 不能修改只读属性")
        self.__dict__["x"] = value
    
    @property
    def y(self):
        return self.__dict__["y"]
    @y.setter
    def y(self,value):
        if "y" in self.__dict__:
            raise AttributeError("AttributeError! 不能修改只读属性")
        self.__dict__["y"] = value

    def __init__(self,val_x,val_y):
        self.x = val_x
        self.y = val_y
        

p = ImmutablePoint(3, 4)
print(p.x)      # 3
print(p.y)      # 4

p.x = 10      # AttributeError! 不能修改只读属性