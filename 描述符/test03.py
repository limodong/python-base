# 编写一个描述符，记录某个类属性被访问和修改的次数：

class AccessCounter:
    access_count = 0
    modify_count = 0

    @staticmethod
    def get_access_count():
        return AccessCounter.access_count
    @staticmethod
    def get_modify_count():
        return AccessCounter.modify_count

    def __init__(self,value):
        self.init_value = value
    
    def __set_name__(self,owner,name):
        self.name = name
    
    def __set__(self, instance, value):
        instance._value = value
        self.modify_count += 1
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.init_value is not None:
            instance._value = self.init_value
        self.access_count += 1
        return instance._value



class MyClass:
    value = AccessCounter(10)  # 初始值为 10


obj = MyClass()
print(obj.value)      # 10
print(obj.value)      # 10
obj.value = 20
print(obj.value)      # 20

# 查看访问和修改次数
print(AccessCounter.get_access_count())   # 3（被访问了 3 次）
print(AccessCounter.get_modify_count())   # 1（被修改了 1 次）