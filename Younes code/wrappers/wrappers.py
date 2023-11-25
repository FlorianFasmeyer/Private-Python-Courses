from functools import wraps
import time
import sys


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper


@timeit
def delay_print(txt):
    prnt = iter(list(txt))
    for char in txt:
        print(next(prnt), end='', flush=True)
        time.sleep(0.05)


@timeit
def delay_print2(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


if __name__ == '__main__':
    delay_print('Hello world !\n')
    delay_print2('Hello world !\n')