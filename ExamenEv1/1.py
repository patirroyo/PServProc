""" EJERCICIO1(4,5 puntos)
Implementa en python un código de Productor Consumidor mediante cola sincronizada tal que:
-El productor produce números enteros mayor que 100 y menor que 500(Aleatorios), el tiempo de espera entre la generación de un número y otro es de PT segundos (1 punto)
-El consumidor lee X números de la cola de golpe, calcula la multiplicación de esos X números .(1 punto).el tiempo de espera entre la lectura de X elementos cola y la siguiente lectura de los siguientes X elementos es de  CT segundos (1 punto)
Prueba el algoritmo con los distintos casos usando una relación de productor:consumidor de     
1:1   con PT=1  CT=4 y X=3 (0,5 puntos)
4:2 con PT=2  CT=2 y X=2 (0,5 puntos)
2:6 con PT=1  CT=10 y X=4 (0,5 puntos) """


from math import gcd
import time
import threading
import random
import queue

class Producer(threading.Thread):

    def __init__(self, cola, pt):
        threading.Thread.__init__(self)
        self.cola = cola
        self.pt=pt
    def run(self):
        while True:
            aleatorio = random.randint(101, 500)  
            self.cola.put(aleatorio)
            print("Productor: Añadido el " + str(aleatorio))
            print("Productor: " + str(self.cola.qsize()) + " elementos en la cola")
            print("Productor: " + str(self.cola.queue))
            time.sleep(self.pt) # PT producer time

class Consumer(threading.Thread):
    def __init__(self, cola, ct, x):
        threading.Thread.__init__(self)
        self.cola = cola
        self.ct=ct
        self.x=x
    
    def run(self):
        while True:
            list = []
            if self.cola.qsize() >= self.x:
                for i in range(self.x):  
                    list.append(self.cola.get())
                print("Consumidor: ha cogido " + str(self.x) + " elementos de la cola")

                self.multiply(list)
            else:
                print("Consumidor: no hay suficientes elementos en la cola")
                print("Consumidor: " + str(self.cola.qsize()) + " elementos en la cola")

            time.sleep(self.ct)  # CT consumer time
    
    def multiply(self, list):
        result = 1
        string = "Multiplicación: "
        for i in range(len(list)):
            if i == len(list) - 1:
                string = string + str(list[i])
            else:
                string = string + str(list[i]) + " * "
            result = result * list[i]
        string = string + " = " + str(result)
        print(string)

def mainEj2(nP,nC, pt, ct, x):
    cola = queue.Queue()
    listProducer = []
    for i in range(nP):
        t1 = Producer(cola, pt)
        listProducer.append(t1)
    
    listConsumer = []
    for i in range(nC):
        t2 = Consumer(cola, ct, x)
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
    #mainEj2(1,1,1,4,3)
    #mainEj2(4,2,2,2,2)
    mainEj2(2,10,1,10,4)