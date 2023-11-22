from numba import jit
from timeit import timeit

# def fib_iter2(n):
#     """
#         Funkcja drukuje kolejne wyrazy ciągu Fibonacciego
#         aż do wyrazu n-tego, który zwraca.
#         Wersja iteracyjna z pętlą for.
#     """
#     a, b = 0, 1
#     print("wyraz", 1, a)
#     print("wyraz", 2, b)
#     for i in range(1, n - 1):
#         # wynik = a + b
#         a, b = b, a + b
#         print("wyraz", i + 2, b)
#
#     # print()  # wiersz odstępu
#     return b
@jit(nopython=True)
def fib_rek(n):
    """
        Funkcja zwraca n-ty wyraz ciągu Fibonacciego.
        Wersja rekurencyjna.
    """
    if n < 1:
        return 0
    if n < 2:
        return 1
    return fib_rek(n - 1) + fib_rek(n - 2)

time = timeit("fib_rek(40)", globals=globals(), number=1)
print(time) # 27,7s -> 1 s

