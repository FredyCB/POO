import socket
from datetime import datetime

# Crear el socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincular el socket a una dirección y puerto
HOST = '127.0.0.1'  # Dirección del servidor (localhost)
PORT = 65432        # Puerto a usar
server_socket.bind((HOST, PORT))

# Escuchar conexiones entrantes
server_socket.listen(1)
print(f"Servidor escuchando en {HOST}:{PORT}")

# Aceptar una conexión
while True:
    conn, addr = server_socket.accept()
    print(f"Conexión establecida con {addr}")

    # Recibir datos del cliente (los primeros 1024 bytes)
    data = conn.recv(1024).decode('utf-8')
    print(f"Recibido: {data}")

    # Responder al cliente
    response = f"Mensaje recibido: {datetime.now()}"
    conn.send(response.encode('utf-8'))

    if data == "exit":
        print("Cerrando el servidor...")
        # Cerrar la conexión
        conn.close()
        break
