"""Usando procesos, abre tres procesos,cada uno de los cuales debe….
	P1: debe abrir el bloc de notas/editor/cmd.exe de texto del sistema que uses
	P2: debes esperar 5 segundos para cambiar la prioridad de P1
	P3: se lanza 2 segundos después de P2 haya arrancado y mata a P1 al instante
	¿Qué es lo que ocurre durante la ejecución?
    
    Que los procesos no se esperan y por lo tanto puede que el proceso 1 y el 3 acaben antes de que el proceso 2 cambie la prioridad del proceso 1 y el programa termine antes de tiempo y el proceso2 no pueda cambiar la prioridad del proceso 1.

    Para ello uso join() para que el proceso padre espero a que terminen los procesos 2 y 3 y así el proceso 2 pueda cambiar la prioridad del proceso 1 y el programa termine correctamente.
    
    ¿Termina el programa correctamente?¿Cómo podrías solucionarlo?

    Si no se usa el join() no termina correctamente, pero se puede solucionar de esa manera o usando la libreria asyncio que permite que los procesos se esperen entre ellos además de ser compatible con los hilos y los procesos.
"""

import os
import subprocess
import time
import psutil
import multiprocessing as mp


def create_process_1(colaPID):
    
    p1_pid = os.getpid()
    p1_ppid = os.getppid()
    
    
    
    colaPID.put(p1_pid)
    
    nano = subprocess.run(["nano"])
    print(f"proceso1 pid: {p1_pid} ppid: {p1_ppid}")
    print(f"Proceso1 lanzando un nano: {nano}")
    
    print(f"Proceso1 terminado")
    

def create_process_2(colaPID):

    p2_pid = os.getpid()
    p2_ppid = os.getppid()
    print(f"Creando Proceso2 (PID: {p2_pid}, PPID: {p2_ppid})")
    
    time.sleep(5) 

    p1_pid = colaPID.get()

    print(f"Proceso2 cambiando la prioridad del Proceso1 con pid: {p1_pid}")
    process1 = psutil.Process(p1_pid)
    process1.nice(10)  # Cambia la prioridad a 10
    
    
    print(f"Proceso2 terminado")
        
def create_process_3():
    time.sleep(2)
    p3_pid = os.getpid()
    p3_ppid = os.getppid()
    print(f"Creando Proceso3 (PID: {p3_pid}, PPID: {p3_ppid})")
    
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'pico':
            print(f"Proceso3 matando al Proceso nano con pid: {proc.info['pid']}")
            os.kill(proc.info['pid'], 9)
            break
    
    print(f"Proceso3 terminado")
    

if __name__ == "__main__":

    pp_pid = os.getpid()
    print(f"procesoPadre pid: {pp_pid} ppid: {os.getppid()}")
    
    colaPID = mp.Queue()
    
    
    #creamos los procesos
    p1 = mp.Process(target=create_process_1, args=(colaPID,))
    p2 = mp.Process(target=create_process_2, args=(colaPID,))
    p3 = mp.Process(target=create_process_3)
    

    #iniciamos los procesos
    p1.start()
    p2.start()
    time.sleep(2)
    #esperamos a que termine el proceso 2
    p2.join()
    p3.start()
    p3.join()
    


    #esperamos a que terminen los procesos
    
    

    print("ProcesoPadre terminado")


