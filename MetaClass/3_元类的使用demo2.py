# 使用class来当做元类

# 继承type的类也是元类
class UpperAttrMetaClass(type):
    def __new__(cls, class_name, class_parents, class_attr):
        new_attrs = dict((name.upper(), value) if not name.startswith('__') else (name, value)  for name, value in class_attr.items())

        # 方法1：通过type来做类对象的创建
        # return type(class_name, class_parents, new_attrs) # 返回一个对象，但同时这个对象是一个类

        # 方法2：复用type.__new__方法
        return type.__new__(cls, class_name, class_parents, new_attrs) # 下面两种写法一样
        # # return super().__new__(cls, class_name, class_parents, new_attrs)
        # return super(UpperAttrMetaClass, cls).__new__(cls, class_name, class_parents, new_attrs)


class Foo(object, metaclass=UpperAttrMetaClass): # Foo = UpperAttrMetaClass('Foo',(object,),{'bar': 'pip'})
    bar = 'pip'


if __name__ == '__main__':
    print(hasattr(Foo, 'bar')) # False
    print(hasattr(Foo, 'BAR')) # True

    f = Foo()
    print(f.BAR) # pip
