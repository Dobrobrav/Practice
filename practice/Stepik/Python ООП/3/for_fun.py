import time


lst = [i for i in range(100_000_000)]

start_time = time.time_ns()
a = list(lst)
print(time.time_ns() - start_time)

tpl = tuple(lst)

start_time = time.time_ns()
b = list(tpl)
print(time.time_ns() - start_time)

