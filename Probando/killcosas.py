"""
Crea un programa python que contenga dos procesos:
Proceso1: abre el editor de textos de linux
Proceso2: espera 10 segundos y mata el proceso1
"""
import time
import os
import multiprocessing
import psutil


def proceso1(diccionario_pids):
    print("Proceso 1")
    print("PID: ", os.getpid())
    diccionario_pids['pid1'] = os.getpid()

    # Abre el editor de textos, lo que hace os.system es abrir un terminal y ejecutar el comando que le pasemos
    os.system("nano")

    # Espera 5 segundos
    time.sleep(5)
    
    # Cambia la prioridad del proceso 2 a 10
    if psutil.pid_exists(diccionario_pids['pid2']):
        print("Prioridad del proceso 2 antes de cambiar: ",psutil.Process(diccionario_pids['pid2']).nice())
        psutil.Process(diccionario_pids['pid2']).nice(10)
        print("Prioridad del proceso 2 cambiada a 10: ",psutil.Process(diccionario_pids['pid2']).nice())
    else:
        print("Proceso 2 no existe")

    # Se termina el proceso 1
    print("Proceso 1 terminado")


def proceso2(diccionario_pids):
    print("Proceso 2")

    print("PID: ", os.getpid())
    diccionario_pids['pid2'] = os.getpid()

    # Espera 10 segundos
    time.sleep(1)

    # Mata a cualquier proceso de nano que haya abierto, porque no nos deja matar a ese proceso en concreto.
    # os.system("killall nano")
    # print("Proceso 1 matado")
    
    # Como esto no me funciona mato desde el terminal todos los procesos de nano
    if psutil.pid_exists(diccionario_pids['pid1']):
        print("Proceso 1 existe con id: ", diccionario_pids['pid1'])
        #psutil.Process(diccionario_pids['pid1']).kill() 
        os.kill(diccionario_pids['pid1'], 9) # el 9 es el signal.SIGKILL que es el que mata el proceso sin preguntar nada
    else:
        print("Proceso 1 no existe")
    
    # Se termina el proceso 2
    print("Proceso 2 terminado")


if __name__ == '__main__':

    # Creamos un diccionario para compartir los pids entre procesos
    manager = multiprocessing.Manager()
    diccionario_pids = manager.dict({'pid1': 0, 'pid2': 0})

    # Instanciamos los procesos
    p1 = multiprocessing.Process(target=proceso1, args=(diccionario_pids,))
    p2 = multiprocessing.Process(target=proceso2, args=(diccionario_pids,))
    
    # Iniciamos los procesos
    p1.start()
    p2.start()
    # Esperamos a que terminen los procesos
    p1.join()
    p2.join()
    print("Fin del programa")