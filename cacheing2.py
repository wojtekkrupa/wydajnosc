# from functools import lru_cache
from timeit import timeit
import random
from numba import jit

# @lru_cache #< 2s
@jit(nopython=True) # 0,2s
def get_order_details(order_id):
    for _ in range(1000_000):
        pass
    return 100 * order_id

# @profile
def main():
    orders_to_search = [random.randint(0, 100) for _ in range(1000)]
    for order in orders_to_search:
        get_order_details(order)

time = timeit("main()", globals=globals(), number=1)
print(time)
