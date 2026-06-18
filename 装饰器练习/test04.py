def cache(func):
    _cache_dict = {}
    def wrapper(*args,**kwargs):
        
        key = (args,tuple(kwargs.items()))
        if key not in _cache_dict.keys():
            _cache_dict[key] = func(*args,**kwargs)
        return _cache_dict[key]
        
    return wrapper
    

@cache
def fibonacci(n):
    if n < 3:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(35))  # 应该快速返回结果