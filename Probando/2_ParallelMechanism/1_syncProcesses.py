from multiprocessing import Pool, Manager
import time

def f(args):
    lock, i = args
    with lock:
        print('hello world', i)
        time.sleep(1)  # Simula una tarea que toma tiempo

def main():
    with Manager() as manager:
        lock = manager.Lock()  # Crear un objeto Lock compartido
        with Pool() as pool:
            pool.map(f, [(lock, num) for num in range(10)])

if __name__ == '__main__':
    main()