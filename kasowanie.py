import os
# from numba import jit
from timeit import timeit
# @jit(nopython=True)
def delete_files_in_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            os.remove(file_path)

if __name__ == "__main__":
    folder_path = "c:\\test"  # Zmień na właściwą ścieżkę

    time = timeit("delete_files_in_folder(folder_path)", globals=globals(), number=1)
    print(time)

