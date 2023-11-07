from math import gcd
import time
import threading
import random
import queue

class Producer(threading.Thread):
    """
    Produces random integers to a list
    """

    def __init__(self, cola, pt):
        """
        Constructor.

        @param integers list of integers
        @param queue queue synchronization object
        """
        threading.Thread.__init__(self)
        self.cola = cola
        self.pt=pt
    
    def run(self):
        """
        Thread run method. Append random integers to the integers
        list at random time.
        """
        while True:
            # examen
            for i in range(10):  
                self.cola.put(random.randint(10, 1000))   
            time.sleep(self.pt) # PT producer time

class Consumer(threading.Thread):
    """
    Consumes random integers from a list
    """

    def __init__(self, cola, ct, x):
        """
        Constructor.

        @param integers list of integers
        @param queue queue synchronization object
        """
        threading.Thread.__init__(self)
        self.cola = cola
        self.ct=ct
        self.x=x
    
    def run(self):
        """
        Thread run method. Consumes integers from list
        """
        while True:
            list = []
            for i in range(self.x):  
                list.append(self.cola.get())
            
            self.calculateMCD(list)

            time.sleep(self.ct)  # CT consumer time
        
    def calculateMCD(self, list):
        print("MCD: " + str(list[0]) + " " + str(list[1]) + " " + str(list[2]) + " = " + str(gcd(list[0], gcd(list[1], list[2]))))
        print(list)

def main():
    integers = []
    cola = queue.Queue()
    t1 = Producer(cola)
    t2 = Consumer(cola)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

def mainEj2(nP,nC):
    integers = []
    cola = queue.Queue()
    listProducer = []
    for i in range(nP):
        t1 = Producer(cola, 2)
        listProducer.append(t1)
    listConsumer = []
    for i in range(nC):
        t2 = Consumer(cola, 4, 2)
        listConsumer.append(t2)
    
    for prducer in listProducer:
        prducer.start()
    for consumer in listConsumer:
        consumer.start()
    for prducer in listProducer:
        prducer.join()
    for consumer in listConsumer:
        consumer.join()


if __name__ == '__main__':
    #mainEj2(1,1)
    mainEj2(4,2)
    #mainEj2(2,10)
 
