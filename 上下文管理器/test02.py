# 编写一个 TempDirectory 上下文管理器，进入时创建临时目录，退出时自动删除
import tempfile
import shutil
'''
tempfile 和 shutil 是 Python 中用于文件系统操作的标准库
- tempfile模块 用来 生成临时文件与目录，解决名称冲突与清理问题。
- shutil 模块 提供文件和目录的高级操作，如复制、移动、删除（整个目录树）、权限修改、查看磁盘等
'''

class TempDirectory:
    def __enter__(self):
        # 创建临时目录，返回路径
        self.tmp_dir = tempfile.mkdtemp()
        return self.tmp_dir

    def __exit__(self, exc_type, exc_val, exc_tb):
        
        # 退出时删除整个目录树
        shutil.rmtree(self.tmp_dir)
        # 返回 False 表示不抑制异常（如果有异常仍会向上抛出）
        return False


with TempDirectory() as tmp_dir:
    print(f"临时目录: {tmp_dir}")
    # 可以在这个目录中创建文件，比如：
    # with open(os.path.join(tmp_dir, 'test.txt'), 'w') as f:
    #     f.write('hello')

print("临时目录已清理")