from functools import wraps

def prefix_decorator(prefix):
    def decorator_function(original_function):
        @wraps(original_function)
        def wrapper_function(*args, **kwargs):
            print(prefix, 'Executed Before', original_function.__name__)
            result = original_function(*args, **kwargs)
            print(prefix, 'Executed After', original_function.__name__, '\n')
            return result
        return wrapper_function
    return decorator_function


@prefix_decorator('LOG:')
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


if __name__ == '__main__':
    print(display_info.__name__)
    display_info('John', 25)
    display_info('Travis', 30)