"""
任务 1：列表扁平化
实现函数 flatten，接收一个可能包含嵌套列表的列表（如 [1, [2, 3], [[4], 5]]），返回一个将所有元素展开后的一维列表（如 [1, 2, 3, 4, 5]）。

任务 2：列表/元组转链表
实现函数 to_linked_list，接收一个列表或元组，将其转换为一个链表结构并返回。

任务 3：字典合并
实现函数 merge_dicts，接收不定数量的字典参数，将它们合并为一个大字典。
合并规则：求并集，如果有相同的键，后传入的字典中的值覆盖先传入的字典中的值（浅合并即可）
"""

# def flatten(arr, result=[]):
#     for item in arr:
#         if type(item) == list:
#             flatten(item, result)
#         else:
#             result.append(item)
#     return result


# print(flatten([1, [2, 3], [[4], 5]]))


def to_linked_list(arr, node={"value": "", "next": None}, i=0):
    node["value"] = arr[i]
    i += 1
    if len(arr) > i:
        node["next"] = {"value": arr[i], "next": None}
        to_linked_list(arr[i:], node["next"])
    return node


print(to_linked_list((1, 2, 3)))

# def merge_dicts(*arr)
