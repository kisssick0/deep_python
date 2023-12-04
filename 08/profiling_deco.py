import io
import pstats
from functools import wraps
import cProfile


def props(cls):
    return [i for i in cls.__dict__.keys() if i[:1] != '_']


def profile_deco(input_func):
    profiler = cProfile.Profile()

    @wraps(input_func)
    def wrapper(*args, **kwargs):
        profiler.enable()
        result = input_func(*args, **kwargs)
        profiler.disable()
        return result

    def print_stat():
        out = io.StringIO()
        stat = pstats.Stats(profiler, stream=out)
        stat.print_stats()
        print(out.getvalue())

    wrapper.print_stat = print_stat
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
