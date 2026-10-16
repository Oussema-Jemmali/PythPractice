import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1",15555))

print("Connexion etablie avec le serveur.")

print("Adresse local : ", client.getsockname)

while True:
    message  = input("Votre message (A pour arreter la communication) :")
    client.sendall(message.encode())
    if message == "A":
        break

client.close()
print("Client arrete")