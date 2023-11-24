from functools import wraps
from memory_profiler import profile
from io import StringIO


def props(cls):
    return [i for i in cls.__dict__.keys() if i[:1] != '_']


def profile_deco(input_func):
    @wraps(input_func)
    def wrapper(*args, **kwargs):
        if 'stats' not in props(wrapper):
            wrapper.stat = StringIO()
        if 'call_num' not in props(wrapper):
            wrapper.call_num = 0
        wrapper.call_num += 1
        wrapper.stat.write(f'\n{wrapper.call_num} call of func\n')
        decorated = profile(input_func, stream=wrapper.stat)

        def print_stat():
            print(wrapper.stat.getvalue())

        wrapper.print_stat = print_stat
        return decorated(*args, **kwargs)
    return wrapper


@profile_deco
def add(a, b):
    return a + b


@profile_deco
def sub(a, b):
    return a - b


if __name__ == '__main__':
    add(1, 2)
    add(4, 5)
    sub(4, 5)
    add.print_stat()
    sub.print_stat()
