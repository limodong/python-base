class Connect:
    def __init__(self,key):
        self.key = key

class ConnectPoolFactory:
    pool = {}
    def __new__(cls,conn_id):
       is_exist = cls.pool.get(conn_id,False)
       if is_exist == False:
           cls.pool[conn_id] = {}
       return cls.pool[conn_id]

    def __init__(self):
        print("初始化完成！")


connect_pool = ConnectPoolFactory("1")
connect_pool2 = ConnectPoolFactory("2")
connect_pool3 = ConnectPoolFactory("1")
print(connect_pool is connect_pool3)