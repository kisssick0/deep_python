import time


func_dict = {}


def mean(k: int):
    def inner_mean(func):
        def inner(*args):
            if not isinstance(k, int):
                raise TypeError
            if k == 0:
                raise ZeroDivisionError
            if k < 0:
                raise ValueError

            start_ts = time.time()
            func(*args)
            end_ts = time.time()

            if str(func.__name__) not in func_dict:
                func_dict[str(func.__name__)] = []

            curr_time = end_ts - start_ts
            func_dict[str(func.__name__)].append(curr_time)
            # print(func_dict)

            if len(func_dict[str(func.__name__)]) < k:
                mean_time = 0
            else:
                mean_time = sum(func_dict.get(str(func.__name__))[len(func_dict.get(str(func.__name__))) - k:]) / k
                # print(mean_time)
            return mean_time
        return inner
    return inner_mean


@mean(10)
def koo(arg1):
    arg1 += 1
    # time.sleep(0.5)


@mean(2)
def boo(arg1):
    arg1 += 1


# for _ in range(1):
    # print(foo(0.5))
