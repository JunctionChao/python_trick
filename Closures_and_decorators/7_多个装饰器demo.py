def set_func1(func):
    def call_func():
        return "<h1>" + func() + "</h1>"   # 这里的func() 在执行过程中会去调用set_func2中的call_func()
    return call_func

def set_func2(func):
    def call_func():
        return "<td>" + func() + "</td>"
    return call_func


@set_func1
@set_func2
def get_str():
    return "Hello"

if __name__ == '__main__':
    print(get_str()) # <h1><td>Hello</td></h1>