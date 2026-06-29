from contextlib import contextmanager

@contextmanager
def timer(text):
    import time
    start = time.time()
    try:
        yield
    finally:
        use_time = time.time() - start
        print(f"{text} 耗时：{use_time:.5}")

with timer("数据处理"):
    import time
    time.sleep(1)
    print("处理完成")