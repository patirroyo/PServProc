import multiprocessing as mp
import random
import string

def rand_string(length, output):
    """Generates a random string of numbers, lower- and uppercase chars."""
    random.seed(123)
    rand_str = ''.join(random.choice(
        string.ascii_lowercase
        + string.ascii_uppercase
        + string.digits)
        for i in range(length))
    output.put(rand_str)

if __name__ == "__main__":
    # Define an output list
    output = mp.Queue()

    # Setup a list of processes that we want to run
    processes = [mp.Process(target=rand_string, args=(10, output)) for x in range(4)]

    # Run processes
    for p in processes:
        p.start()

    # Exit the completed processes
    for p in processes:
        p.join()

    # Get process results from the output list
    results = [output.get() for p in processes]

    print(results)
