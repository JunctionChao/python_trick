# python中一切皆对象，因此类也是一种对象
# globals() 可以查看全局对象引用，locals()返回当前位置的全部局部变量。
# 使用dir()可以查看对象内的所有属性和方法，
# dir(__builtins__) 或者 __builtins__.__dict__可以查看解释器内置的属性和方法
# __dict__可以看作是数据对象的名称空间，所以只包含自己的属性（并不是所有对象都拥有__dict__属性）, dir()除了显示自己的还显示继承来的属性

"""
用class关键字定义的类本身也是一个对象，负责产生该对象的类称之为元类，元类可以简称为类的类
元类的主要目的是为了控制类的创建行为
type是Python的一个内建元类，用来直接控制生成类，在python当中任何class定义的类其实都是type类实例化的结果
只有继承了type类才能称之为一个元类，否则就是一个普通的自定义类，自定义元类可以控制类的产生过程，类的产生过程其实就是元类的调用过程.

一个类由三大组成部分，分别是
1、类名class_name
2、继承关系class_bases
3、类的名称空间class_dict

方式1：使用class关键字（python解释器会自动转化为第二种）
方式2：通过type关键字，依次传入以上三个参数即可。
"""

# 正常定义类的写法
class Person(object): # 解释器会转化为 Person = type('Person',(object,),{...}) # 这里object可以不写
    country = 'China'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def get_country(cls):
        print(cls.country)

    @staticmethod
    def static():
        print("static method")

    def tell(self):
        print('%s 的年龄是:%s'%(self.name,self.age))


# 通过元类来创建类
country = 'China'
def __init__(self, name, age):
    self.name = name
    self.age = age

@classmethod
def get_country(cls):
    print(cls.country)

@staticmethod
def static():
    print("static method")

def tell(self):
    print('%s 的年龄是:%s'%(self.name,self.age))

# 返回的就是类对象
# type(类名, 父类的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)
Person = type('Person',
            (object,),
            {
                'country':country,
                '__init__':__init__,
                'get_country': get_country,
                'static': static,
                'tell':tell
            })


if __name__ == '__main__':
    help(Person)

    p = Person('John', 25)
    # 实例对象由类创建，类由元类创建
    print(p.__class__, p.__class__.__class__) # <class '__main__.Person'> <class 'type'>