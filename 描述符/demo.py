# 属性描述符
class MyDescrptor:

    def __set_name__(self,owner,name):
        print(f"__set_name__ called with owner={owner}, name={name}")

    #  owner：是一个类，这个类是调用这个属性描述符的类， instance：是一个实例对象，是owner类实例化的对象，self：MyDescrptor，描述符本身的类
    def __get__(self, instance, owner):
        print("call __get__ ......")
        pass
    def __set__(self, instance, value):
        print("call __set__ ......")
        pass
    def __delete__(self, instance):
        print("call __delete__ ......")
        pass

class MyClass:
    
    num = MyDescrptor() # num是一个属性描述符
    def __init__(self,value):
        self.num = value

ins = MyClass(109)
# ins.num = 99
print(ins.num) # 实际实在调用MyDescrptor.__get__(MyDescrptor,ins,MyClass)
del ins.num