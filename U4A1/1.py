#A file transfer program which can transfer files back and forth from a remote ftp sever.


from ftplib import FTP 

# Connect to the FTP server
url = "127.0.0.1"
username = "admin"
password = "preguntaraalberto"
ftp = FTP(url)
ftp.login(username, password)

# Upload a file to the server
with open("local_file.txt", "rb") as file:
    ftp.storbinary("STOR remote_file.txt", file)

# Download a file from the server
with open("downloaded_file.txt", "wb") as file:
    ftp.retrbinary("RETR remote_file.txt", file.write)

# List the files in the current directory
ftp.retrlines('LIST')

# Disconnect from the FTP server
ftp.quit()