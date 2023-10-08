import time
from functools import wraps


def mean(k: int):
    def inner_mean(func):
        @wraps(func)
        def inner(*args):
            if not isinstance(k, int):
                raise TypeError
            if k == 0:
                raise ZeroDivisionError
            if k < 0:
                raise ValueError

            start_ts = time.time()
            res = func(*args)
            end_ts = time.time()

            curr_time = end_ts - start_ts
            if 'func_lst' not in inner.__dict__:
                inner.func_lst = []
            inner.func_lst.append(curr_time)

            call_time_list = inner.func_lst
            if len(call_time_list) < k:
                mean_time = sum(call_time_list) / \
                            len(call_time_list)
            else:
                mean_time = sum(call_time_list[len(call_time_list) - k:]) / k
            print(mean_time)
            return res
        return inner
    return inner_mean


@mean(10)
def koo(arg1):
    arg1 += 1
    # time.sleep(0.5)


@mean(2)
def boo(arg1):
    arg1 += 1


# for _ in range(10):
    # print(koo(0.5))

# for _ in range(10):
    # print(koo(0.5))
