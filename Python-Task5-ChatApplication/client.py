import socket
import threading
from datetime import datetime

HOST = "127.0.0.1"
PORT = 5000

name = input("Enter your name: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


def receive():
    while True:
        try:
            message = client.recv(1024).decode()

            if message == "NAME":
                client.send(name.encode())
            else:
                print(message)

        except:
            print("\nDisconnected from server.")
            client.close()
            break


def write():
    while True:
        message = input()

        if message.lower() == "exit":
            print("Leaving chat...")
            client.close()
            break

        timestamp = datetime.now().strftime("%H:%M")

        full_message = f"[{timestamp}] {name}: {message}"

        try:
            client.send(full_message.encode())
        except:
            break


print("\nType your messages below.")
print("Type 'exit' to leave the chat.\n")

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()