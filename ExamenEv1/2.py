# dado el siguiente código hazlo multihilo(0,5 puntos), consigue que la información pueda aparecer ordenada por pantalla y en el fichero se escriba de manera ordenada(2 puntos)
import os
import time
import subprocess
import tempfile
import threading

file_name = os.path.join(tempfile.gettempdir(), os.urandom(24).hex())
lock = threading.Lock()  # Crear un objeto Lock compartido

def code(args):
    name = args
    time.sleep(10)
    with lock:
        with open(file_name, 'a') as f:
            print("guardando en "+file_name)
            f.write("\ncodigo limpio fue escrito por "+str(name))
            subprocess.run(["ping","-c", "4", "google.com"])


    
# llama  a mi metodo usando hilos
h = threading.Thread(target=code, args=("Jesús",))
h.start()

h1 = threading.Thread(target=code, args=("Ismael",))
h1.start()

h2 = threading.Thread(target=code, args=("Nacho",))
h2.start()

h3 = threading.Thread(target=code, args=("Mikel",))
h3.start()

h4 = threading.Thread(target=code, args=("David",))
h4.start()

h.join()
h1.join()
h2.join()
h3.join()
h4.join()