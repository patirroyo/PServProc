import socket
import time

# Dirección y puerto del servidor (B)
SERVER_ADDRESS = ('', 65535)

# Inicia el servidor
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(SERVER_ADDRESS)
    sock.listen(1)
    print("Esperando mensajito...")

    conn, addr = sock.accept()

    with conn:
        print('Uy, cosquillas, me he conectado con:', addr)
        data = conn.recv(1024)
        with open("mensajito_cifrado.bin", "wb") as f:
            f.write(data)
    print("Me ha llegado algo que no entiendo de A, voy a ver si le puedo preguntar a Gorka...")
    time.sleep(1)
    print("Gorka dice: 'No entiendo nada, pero si quieres te lo descifro'")
    time.sleep(1)
    for i in range(100):
        print("descifrando...", i, "%")
        time.sleep(1/100)

    # Descifra el mensaje
    from Crypto.PublicKey import RSA
    from Crypto.Cipher import PKCS1_OAEP
    private_key = RSA.import_key(open("private.pem").read())

    with open("mensajito_cifrado.bin", "rb") as f:
        enc_session_key = f.read(256)

    cipher_rsa = PKCS1_OAEP.new(private_key)
    secret_code = cipher_rsa.decrypt(enc_session_key)
    
    with open("mensajito_descifrado.txt", "wb") as f:
        f.write(secret_code)
    print("Mensaje descifrado y guardado en mensajito_descifrado.txt")
    time.sleep(1)
    print("Gorka dice: 'Vaya, parece que es un mensaje para mí, pero no sé de quién es...'")
    time.sleep(1)
    print("Gorka dice: 'A ver si me entero de algo más...'")
    time.sleep(1)
    print("Gorka dice: 'Ah, sí, es de A, y dice':", secret_code.decode("utf-8"))
    time.sleep(3)
    print("Gorka dice: 'Pero si le he pagado ya...'")

