"""
素数（质数） 是指在大于 1 的自然数中，除了 1 和它本身以外不再有其他因数的数。例如：2、3、5、7、11 都是素数，而 4、6、8、9 则不是。
编写一个程序，要求如下：
1. 用户输入：通过 input() 函数获取起始数字和结束数字。
2. 输入合法性检查：
  ○ 输入必须是正整数（大于 0 的整数）
  ○ 结束数字必须大于起始数字
  ○ 如果输入不合法，给出相应提示并要求重新输入
3. 素数判断：使用循环判断该范围内每个数字是否为素数。
4. 输出结果：打印该范围内的所有素数，并统计素数的个数。
"""

num_start = 0
num_end = 0
while num_start < 0 or num_end < 0 or num_start >= num_end:
    num_start = int(input("请输入起始数字："))
    num_end = int(input("请输入结束数字："))
    if num_start > 0 and num_end > 0 and num_start < num_end:
        break
    else:
        print("输入不合法！起始数字和结束数字不能为负整数，结束数字必须大于起始数字")
print(f"{num_start} 到 {num_end} 之间的素数有：")
while num_start <= num_end:
    if num_start == 2:
        print(f"")
    else:
        n = num_start % 2
