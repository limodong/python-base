# 编写一个 `Temperature` 类，温度必须在 -273.15（绝对零度）到 1000 之间

class Temperature:
    @property
    def celsius(self):
        return self._celsius
    @celsius.setter
    def celsius(self,value):
        if value <= -300:
            raise ValueError("ValueError! 温度不能低于绝对零度")
        self._celsius = value
    @property
    def fahrenheit(self):
        return self._celsius * 3.08
    @property
    def kelvin(self):
        return self._celsius * 11.926

    def __init__(self,value):
        self.celsius = value

t = Temperature(25)
print(t.celsius)      # 25
print(t.fahrenheit)   # 77.0（只读属性，自动计算）
print(t.kelvin)       # 298.15（只读属性，自动计算）

t.celsius = -300    # ValueError! 温度不能低于绝对零度