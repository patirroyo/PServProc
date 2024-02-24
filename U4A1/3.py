#Enter an IP address and find the country that IP is registered in. 
import requests

def obtener_pais_por_ip(ip):
    url = f"http://ipinfo.io/{ip}/json"
    respuesta = requests.get(url)
    
    if respuesta.status_code == 200:
        datos = respuesta.json()
        pais = datos.get('country', 'No se pudo determinar el país')
        return pais
    else:
        return f"No se pudo obtener la información. Código de estado: {respuesta.status_code}"

if __name__ == "__main__":
    ip_usuario = input("Ingrese una dirección IP: ")
    pais = obtener_pais_por_ip(ip_usuario)
    print(f"La dirección IP {ip_usuario} está registrada en el país: {pais}")
