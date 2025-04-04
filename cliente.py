import socket
import platform
import psutil

def obtener_informacion_sistema():
    nombre_equipo = platform.node()
    cpu_modelo = platform.processor()
    carga_cpu = psutil.cpu_percent(interval=1)
    memoria_ram = psutil.virtual_memory().percent
    
    informacion = (
        f"Nombre del equipo: {nombre_equipo}\n"
        f"Modelo de CPU: {cpu_modelo}\n"
        f"Carga de CPU: {carga_cpu} %\n"
        f"Consumo de RAM: {memoria_ram} %"
    )
    return informacion

def cliente_tcp():
    servidor_ip = '192.168.1.4' 
    puerto = 10000
    
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect((servidor_ip, puerto))
    
    try:
        informacion = obtener_informacion_sistema()
        print(f"Enviando información:\n{informacion}")
        cliente_socket.sendall(informacion.encode('utf-8'))
        
        respuesta = cliente_socket.recv(1024).decode('utf-8')
        print(f"Respuesta del servidor: {respuesta}")
    finally:
        cliente_socket.close()

if __name__ == "__main__":
    cliente_tcp()