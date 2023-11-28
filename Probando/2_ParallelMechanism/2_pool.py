from multiprocessing import Pool, TimeoutError
import time
import os

def f(x):
    return x*x

if __name__ == '__main__':
    pool = Pool(processes=os.cpu_count())              # start 4 worker processes
    print(os.cpu_count())
    print (pool.map(f, [20]))
    # print "[0, 1, 4,..., 81]"
    print (pool.map(f, range(10)))
    print("-------------Unordered-------------------")
    # print same numbers in arbitrary order
    for i in pool.imap_unordered(f, range(10)):
        print(i)
    print("------------Async timeout 1--------------------")
    # evaluate "f(20)" asynchronously
    res = pool.apply_async(f, (20,))      # runs in *only* one process
    print (res.get(timeout=1))              # prints "400"
    print("-----------Async pid timeout 1---------------------")
    # evaluate "os.getpid()" asynchronously
    res = pool.apply_async(os.getpid, ()) # runs in *only* one process
    print (res.get(timeout=1))              # prints the PID of that process
    print("--------------------------------")
    # launching multiple evaluations asynchronously *may* use more processes
    multiple_results = [pool.apply_async(os.getpid, ()) for i in range(4)]
    print([res.get(timeout=1) for res in multiple_results])
    print("--------------------------------")
    # make a single worker sleep for 10 secs
    res = pool.apply_async(time.sleep, (1,))
    try:
        print(res.get(timeout=10))
    except TimeoutError:
        print ("We lacked patience and got a multiprocessing.TimeoutError")