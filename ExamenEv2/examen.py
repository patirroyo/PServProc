from scp import SCPClient  
from http.server import BaseHTTPRequestHandler, HTTPServer
import paramiko 
from Crypto.PublicKey import RSA  
from Crypto.Cipher import AES, PKCS1_OAEP
import smtplib
from ftplib import FTP  
import json
from email.message import EmailMessage


class HelloHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)  
        self.send_header('Content-type', 'text/html')  
        self.end_headers()  

    def do_GET(self):
        self.do_HEAD() 
        self.wfile.write("""<html><head><title>Hello
            Gorka</title></head><body><p>HelloWorld</p>
            <form method="POST" >
            <input type="submit" value="Click me"/>
            </form>
            </body></html>""".encode("utf-8")) 


    def do_POST(self):
        self.do_HEAD()
        self.wfile.write("""<html><head><title>Muajajajaj
            </title></head><body><p>Form received</p>
            <img src=https://c.tenor.com/SVHx9p0mH-kAAAAM/the-simpsons-mr-burns.gif>
            </body></html>""".encode("utf-8")) 
        self.get_Documents() 
        
    def get_Documents(self):
        self.downloadSSH() 
        return
        self.desEncrypt() 
        self.writeEncryptedDataTofile() 
        self.loadJson()
        self.sendEmail() 
        self.uploadFTP()  

    def downloadSSH(self):
        print("connect SSH")

        # ssh = paramiko.SSHClient() 
        # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # ssh.connect(hostname='127.0.0.1', port=2222, username='linuxserver', password='password')

        # scp = SCPClient(ssh.get_transport())
        # scp.get('/config/home/encrypted_data.bin') 
        # scp.get('/config/home/private.pem') 
        # scp.close()  
        # ssh.close()  
        self.wfile.write("""
            <hr/><p>SSH hecho</p>""".encode("utf-8")) 
        print("SSH end")

    
    def listCallback(line):
        print(line) 

    
    def writeEncryptedDataTofile(self):
        file_out = open("albertosaz.json", "wb")  
        file_out.write(self.session_key)
        file_out.close() 

    def uploadFTP(self):
        print("Upload FTP") 

        url = self.data["ftp_host"] 

        with FTP(url) as conn:
            conn.login(self.data["ftp_user"], self.data["ftp_password"])  
            conn.cwd('/')  
            print(conn.pwd()) 
            print(conn.getwelcome())  
            with open('albertosaz.json', 'rb') as file:
                conn.storbinary('STOR albertosaz.txt', file) 
            conn.retrlines('LIST', self.listCallback())   
            conn.quit()  
        print("Upload FTP end")

    def sendEmail(self):
        print("Enviar email")
        client = smtplib.SMTP(host=self.data["smtp_host"], port=self.data["smtp_port"])  
        sender = 'alberto@salesianos.edu' 
        dest = 'apruebame@salesianos.edu' 
        with open('albertosaz.json') as fp:
            msg = EmailMessage()
            msg.set_content(fp.read())
        
        msg['Subject'] = 'ExamenAlberto'
        msg['From'] = sender
        msg['To'] = dest
        client.send_message(msg)
        client.quit()  
        print("Enviar email end")


    def desEncrypt(self):
        print("Desencriptar")

        file_in = open("encrypted_data.bin", "rb")  
        private_key = RSA.import_key(open("private.pem").read())  
        enc_session_key = file_in.read(private_key.size_in_bytes())  
        file_in.close()  
        cipher_rsa = PKCS1_OAEP.new(private_key)
        self.session_key = cipher_rsa.decrypt(enc_session_key)  #
        print(self.session_key)  
        print("Desencriptar end")

    def loadJson(self):
        data = open('albertosaz.json', 'r', encoding='utf-8')
        self.data = json.load(data)
        

params = '', 8083
server = HTTPServer(params, HelloHandler)

try:
    server.serve_forever()
except KeyboardInterrupt:
    pass

server.server_close()