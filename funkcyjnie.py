# # funkcyjnie
# def main(): # Definicja funkcji o nazwie main()
#     Lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     print("Lista = ", Lista, ".", sep = "")
#     print("Suma liczb = ", sum(Lista), ".", sep = "")
#
#
# main() # Wywołanie funkcji main().

# Zadanie 1.4. dużo wolniej niz imperatywnie
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)

def main(): # Definicja funkcji o nazwie main().
    for n in range(4):
        print(fibonacci(n), ", ", sep = "", end = "")
main() # Wywołanie funkcji main().