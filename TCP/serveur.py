import socket

#1 Creation d'un socket TCP utilisant ipv4
serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 15555

#2 Association le serveur a l'adresse localhost estle port 15555
serveur.bind((host, port))

#3 Autorisation l'attente de connexions entrantes
serveur.listen()

print("Serveur en attente le client ...")

#4 Accepter la connexion
client, adresse = serveur.accept()

print("Client connecté : ",adresse)

#5 Transfere des donnees
while True:
    donnees = client.recv(1024)
    if not donnees:
        break

    message = donnees.decode()
    print("Client :", message)

    if message == "A":
        print("Arret de la communication")
        break

client.close()
serveur.close()

print("Serveur arrete")
