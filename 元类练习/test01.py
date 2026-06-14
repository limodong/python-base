# 创建一个单例元类，使用这个单例元类定义的类在实例化后，实例化的对象始终只有一个，就算将类多次实例化始终只会生成一个对象
# ***元类必须继承type
class SingletonMeta(type):
    # 由于这是一个公共元类，所以可以用一个私有字典来将缓存类的实例化对象
    _instance = {}
    # 元类__call__中的self指的时创建实例的类对象，而不是实例对象，所以这里把self改名字为cls（class的缩写）
    def __call__(cls, *args, **kwds):
        # cls类的实例化，cls() ==等价于==> type(cls)__call__(参数) 
        ins = super().__call__(*args,**kwds)
        # 如果这个类不在字典中，就添加到字典中并返回
        if cls not in SingletonMeta._instance:
            SingletonMeta._instance[cls] = ins
        return SingletonMeta._instance[cls]

class DataBase(metaclass=SingletonMeta):
    def __init__(self,host):
        self.host = host

data_base1 = DataBase("Mysql")
data_base2 = DataBase("DM")
print(data_base1 is data_base2)
print(data_base2.host)