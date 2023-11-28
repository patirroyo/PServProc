"""Crea dos hilos, y lístalos usando psutil
un proceso abre el editor de texto

El primer hilo estará 10 segundos vivo y matará al otro proceso, finalmente creará un fork de si mismo
El segundo proceso a los 5 segundos cambiará la prioridad del primer proceso y lanzará un ping a la web de google"""

import os
import psutil
import time
import subprocess
import multiprocessing
import sys


def proceso1(PROCESO_PADRE_PID):
    print(f"Proceso1 con PID: {os.getpid()} creado.")
    time.sleep(10)  # El primer proceso vive 10 segundos

    # Enviar señal para terminar el proceso2
    for proceso in psutil.process_iter(['pid', 'name']):
        if proceso.name() == "Python" and int(proceso.info['pid']) != os.getpid():
            proceso.kill()

    # Evitar bucle infinito al realizar el fork a sí mismo
    if os.getppid() == PROCESO_PADRE_PID:
        # Realizar un fork de sí mismo
        print(PROCESO_PADRE_PID, os.getpid())
        if esWindows():
            proceso_principal = multiprocessing.Process(
                name="procesoFork", target=proceso1, args=(PROCESO_PADRE_PID,))
            proceso_principal.start()
            print("esperando 10 segundos para volver a hacer el fork si procede")
        else:
            os.fork()  # adaptar esta parte si se usa windows
            print("esperando 10 segundos para volver a hacer el fork si procede")

    else:
        print("ya no se hace nada mas puedes darle al enter para salir")


def proceso2():
    print(f"Proceso2 con PID: {os.getpid()} creado.")
    time.sleep(5)  # El segundo proceso vive 5 segundos
    # Ejecutar el comando ping en el proceso2
    cambiar_prioridad()
    subprocess.run(["ping", "google.com"])


def esWindows():
    try:
        sys.getwindowsversion()
    except AttributeError:
        return (False)
    else:
        return (True)


def cambiar_prioridad():
    for proceso in psutil.process_iter(['pid', 'name']):
        if proceso.info['name'] == "Python" and int(proceso.info['pid']) != os.getpid():
            if esWindows():
                subprocess.check_output(
                    "wmic process where processid=\""+str(os.getpid())+"\" CALL   setpriority \"below normal\"")
            else:
                process1 = psutil.Process(proceso.info['pid'])
                process1.nice(10)


if __name__ == "__main__":
    PROCESO_PADRE_PID = os.getpid()

    proceso_principal = multiprocessing.Process(
        name="proceso1", target=proceso1, args=(PROCESO_PADRE_PID,))
    proceso_secundario = multiprocessing.Process(
        name="proceso2", target=proceso2, args=())

    proceso_principal.start()
    proceso_secundario.start()

    proceso_principal.join()
    proceso_secundario.join()

    print("Proceso principal finalizado")
