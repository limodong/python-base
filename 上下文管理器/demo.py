from contextlib import contextmanager
class my_open:
    def __enter__(self):
        print("__enter__")
    def __exit__(self, exc_type, exc, tb):
        print("__exit__")

with my_open() as mo:
    # 先执行__enter__方法
    print("12312321") # 再执行代码部分
    #代码部分执行完之后再执行__exit__方法



class DatabaseServer:
    def __init__(self,host,name):
        self.host = host
        self.name = name

    @contextmanager
    def connect(self):
        '''使用生成器实现上下文管理器'''
        print(f"获取资源：{self.name}")
        try:
            # 执行__enter__方法
            yield "success" 
        finally:
            # __exit__方法会在finally中运行
            print(f"释放资源：{self.name}")
        

db = DatabaseServer("localhost","mysql")
with db.connect() as result:
    print(result)


@contextmanager
def safe_file_write(file_path):
    """安全写入文件：先写入临时文件，成功后再替换原文件"""
    temp_path = file_path + ".tmp"
    try:
        f = open(temp_path, "w")
        yield f
        f.close()
        # 写入成功，替换原文件
        import os
        os.replace(temp_path, file_path)
        print("写入成功")
    except Exception as e:
        # 写入失败，清理临时文件
        f.close()
        import os
        if os.path.exists(temp_path):
            os.remove(temp_path)
        print(f"写入失败: {e}")
        raise  # 重新抛出异常


# 使用
with safe_file_write("data.txt") as f:
    print("开始写入。。。")
    f.write("Hello, World!\n")