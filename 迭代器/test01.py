# 编写一个生成器函数 flatten，将嵌套的列表扁平化：
def flattn(nested_list):
    for item in nested_list:
        if isinstance(item,list):
            yield from flattn(item)
        else:
            yield item
nested = [1, [2, [3, 4], 5], 6, [7, 8]]
print(list(flattn(nested)))