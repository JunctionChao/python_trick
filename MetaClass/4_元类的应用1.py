# 使用元类思想来实现ORM

class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs):
        mappings = dict()

        for k, v in attrs.items():
            if isinstance(v, tuple):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
            
        for k in mappings.keys():
            attrs.pop(k)

        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)


class User(metaclass=ModelMetaClass):
    uid = ('uid', "int unsigned")
    name = ('username', "varchar(30)")
    email = ('email', "varchar(30)")
    password = ('password', "varchar(30")
    # 当指定元类后，以上的类属性将不在类中，而是在__mappings__属性指定的字典中存储
    # 以上的User类中有
    # __mappings__ = {
    #     "uid": ('uid', "int unsigned")
    #     "name": ('username', "varchar(30)")
    #     "email": ('email', "varchar(30)")
    #     "password": ('password', "varchar(30")
    # }
    # __table__ = "User"
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)
        
    def save(self):
        fields = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v[0])
            args.append(getattr(self, k, None))
        
        # sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join((str(i) for i in args)))
        
        args_temp = list()
        for temp in args:
            if isinstance(temp, int):
                args_temp.append(str(temp))
            elif isinstance(temp, str):
                args_temp.append("'%s'" % temp)
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(args_temp))
        print("SQL: %s" % sql)


if __name__ == '__main__':
    u = User(uid=123, name="John", email="John@gmail.com", password="pwd")
    u.save()
