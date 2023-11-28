"""Crea dos hilos, y lístalos usando psutil
un proceso abre el editor de texto

El primer hilo estará 10 segundos vivo y matará al otro proceso, finalmente creará un fork de si mismo
El segundo proceso a los 5 segundos cambiará la prioridad del primer proceso y lanzará un ping a la web de google"""

import os
import subprocess
import time
import psutil
import multiprocessing as mp




def create_process_1(colaPID, sleep_time, pp_pid):
    
    time.sleep(2) #esperamos a que se cree el proceso2
    p2_pid = colaPID.get()
    colaPID.put(os.getpid())
    p1_pid = os.getpid()
    p1_ppid = os.getppid()
    print(f"Creando Proceso1 (PID: {p1_pid}, PPID: {p1_ppid})")
    

    time.sleep(sleep_time)

    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['pid'] == p2_pid:
            print(f"Proceso1 matando al Proceso2 con pid: {p2_pid}")
            os.kill(p2_pid, 9)
            break
    
    
    if pp_pid == p1_ppid:
        print("Proceso1 creando un fork de sí mismo")
        
        
        p1fork = os.fork()
        
        print(f"Proceso1 fork pid: {p1fork}")
        #processid > 0 representa el proceso padre
        if p1fork > 0:
            print ("\nParent process:")
            print("Process ID:", os.getpid())
            print("Cild's process ID:", p1fork)
            print("Proceso padre esperando a que el hijo termine...")
            os.waitpid(p1fork, 0)
            print("\n")
        else:
            print ("\nChild process:")
            print("Process ID:", os.getpid())
            print("Parent's process ID:", os.getppid())
            print("Al final ha un fork de sí mismo")
            print("\n")
    else:
        print("Proceso1 no puede crear un fork de sí mismo porque no es el proceso padre")
        
        
    print(f"Proceso1 terminado")

def create_process_2(colaPID, sleep_time):
    
    p2_pid = os.getpid()
    p2_ppid = os.getppid()
    
    print(f"proceso2 pid: {p2_pid} ppid: {p2_ppid}")
    colaPID.put(os.getpid())

    time.sleep(sleep_time)


    p1_pid = colaPID.get()
    print(f"Proceso2 cambiando la prioridad del Proceso1 con pid: {p1_pid}")
    process1 = psutil.Process(p1_pid)
    process1.nice(10)  # Cambia la prioridad a 10
    print("Proceso2 lanzando un ping a google.com")
    subprocess.run(["ping","-c","4", "google.com"])
    #os.system("ping -c 4 google.com")
    time.sleep(5000)   
    print(f"Proceso2 terminado")
    

if __name__ == "__main__":

    pp_pid = os.getpid()
    print(f"procesoPadre pid: {pp_pid} ppid: {os.getppid()}")
    
    colaPID = mp.Queue()
    
    
    #creamos los procesos
    p1 = mp.Process(target=create_process_1, args=(colaPID,10, pp_pid))
    p2 = mp.Process(target=create_process_2, args=(colaPID,5))


    #iniciamos los procesos
    p2.start()
    p1.start()

    print("Listando todos los procesos")
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == "Python":
            print(proc.info)

    #listamos todos los procesos
    """print("Listando todos los procesos")
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == "proceso1" or proc.info['name'] == "proceso2":
            print(proc.info)"""


    #esperamos a que terminen los procesos
    p1.join()
    p2.join()

    print("ProcesoPadre terminado")


