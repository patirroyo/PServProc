import socket

# Dirección y puerto del cliente (A)
input = input("Introduce la dirección IP del destino, si no introduces nada se usará la dirección por defecto: localhost")
SERVER_ADDRESS = (input, 65535)

# Lee el archivo cifrado
with open("encrypted_data.bin", "rb") as f:
    data = f.read()

# Inicia la conexión con el servidor
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(SERVER_ADDRESS)
    sock.sendall(data)
    print("Mensajito para Gorka enviado a B")