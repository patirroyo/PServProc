#Enter an IP address and a port range where the program will then attempt to find open ports on the given computer by connecting to each of them. On any successful connections mark the port as open. 
import socket

def scan_ports(ip_address, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port+1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip_address, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except socket.error:
            pass
    return open_ports

ip_address = input("Enter the IP address: ")
start_port = int(input("Enter the starting port: "))
end_port = int(input("Enter the ending port: "))

open_ports = scan_ports(ip_address, start_port, end_port)
print("Open ports:", open_ports)

