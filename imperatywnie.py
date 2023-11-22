# imperatywnie
# def main():  # Definicja funkcji o nazwie main()
#     Lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     print("Lista = ", Lista, ".", sep="")
#     suma = 0
#     for i in Lista:
#         suma = suma + i
#     print("Suma liczb = ", suma, ".", sep="")
#
#
# main()  # Wywołanie funkcji main()

# Zadanie 1.3. duzo szybciej niż funkcyjnie
def fibonacci(n, pierwszy = 0, drugi = 1):
    for _ in range(n):
        print(pierwszy, ", ", end = "", sep = "")
        pierwszy, drugi = drugi, pierwszy + drugi

def main(): # Definicja funkcji o nazwie main().
    fibonacci(4)
main() # Wywołanie funkcji main()