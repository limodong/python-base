"""
实现一个函数 create_account(initial_balance)，返回两个字典：
● deposit(amount): 存款，返回新余额
● withdraw(amount): 取款，余额不足返回 "余额不足"，否则返回新余额
要求使用闭包保存余额状态，不要暴露余额变量。
"""


def create_account(initial_balance):
    def add(num):
        nonlocal initial_balance
        initial_balance += num
        return initial_balance

    def decrease(num):
        nonlocal initial_balance
        if initial_balance < num:
            return "余额不足"
        else:
            initial_balance -= num
            return initial_balance

    return [add, decrease]


deposit, withdraw = create_account(100)
print(deposit, withdraw)
print(deposit(50))  # 150
print(withdraw(30))  # 120
print(withdraw(200))  # 余额不足

deposit2, withdraw2 = create_account(50)
print(deposit2(10))  # 60 —— 独立的账户
