import socket
import datetime

def manejar_cliente(cliente_socket, cliente_direccion):
    try:
        mensaje = cliente_socket.recv(1024).decode('utf-8')
        if mensaje:
            fecha_actual = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            ip_cliente = cliente_direccion[0]
            log_mensaje = f"{fecha_actual} {ip_cliente} - {mensaje}"
            
           
            with open("registro.log", "a") as archivo_log:
                archivo_log.write(log_mensaje + "\n")
            
            print(f"Mensaje recibido: {log_mensaje}")
            cliente_socket.sendall("Información recibida, sistema actuando correctamente".encode('utf-8'))
    finally:
        cliente_socket.close()

def servidor_tcp():
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind(('192.168.1.4', 10000))
    servidor_socket.listen(5)
    print("Servidor en espera de conexiones...")
    while True:
        cliente_socket, cliente_direccion = servidor_socket.accept()
        print(f"Conexión aceptada desde {cliente_direccion}")
        manejar_cliente(cliente_socket, cliente_direccion)

if __name__ == "__main__":
    servidor_tcp()

