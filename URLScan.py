import socket

# Obtener la dirección IP de un enlace HTTP/HTTPS
def get_ip(url):
    try:
        hostname = url.replace('http://', '').replace('https://', '').split('/')[0]
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.gaierror:
        print("No se pudo obtener la dirección IP del servidor.")
        return None

# Función principal
def main():
    url = input("Ingresa la URL del servidor: ")
    ip = get_ip(url)
    if ip:
        print(f"Dirección IP del servidor: {ip}")
    else:
        print("No se pudo obtener la dirección IP del servidor.")

if __name__ == "__main__":
    main()
