# 一个可迭代对象可以通过iter()可以返回一个迭代器。
# 如果想要一个对象称为可迭代对象，即可以使用for，那么必须实现__iter __()方法。
# 在一个类的实例对象想要变成迭代器，就必须实现__iter__()和__next__()方法。
# 调用iter()时，在对象内部默认调用__iter__()，即__iter__()的返回值应该是一个迭代器。
# for的每次循环中或者next()时，都是自动调用迭代器的__next__()方法，并有一个返回值

class Classmate():
    def __init__(self):
        self.names = list()

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        return ClassIterator(self)


class ClassIterator():
    def __init__(self, obj):
        self.obj = obj
        self.current_num = 0 

    def __iter__(self):
        pass

    def __next__(self):
        if self.current_num < len(self.obj.names):
            ret = self.obj.names[self.current_num]
            self.current_num += 1
            return ret
        else:
            raise StopIteration

if __name__ == "__main__":
    c = Classmate()
    for i in range(4):
        c.add("name_"+str(i))

    for name in c:
        print(name)