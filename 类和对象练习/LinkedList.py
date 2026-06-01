"""
请实现一个单链表类 LinkedList，支持以下操作：
需要实现的方法：
方法	说明
__init__(data=None)	初始化空链表；data 可以是列表、元组或集合，其中的值会被初始化为链表的节点
traverse(callback)	遍历链表，对每个节点值调用 callback(index, value)
__str__()	返回链表的字符串表示，如 "1 -> 2 -> 3"
to_list()	将链表转换为 Python 列表并返回
append(value)	在链表尾部添加一个新节点
prepend(value)	在链表头部添加一个新节点
insert(index, value)	在指定索引位置插入新节点，索引从 0 开始
delete_by_value(value)	删除第一个值等于 value 的节点，返回是否删除成功
delete_by_index(index)	删除指定索引位置的节点，返回被删除的值，索引越界时返回 None
find(value)	查找值等于 value 的节点，返回其索引，不存在返回 -1
get(index)	获取指定索引位置的值，索引越界时返回 None
get_length()	返回链表长度
is_empty()	判断链表是否为空
提示： 你可能需要先定义一个 Node 类来表示链表节点。
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, data=None):
        self.lienked_list = []
        if isinstance(data, list) or isinstance(data, set) or isinstance(data, tuple):
            if len(data) != 0:
                for value in data:
                    self.append(value)

    # 遍历链表，对每个节点值调用 callback(index, value)
    def traverse(self, callback):
        for index, item in enumerate(self.lienked_list):
            callback(index, item.value)

    # 返回链表的字符串表示，如 "1 -> 2 -> 3"
    def __str__(self):
        str = ""
        for index, node in enumerate(self.lienked_list, 1):
            str += node.value
            if index < len(self.lienked_list):
                str += " -> "
        return str

    # 将链表转换为 Python 列表并返回
    def to_list(self):
        node_list = list(map(lambda item: item.value, self.lienked_list))
        return node_list

    # 在链表尾部添加一个新节点
    def append(self, value):
        node = Node(value)
        self.lienked_list.append(node)
        prev_node_idx = self.get_length() - 2 if self.get_length() > 1 else -1
        if prev_node_idx != -1:
            self.lienked_list[prev_node_idx].next = node

    # 在链表头部添加一个新节点
    def prepend(self, value):
        node = Node(value)
        if self.get_length() != 0:
            node.next = self.lienked_list[0]
        self.lienked_list.insert(0, node)

    # 在指定索引位置插入新节点，索引从 0 开始
    def insert(self, index, value):
        node = Node(value)
        prev_node_index = 0 if index == 0 else index - 1
        node.next = self.lienked_list[prev_node_index]
        self.lienked_list.insert(index, node)

    # 删除第一个值等于 value 的节点，返回是否删除成功
    def delete_by_value(self, value):
        del_idx = None
        for index, item in enumerate(self.lienked_list):
            if value == item.value:
                del_idx = index
                break
        if del_idx != None:
            next_node = self.lienked_list[del_idx].next
            prev_node = self.lienked_list[del_idx - 1]
            del self.lienked_list[del_idx]
            if next_node != None and prev_node != None and del_idx != 0:
                prev_node.next = next_node
                return True
        return False

    # 删除指定索引位置的节点，返回被删除的值，索引越界时返回 None
    def delete_by_index(self, index):
        if self.get_length() < index or index < 0:
            return None
        node = self.lienked_list[index]
        print(f"delete_by_index ---> {node.value}")
        del self.lienked_list[index]
        return node.value

    # 查找值等于 value 的节点，返回其索引，不存在返回 -1
    def find(self, value):
        for index, item in enumerate(self.lienked_list):
            if item.value == value:
                return index
        return -1

    # 获取指定索引位置的值，索引越界时返回 None
    def get(self, index):
        return (
            self.lienked_list[index].value
            if index >= 0 and index < len(self.lienked_list)
            else None
        )

    # 返回链表长度
    def get_length(self):
        return len(self.lienked_list)

    # 判断链表是否为空
    def is_empty(self):
        return self.get_length() == 0


# linked_list = LinkedList()
# linked_list.append("a")
# linked_list.append("b")
# linked_list.append("c")
# print(linked_list.__str__())
# print(linked_list.get(1).next.value)
# linked_list.insert(0, "0")
# print(linked_list.to_list())
# print(linked_list.delete_by_index(1))
# print(linked_list.to_list())
# print("===========================================")
linked_list2 = LinkedList(["x", "c", "v"])
linked_list2.prepend("z")
linked_list2.append("b")
print(f"{linked_list2}")
print(linked_list2.to_list())


def fn(idx, item):
    print(idx, item)


linked_list2.traverse(fn)

print(linked_list2.find("c"))
print(linked_list2.get(2))
print(linked_list2.delete_by_value("c"))
print(linked_list2.to_list())

# print(linked_list2.__str__())
