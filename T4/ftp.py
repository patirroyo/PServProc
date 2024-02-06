from ftplib import FTP, error_perm

def listCallback(line):
    print(line)

url = 'localhost'
ftp_user = 'admin'
ftp_password = 'preguntaraalberto'


try:
    conn = FTP(url)
    conn.login(ftp_user, ftp_password)
    conn.cwd('/')  # Desplazarse en el árbol
    conn.retrlines('LIST')  # Enumerar archivos
    file_list = conn.nlst()  # Obtener la lista de archivos de la carpeta
    print("Lista de archivos en la carpeta:")
    for file in file_list:
        print(file)

    print("Carpeta actual:", conn.pwd())  # Saber en qué carpeta estamos
    print("Mensaje de bienvenida:", conn.getwelcome())  # Recuperar el mensaje de presentación

    with open('test.txt', 'rb') as f:
        conn.storbinary('STOR test_on_ftp.txt', f)

    conn.retrlines("LIST", listCallback)

    fichero_enServidor = "test_on_ftp.txt"
    fichero_local = "bajado.txt"
    with open(fichero_local, "wb") as file:
        # Usamos el comando RETR para descargar
        conn.retrbinary(f"RETR {fichero_enServidor}", file.write)
except error_perm as e:
    print(f"Error de permisos: {e}")
except Exception as e:
    print(f"Se ha producido un error: {e}")
