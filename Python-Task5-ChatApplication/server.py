import socket
import threading
from datetime import datetime

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
names = []

running = True


def broadcast(message):
    for client in clients[:]:
        try:
            client.send(message)
        except:
            if client in clients:
                index = clients.index(client)
                clients.remove(client)
                names.pop(index)
                client.close()


def handle_client(client):
    global running

    while running:
        try:
            message = client.recv(1024)

            if not message:
                raise Exception()

            broadcast(message)

        except:
            if client in clients:
                index = clients.index(client)
                username = names[index]

                clients.remove(client)
                names.remove(username)
                client.close()

                timestamp = datetime.now().strftime("%H:%M")

                broadcast(f"[{timestamp}] {username} left the chat.".encode())

                print(f"{username} disconnected.")

            break


def accept_clients():
    global running

    while running:
        try:
            client, address = server.accept()

            print(f"\nConnected: {address}")

            client.send("NAME".encode())

            username = client.recv(1024).decode()

            clients.append(client)
            names.append(username)

            timestamp = datetime.now().strftime("%H:%M")

            broadcast(f"[{timestamp}] {username} joined the chat.".encode())

            print(f"{username} joined the chat.")

            thread = threading.Thread(target=handle_client, args=(client,))
            thread.daemon = True
            thread.start()

        except:
            break


def server_commands():
    global running

    while running:

        command = input()

        if command.lower() == "shutdown":

            print("\nShutting down server...")

            running = False

            for client in clients[:]:
                try:
                    client.send("\nServer is shutting down.".encode())
                    client.close()
                except:
                    pass

            clients.clear()
            names.clear()

            server.close()

            print("Server stopped successfully.")

            break


print("=" * 50)
print("        CHAT SERVER")
print("=" * 50)
print(f"Server running on {HOST}:{PORT}")
print("Type 'shutdown' to stop the server.\n")

accept_thread = threading.Thread(target=accept_clients)
accept_thread.daemon = True
accept_thread.start()

server_commands()