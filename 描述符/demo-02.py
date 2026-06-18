import math


'''
    属性描述符

'''
class RadiusDescriptor:
    def __set_name__(self,owner,name):
        print(f"RadiusDescriptor __set_name__ {owner} __ {name}")

    # 只有存在__set__或__delete__就是数据型描述符
    def __set__(self, instance, value):
        print("radius __ call __set__")
        if value < 0:
            raise AttributeError("radius不能为负数!")
        instance._radius = value
    def __delete__(self, instance):
        print("call __delete__")
        raise AttributeError("radius不能被删除")
    
    # 如果只有__get__方法那就是非数据型描述符
    def __get__(self, instance, owner):
        print("radius __ call __get__")
        return instance._radius

class AreaDescriptor:
    def __set_name__(self,owner,name):
        print(f"AreaDescriptor __set_name__ {owner} __ {name}")
    def __set__(self, instance, value):
        print(f" area __ call __set__ ")
        raise AttributeError("area不能修改")
    def __delete__(self, instance):
        raise AttributeError("Area不能删除")
    def __get__(self, instance, owner):
        print("area __ call __get__")
        return instance._radius**2 * math.pi

class DiameterDescriptor:

    def __set_name__(self,owner,name):
        print(f"DiameterDescriptor __set_name__ {owner} __ {name}")

    def __set__(self, instance, value):
        raise AttributeError("diameter不能被修改")

    def __get__(self, instance, owner):
        print("diameter __ call __get__")
        return instance._radius * 2

    def __delete__(self, instance):
        raise AttributeError("diameter不能删除")

class Circle:
    radius = RadiusDescriptor()
    area = AreaDescriptor()
    diameter = DiameterDescriptor()
    def __init__(self,radius):
        self.radius = radius

circle = Circle(10)
print(circle.radius,circle.area,circle.diameter)
circle.radius = 20
# circle.diameter = 100
del circle.diameter
print(circle.radius,circle.area,circle.diameter)


""" class Circle:
    def __init__(self,radius):
        # 半径
        self.radius = radius
        # 面积
        self.area = radius**2 * math.pi
        #直径
        self.diameter = radius * 2

circle = Circle(5)
print(circle.radius,circle.area,circle.diameter) """