from scp import SCPClient
from http.server import BaseHTTPRequestHandler,HTTPServer
import paramiko
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
import smtplib
from ftplib import FTP

params='',8083
class   HelloHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
    def do_GET(self):
        self.do_HEAD()
        self.wfile.write("""<html><head><title>Hello
            Gorka</title></head><body><p>HelloWorld</p>
            <form method="POST" >
            <input type="submit" value="Click me">
                <img src="https://imgs.search.brave.com/pBeJWe6LJKO24PheFi1S1IkMEiCKTaePqGQnPGY1EOg/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvMTI2/MTM0MDQyMy92ZWN0/b3IvcmFkaW9hY3Rp/dmUtc3ltYm9sLWlj/b24tc2V0LW51Y2xl/YXItcmFkaWF0aW9u/LXdhcm5pbmctc2ln/bi1hdG9taWMtZW5l/cmd5LWxvZ28tdmVj/dG9yLmpwZz9zPTYx/Mng2MTImdz0wJms9/MjAmYz1kVVhlZVVM/SEwwUzJlN0lEYU1B/TGdoYWtCTFprM0th/MlltSVZLLUNZYml3/PQ">
                         </input>
            </form>
            </body></html>""".encode("utf-8"))
    def do_POST(self):
        self.do_HEAD()
        self.wfile.write("""<html><head><title>Hello
            World</title></head><body><p>Form received</p>
            </body></html>""".encode("utf-8"))
    
    
    def get_Documents(self):
        self.connectSSH()
        self.desEncrypt()
        self.writeEncryptedDataTofile()
        self.sendEmail()
        self.uploadFTP()

    def connectSSH(self):
        print("connect SSH")
        print(self.rfile.read())
        print("SSH end")

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(hostname='192.168.1.123', port='2222',username='alumno', password='salesianos')

        # SCPCLient takes a paramiko transport as an argument
        scp = SCPClient(ssh.get_transport())
        scp.get('encripted.bin')
        scp.get('private.pem')
        scp.close()
        ssh.close()
        print("SSH end")

    def listCallback(line):
        print(line)

    def writeEncryptedDataTofile(self):
        # write session key to file
        file_out = open("albertosaz.txt", "wb")
        file_out.write(self.session_key)
        file_out.close()


    def uploadFTP(self):
        print("Upload FTP")

        url = 'localhost'
        with FTP(url) as conn:
            conn.login('admin','preguntaalprofesor')
            conn.cwd('/')
            print(conn.pwd())
            print(conn.getwelcome())

            with open('albertosaz.bin', 'rb') as file:
                conn.storbinary('STOR albertosaz.bin', file)

            conn.retrlines('LIST', self.listCallback)
            conn.quit()
        print("Upload FTP end")

    def sendEmail(self):
        print("Enviar email")
        client= smtplib.SMTP(host='localhost', port=3025)
        sender = 'alberto@salesioanos.edu'
        dest = 'apruebame@salesianos.edu'
        message=self.sesion_key
        message_template = 'From:%s\r\nTo:%s\r\n\r\n%s'
        client.set_debuglevel(1)
        client.sendmail(sender,dest,message_template%(sender,dest,message))
        client.quit()
        print("Enviar email end")

    def desEncrypt(self):
        print("Desencriptar")
        

        file_in = open("encrypted_data.bin", "rb")
        private_key = RSA.import_key(open("private.pem").read())
        enc_session_key = file_in.read(private_key.size_in_bytes())
        file_in.close()

        # Decrypt the session key with the private RSA key
        cipher_rsa = PKCS1_OAEP.new(private_key)
        self.session_key = cipher_rsa.decrypt(enc_session_key)
        print(self.session_key)
        print("Desencriptar end")

server=HTTPServer(params,HelloHandler)

try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
server.server_close()