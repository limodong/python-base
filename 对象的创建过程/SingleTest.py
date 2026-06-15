class DB():
    data = None
    def __new__(cls,*args):
        if cls.data is None:
            return super().__new__(cls)
        return cls.data
    
    def __init__(self,db_name,account,pwd):
        self.db_name = db_name
        self.account = account
        self.pwd = pwd
        print("数据库初始化完成。。。")

db = DB("mysql","root","root")
print(db.__dict__)
