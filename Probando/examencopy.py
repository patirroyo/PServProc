"""
    Crea dos procesos, y lístalos usando psutil
    El primer proceso estará 10 segundos vivo y 
    matará al otro proceso,
    finalmente creará un fork de si mismo.
    El segundo proceso a los 5 segundos cambiará la prioriodad del primer proceso.
    y lanzará el comando ping a la web de google
"""
import multiprocessing
import psutil
import os
import time


def proceso1(diccionario_pids, PROCESO_PADRE_PID):
    print("Proceso 1 Creado")

    print("PID: ", os.getpid())
    diccionario_pids['pid1'] = os.getpid()

    # Se duerme 10 segundos
    time.sleep(10)

    # mata al proceso 2
    print("Hora de matar al proceso 2")
    if psutil.pid_exists(diccionario_pids['pid2']):
        print("Proceso 2 existe con id: ", diccionario_pids['pid2'])
        psutil.Process(diccionario_pids['pid2']).kill()
        print("Proceso 2 muerto, no existe ya:", diccionario_pids['pid2'])
    else:
        print("Proceso 2 no existe")

    # crea un fork de si mismo
    print("Comprobando si el proceso ya viene de un fork")
    if PROCESO_PADRE_PID == os.getppid():
        print("El proceso no viene de un fork")
        print("Proceso 1 creando un fork de si mismo")
        print("Fork creado")
        os.fork()
    else:
        print("El proceso viene de un fork, no se puede crear otro fork para evitar un bucle infinito")

    # TERMINA EL PROCESO 1
    print("Proceso 1 terminado")


def proceso2(diccionario_pids):
    print("Proceso 2 Creado")

    print("PID: ", os.getpid())
    diccionario_pids['pid2'] = os.getpid()

    time.sleep(5)

    # cambia la prioridad del proceso 1
    print("Proceso 2 cambiando prioridad del proceso 1")
    if psutil.pid_exists(diccionario_pids['pid1']):
        print("Prioridad del proceso 1 antes de cambiar: ",
            psutil.Process(diccionario_pids['pid1']).nice())
        psutil.Process(diccionario_pids['pid1']).nice(10)
        print("Prioridad del proceso 1 después de cambiar: ",
            psutil.Process(diccionario_pids['pid1']).nice())
    else:
        print("Proceso 1 no existe")

    # lanza el comando ping a google.com por 4 veces y termina
    print("Lanzando comando ping a google.com")
    os.system("ping -c 4 google.com")

    # TERMINA EL PROCESO 2
    print("Proceso 2 terminado")


# def crear_lista():
#     print("Lista de procesos:")
#     print(psutil.pids())


if __name__ == "__main__":
    # Saco el PID del proceso padre (el primero que se crea al ejecutar el archivo) para poder preguntar más tarde por esto
    PROCESO_PADRE_PID = os.getpid()

    #  crea un diccionario para compartir los pids entre procesos
    manager = multiprocessing.Manager()
    diccionario_pids = manager.dict({'pid1': 0, 'pid2': 0})

    # Crea procesos y llama a sus respectivas funciones
    p1 = multiprocessing.Process(target=proceso1, args=(
        diccionario_pids, PROCESO_PADRE_PID))
    p2 = multiprocessing.Process(target=proceso2, args=(diccionario_pids,))

    #  inicia los procesos
    p1.start()
    p2.start()

    # espera a que los procesos terminen
    p1.join()
    p2.join()

    # finaliza el proceso principal
    print("Finalizado")
