# Exercise 2: Using the multithreading module, write a python program as follows:
# ● Create a pool of threads to run concurrent tasks.
# ● The pool size should be 3.
# ● Create and fill an array of 100 random integer numbers.
# ● Run all 3 threads to parse the vector data. One of them must show the mean, another
# the maximum and minimum value, and the last one the standard deviation. Note that
# although these processes share the vector, they only do so for reading. None of them
# must modify any value of the vector.


import threading
import random
import statistics

class StatsThread(threading.Thread):
    def __init__(self, data, result_holder):
        super().__init__()
        self.data = data
        self.result_holder = result_holder

    def run(self):
        if self.result_holder == "mean":
            result = statistics.mean(self.data)
        elif self.result_holder == "max_min":
            result = (max(self.data), min(self.data))
        elif self.result_holder == "std_dev":
            result = statistics.stdev(self.data)

        print(f"Thread {threading.current_thread().name}: {self.result_holder} = {result}")

def main():
    pool_size = 3
    data = [random.randint(1, 100) for _ in range(100)]

    mean_thread = StatsThread(data, "mean")
    max_min_thread = StatsThread(data, "max_min")
    std_dev_thread = StatsThread(data, "std_dev")

    threads = [mean_thread, max_min_thread, std_dev_thread]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
