from numba import jit
from timeit import timeit


# @jit(nopython=True)
def fib_iter1(n):  # definicja funkcji
    """
        Funkcja drukuje kolejne wyrazy ciągu Fibonacciego
        aż do wyrazu n-tego, który zwraca.
        Wersja iteracyjna z pętlą while.
    """
    pwyrazy = (0, 1)  # dwa pierwsze wyrazy ciągu zapisane w tupli
    a, b = pwyrazy  # przypisanie wielokrotne, rozpakowanie tupli
    # print(a, end=" ")
    while n > 1:
        # print(b, end=" ")
        a, b = b, a + b  # przypisanie wielokrotne
        n -= 1

# if __name__ == '__main__':
#     import sys
#     sys.exit(main(sys.argv))
time = timeit("fib_iter1(40)", globals=globals(), number=1)
print(time)