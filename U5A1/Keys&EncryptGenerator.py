from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import PKCS1_OAEP


key = RSA.generate(2048)
private_key = key.export_key()
file_out = open("B/private.pem", "wb")
file_out.write(private_key)
file_out.close()

public_key = key.publickey().export_key()
file_out = open("A/public.pem", "wb")
file_out.write(public_key)
file_out.close()

secret_code = """
Estaba yo tranquilamente yendo al poblado en tren
cuando de repente me acordé que Gorka me debía 20 euros
(eso lo ha escrito Copilot, no yo, que conste)
me acordé que me quedaba este juego todavia""".encode("utf-8")

file_out = open("A/encrypted_data.bin", "wb")

recipient_key = RSA.import_key(open("A/public.pem").read())
session_key = get_random_bytes(16)

# Encrypt the session key with the public RSA key
cipher_rsa = PKCS1_OAEP.new(recipient_key)
enc_session_key = cipher_rsa.encrypt(secret_code)

file_out.write(enc_session_key)
file_out.close()