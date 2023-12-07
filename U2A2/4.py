# Exercise 4: Cree un programa que ejecute 10 hilos, cada uno de los cuales sumará 100 números aleatorios entre el 1 y el 1000. Muestre el resultado de cada hilo. Ganará el hilo que consiga el número mas alto



import threading
import random

class SumThread(threading.Thread):
    def __init__(self, thread_id):
        super().__init__()
        self.thread_id = thread_id
        self.sum_result = 0

    def run(self):
        for _ in range(100):
            random_number = random.randint(1, 1000)
            self.sum_result += random_number

        print(f"Thread {self.thread_id}: Sum = {self.sum_result}")

def main():
    thread_count = 10
    threads = []

    for i in range(1, thread_count + 1):
        thread = SumThread(i)
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    # Find the thread with the highest sum
    max_sum_thread = max(threads, key=lambda x: x.sum_result)
    print(f"\nThread {max_sum_thread.thread_id} has the highest sum: {max_sum_thread.sum_result}")

if __name__ == "__main__":
    main()
