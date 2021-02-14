"""
上下文管理器对象存在的目的是管理 with 语句

上下文管理器协议包含 __enter__ 和 __exit__ 两个方法。
with 语句开始运行时，会在上下文管理器对象上调用 __enter__ 方法
with 语句运行结束后，会在上下文管理器对象上调用 __exit__ 方法
"""

# sys.stdout.write()只能输出一个字符串str，而print()可以输出多个值，数据类型多样。
# print(obj)实际上是调用sys.stdout.write(obj+'\n')，因此print在打印时会自动加个换行符
# 可以通过help()去查看函数的使用

class LookingGlass:
    def __enter__(self):
        import sys
        self.original_write = sys.stdout.write # 先保存原来的方法
        sys.stdout.write = self.reverse_write # 为 sys.stdout.write 打猴子补丁，替换成自己编写的方法
        return 'JABBERWOCKY'
    def reverse_write(self, text):
        self.original_write(text[::-1])
    # 如果一切正常，调用 __exit__ 方法时传入的参数是 None, None, None；如果抛出了异常，这三个参数是异常数据
    def __exit__(self, exc_type, exc_value, traceback):
        import sys
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('Please DO NOT divide by zero!')
            return True


if __name__ == '__main__':
    # 执行__enter__方法，改变了 sys.stdout.write 方法
    with LookingGlass() as what:
        print('Alice, Kitty and Snowdrop') # pordwonS dna yttiK ,ecilA
        print(what) # YKCOWREBBAJ
    # 执行__enter__方法，还原回 sys.stdout.write 方法
    print(what) # JABBERWOCKY