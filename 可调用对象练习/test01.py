class Counter:
    init_val = 0
    def __init__(self,value):
        self.init_val = value
        self.val = value
    def __call__(self):
        self.val += 1
        return self.val
    def get(self):
        return self.val
    def reset(self):
        self.val = self.init_val
    
c = Counter(10)
print(c())      # 11
c()             # 12
print(c.get())  # 12
c.reset()
print(c.get())  # 10