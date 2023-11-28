import os

def child_process():
    print("Soy el proceso hijo con PID:", os.getpid())

def parent_process():
    print("Soy el proceso padre con PID:", os.getpid())
    child_pid = os.fork()
    
    if child_pid == 0:
        # Código del proceso hijo
        child_process()
    else:
        # Código del proceso padre
        print("Proceso padre esperando a que el hijo termine...")
        os.waitpid(child_pid, 0)
        print("Proceso hijo ha terminado. Proceso padre finalizando.")

if __name__ == "__main__":
    parent_process()
