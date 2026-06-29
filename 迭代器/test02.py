# 编写一个生成器，模拟从数据库分页读取数据
def paginated_query(total_items,page_size):
    '''
    模拟分页查询
    total_items：总数据量
    page_size：每页大小
    每次yield返回一页数据（列表）
    '''
    num = total_items % page_size
    arr = [ x for x in range(0,total_items,page_size)]
    arr.append((arr[len(arr)-1] + num))
    startIndex = 0
    for i in range(1,len(arr)):
        yield [ x for x in range(startIndex,arr[i])]
        startIndex = arr[i]

for page in paginated_query(25,10):
    print(page)