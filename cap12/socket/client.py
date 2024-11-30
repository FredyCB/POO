import socket

# Crear el socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectarse al servidor
HOST = '127.0.0.1'  # Dirección del servidor
PORT = 65432        # Puerto del servidor
client_socket.connect((HOST, PORT))

# Enviar datos al servidor
message = input("Mensaje a enviar: ")
client_socket.send(message.encode('utf-8'))

# Recibir respuesta del servidor (recibimos los primeros 1024 bytes)
response = client_socket.recv(1024).decode('utf-8')
print(f"Respuesta del servidor: {response}")

# Cerrar la conexión
client_socket.close()
