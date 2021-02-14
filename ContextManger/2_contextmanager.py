"""
使用@contextmanager 装饰器能更方便创建上下文管理器

在使用 @contextmanager 装饰的生成器中，需要使用yield 语句的作用是把函
数的定义体分成两部分：yield 语句前面的所有代码在 with 块开始时
（即解释器调用 __enter__ 方法时）执行， yield 语句后面的代码在
with 块结束时（即调用 __exit__ 方法时）执行
"""

import contextlib

@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    yield 'JABBERWOCKY' # yield之前的代码在with块开始时执行，之后的代码在with块结束时执行
    sys.stdout.write = original_write


if __name__ == '__main__':
    # 执行yield之前的代码，在yield出暂停
    with looking_glass() as what:
        print('Alice, Kitty and Snowdrop') # pordwonS dna yttiK ,ecilA
        print(what) # YKCOWREBBAJ
    # 执行yield语句之后的代码，还原回 sys.stdout.write 方法
    print(what) # JABBERWOCKY