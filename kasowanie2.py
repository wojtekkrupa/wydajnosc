from pathos.multiprocessing import ProcessingPool
import os
from timeit import timeit

def delete_files(file_path):
    try:
        os.remove(file_path)
    except Exception:
        pass

def delete_files_parallel(folder_path):
    with ProcessingPool() as pool:
        pool.map(delete_files, [os.path.join(folder_path, file) for file in os.listdir(folder_path)])

if __name__ == "__main__":
    folder_path = "c:\\testy\\test"  # Zmień na właściwą ścieżkę

    time = timeit("delete_files_parallel(folder_path)", globals=globals(), number=1)
    print(time)
