# Exercise 3: Cree un hilo que genere números aleatorios entre 1 y 100 y los vaya insertando en una lista, y otro que recorra circularmente esa lista y sustituya los números terminados en cero por el valor -1. Un tercer hilo abortará los otros dos en el momento en el que la suma de los elementos de la lista supere el valor de 20000

import threading
import random
import time

class RandomNumberThread(threading.Thread):
    def __init__(self, data_list):
        super().__init__()
        self.data_list = data_list
        self.stop_event = threading.Event()

    def run(self):
        while not self.stop_event.is_set():
            random_number = random.randint(1, 100)
            self.data_list.append(random_number)
            print(f"Added {random_number} to the list")
            #time.sleep(0.1)  # Simulating some work

class CircularReplaceThread(threading.Thread):
    def __init__(self, data_list):
        super().__init__()
        self.data_list = data_list
        self.stop_event = threading.Event()

    def run(self):
        while not self.stop_event.is_set():
            for i in range(len(self.data_list)):
                if self.data_list[i] % 10 == 0:
                    self.data_list[i] = -1
                    print(f"Replaced {self.data_list[i]} with -1")
            #time.sleep(0.1)  # Simulating some work

class StopThread(threading.Thread):
    def __init__(self, data_list, threshold):
        super().__init__()
        self.data_list = data_list
        self.threshold = threshold

    def run(self):
        while sum(self.data_list) <= self.threshold:
            print(f"Sum of list: {sum(self.data_list)}")
            #time.sleep(0.1)  # Check the sum every second

        # Trigger stop events in other threads
        random_number_thread.stop_event.set()
        circular_replace_thread.stop_event.set()

if __name__ == "__main__":
    data_list = []
    threshold_value = 20000

    random_number_thread = RandomNumberThread(data_list)
    circular_replace_thread = CircularReplaceThread(data_list)
    stop_thread = StopThread(data_list, threshold_value)

    random_number_thread.start()
    circular_replace_thread.start()
    stop_thread.start()

    random_number_thread.join()
    circular_replace_thread.join()
    stop_thread.join()

    print(f"Final List: {data_list}")
