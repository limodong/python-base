class Typed:
    """强制类型检查的描述符"""
    
    # expected_type 是数据的类型（str | int | float）
    def __init__(self, expected_type):
        self.expected_type = expected_type
        self.name = None

    def __set_name__(self, owner, name):
        # 保存描述符的名称
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        # 判断赋值的类型是否与描述符的类型一致，不一致报错
        if not isinstance(value, self.expected_type):
            raise TypeError(
                f"{self.name} 必须是 {self.expected_type.__name__} 类型，"
                f"而不是 {type(value).__name__}"
            )
        instance.__dict__[self.name] = value


class Student:
    name = Typed(str)
    age = Typed(int)
    score = Typed(float)

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student("Alice", 20, 85.5)
# s.age = "20"      # TypeError! age 必须是 int 类型，而不是 str