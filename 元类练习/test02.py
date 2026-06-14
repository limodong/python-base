# 定义一个元类，元类中有一个字典用来维护使用元类所创建的类,字典的key值是自定义类的名字，字典的value值是自定义类
class PluginMeta(type):
    registered = {}
    # mcs:PluginMeta元类,name：需要创建类的名字，bases：所创建类的父类元组，namespace：创建类的成员变量字典
    def __new__(mcs,name,bases,namespace):
        cls = super().__new__(mcs,name,bases,namespace)
        if name != "Plugin":
            PluginMeta.registered[name] = cls
        return cls
        
class Plugin(metaclass=PluginMeta):
    pass
class ImagePlugin(Plugin):
    pass
class VideoPlugin(Plugin):
    pass
print(PluginMeta.registered)