import time

from datetime import datetime

from random import randint
from multiprocessing import Process, Manager



def generate_info(info):
    while True:
        time. sleep(1)
        info.append(f"something at {datetime.now()}")
        print("New info added")
def process_info(info, results):
    while True:
        time.sleep(1)
        print("Checking for new info")
        if info:
            new_info = info.pop()
            results.append(new_info + " processed")
            print("New info processed")
def main():
    shared_memory = Manager()

    info = shared_memory.list([])
    results = shared_memory.list([])
    
    generator = Process(target=generate_info, args=[info])
    processor1 = Process(target=process_info, args=[info, results])
    processor2 = Process(target=process_info, args=[info, results])

    generator.start()
    processor1.start()
    processor2.start()
    generator.join()

if __name__ == "__main__":
    main()
