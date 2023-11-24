import time
import weakref
from memory_profiler import profile


class SomeClass:
    def __init__(self, value):
        self.value = value


class Slots:
    __slots__ = ('value1', 'value2')

    def __init__(self):
        self.value1 = SomeClass('val1')
        self.value2 = SomeClass('val2')


class SimpleAttrs:
    def __init__(self):
        self.value1 = SomeClass('value1')
        self.value2 = SomeClass('value2')


class WeakRefAttrs:
    def __init__(self):
        self.value1 = weakref.ref(SomeClass('value1'))
        self.value2 = weakref.ref(SomeClass('value2'))


def attr_speed_test(cls_list):
    start = time.time()
    for cls in cls_list:
        r = cls.value1
        r = cls.value2
        cls.value1 = SomeClass('value3')
        cls.value2 = SomeClass('value3')
        del cls.value1
        del cls.value2
    end = time.time()
    return end - start


@profile
def run_tests(repeat_cnt: int, is_print=True):
    start = time.time()
    list_slots = [Slots() for _ in range(repeat_cnt)]
    end = time.time()
    slots_time = end-start

    start = time.time()
    list_simple = [SimpleAttrs() for _ in range(repeat_cnt)]
    end = time.time()
    simple_time = end - start

    start = time.time()
    list_weakref = [WeakRefAttrs() for _ in range(repeat_cnt)]
    end = time.time()
    weakref_time = end - start

    time_attrs_slots = attr_speed_test(list_slots)
    time_attrs_simple = attr_speed_test(list_simple)
    time_attrs_weakref = attr_speed_test(list_weakref)
    if is_print:
        print(f'slots init time: {slots_time}\nslots attrs access time: {time_attrs_slots}\n')
        print(f'weakref init time: {weakref_time}\nweakref attrs access time: {time_attrs_weakref}\n')
        print(f'simple init time: {simple_time}\nsimple attrs access time: {time_attrs_simple}\n')


if __name__ == '__main__':
    REPEAT_CNT_PROFILER = 100_000
    run_tests(REPEAT_CNT_PROFILER)
    print(run_tests.__dict__)
