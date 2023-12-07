# Exercise 1: Using the multithreading module, write a simple python program as follows:
# ● Create a pool of threads to run concurrent tasks.
# ● The pool size should be 10.
# ● The thread should receive as input a number [id] (unique identifier for each of the
# threads, starting from 1) and a number [number_of_writtings] (number of times the
# thread will write the message).
# ● Each thread should sleep a random amount of time (between 100 and 300
# milliseconds) and write the message ("I am 1", "I am 2", etc) a random number of times
# between 5 and 15.

import threading
import time
import random

class CustomThread(threading.Thread):
    def __init__(self, thread_id, number_of_writings):
        super().__init__()
        self.thread_id = thread_id
        self.number_of_writings = number_of_writings

    def run(self):
        for _ in range(self.number_of_writings):
            time.sleep(random.uniform(0.1, 0.3))  # Sleep for a random time between 100 and 300 milliseconds
            print(f"I am {self.thread_id}")

def main():
    pool_size = 10
    threads = []

    for i in range(1, pool_size + 1):
        number_of_writings = random.randint(5, 15)
        thread = CustomThread(i, number_of_writings)
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
