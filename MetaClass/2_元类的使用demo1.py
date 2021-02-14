# 将创建的类属性字符串改为大写

def upper_attr(class_name, class_parents, class_attr):
    # 将不是__开头的属性名改为大写
    new_attr = {}
    for name, value in class_attr.items():
        if not name.startswith("__"):
            new_attr[name.upper()] = value

    # 调用type来创建一个类
    return type(class_name, class_parents, new_attr)


class Foo(object, metaclass=upper_attr): # 解释器会转化为 Foo = upper_attr('Foo',(object,),{'bar': 'pip'})
    bar = 'pip'


print(hasattr(Foo, 'bar')) # False
print(hasattr(Foo, 'BAR')) # True

f = Foo()
print(f.BAR) # pip