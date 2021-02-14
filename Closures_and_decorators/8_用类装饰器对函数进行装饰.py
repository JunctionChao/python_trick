# 通过类装饰器或者类中的类方法等可以进行复杂功能的设计
class Decor():
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("执行装饰器功能")
        print("函数执行前的功能")
        ret = self.func(*args, **kwargs)
        print("函数执行后的功能")
        return ret


@Decor # get_str = Test(get_str)
def get_str():
    return "Hello"


if __name__ == '__main__':
    print(get_str())


"""
执行装饰器功能
函数执行前的功能
函数执行后的功能
Hello
"""
