import socket

serveur = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serveur.bind(("127.0.0.1",9999))

print("Serveur UDP en attente : ")

donnees, adresse = serveur.recvfrom(1024)
message = donnees.decode()

print("Message recu : ",message)
print("Adresse de client : ",adresse)

serveur.close