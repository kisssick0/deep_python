#########################
profiling with speed test
#########################
"/Users/alinakozlova/Desktop/у4еба/8 семестр/deep_python_23b_kisssick/bin/python" /Users/alinakozlova/Desktop/course/deep_python_23b_kisssick/08/profiling.py
slots init time: 3.5412139892578125
slots attrs access time: 0.7687358856201172

weakref init time: 3.899286985397339
weakref attrs access time: 0.761436939239502

simple init time: 3.8229176998138428
simple attrs access time: 0.7290258407592773

Filename: /Users/alinakozlova/Desktop/course/deep_python_23b_kisssick/08/profiling.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    44     15.5 MiB     15.5 MiB           1   @profile
    45                                         def run_tests(repeat_cnt: int, is_print=True):
    46     15.5 MiB      0.0 MiB           1       start = time.time()
    47     51.4 MiB     35.9 MiB      100003       list_slots = [Slots() for _ in range(repeat_cnt)]
    48     51.4 MiB      0.0 MiB           1       end = time.time()
    49     51.4 MiB      0.0 MiB           1       slots_time = end-start
    50                                         
    51     51.4 MiB      0.0 MiB           1       start = time.time()
    52     98.1 MiB     46.8 MiB      100003       list_simple = [SimpleAttrs() for _ in range(repeat_cnt)]
    53     98.1 MiB      0.0 MiB           1       end = time.time()
    54     98.1 MiB      0.0 MiB           1       simple_time = end - start
    55                                         
    56     98.1 MiB      0.0 MiB           1       start = time.time()
    57    129.5 MiB     31.4 MiB      100003       list_weakref = [WeakRefAttrs() for _ in range(repeat_cnt)]
    58    129.5 MiB      0.0 MiB           1       end = time.time()
    59    129.5 MiB      0.0 MiB           1       weakref_time = end - start
    60                                         
    61    129.5 MiB      0.0 MiB           1       time_attrs_slots = attr_speed_test(list_slots)
    62    134.4 MiB      4.9 MiB           1       time_attrs_simple = attr_speed_test(list_simple)
    63    136.1 MiB      1.7 MiB           1       time_attrs_weakref = attr_speed_test(list_weakref)
    64    136.1 MiB      0.0 MiB           1       if is_print:
    65    136.1 MiB      0.0 MiB           1           print(f'slots init time: {slots_time}\nslots attrs access time: {time_attrs_slots}\n')
    66    136.1 MiB      0.0 MiB           1           print(f'weakref init time: {weakref_time}\nweakref attrs access time: {time_attrs_weakref}\n')
    67    136.1 MiB      0.0 MiB           1           print(f'simple init time: {simple_time}\nsimple attrs access time: {time_attrs_simple}\n')


{'__wrapped__': <function run_tests at 0x1072a01f0>}


##########################################
profiling decorator for calls of functions
#########################################
         4 function calls in 0.000 seconds

   Random listing order was used

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        2    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        2    0.000    0.000    0.000    0.000 /Users/alinakozlova/Desktop/course/deep_python_23b_kisssick/08/profiling_deco.py:27(add)




2 function calls in 0.000 seconds

   Random listing order was used

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 /Users/alinakozlova/Desktop/course/deep_python_23b_kisssick/08/profiling_deco.py:32(sub)
