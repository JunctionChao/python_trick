"""
python 通过下划线的命名规范来控制属性的访问

_单下划线开头：弱“内部使用”标识，如：from M import *，将不导入所有以下划线开头的对象，包括包、模块、成员
__双下划线开头双下划线结尾__：指那些包含在用户无法控制的命名空间中的“魔术”对象或属性，如类成员的__name__ 、__doc__、__init__、__import__、__file__、等。推荐永远不要将这样的命名方式应用于自己的变量或函数
__双下划线开头：模块内的成员，表示私有成员，外部无法直接调用
单下划线结尾_：只是为了避免与python关键字的命名冲突
"""

class A:
    def __init__(self, x):
        self.__x = x

if __name__ == '__main__':
    a = A(3)
    # print(a.__x) # AttributeError: 'A' object has no attribute '__x'
    # 其实系统内部进行了命名重整，可以在属性名前加下划线和类名称 _class
    print(a._A__x) # 3