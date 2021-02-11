# 既是可迭代对象同时也是迭代器
class Classmate:
    def __init__(self):
        self.names = []
        self.num = 0

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        return self

    def __next__(self):
        if self.num < len(self.names):
            ret = self.names[self.num]
            self.num += 1
            return ret
        else:
            raise StopIteration


if __name__ == "__main__":
    c = Classmate()
    for i in range(4):
        c.add("name_"+str(i))

    for name in c:
        print(name)