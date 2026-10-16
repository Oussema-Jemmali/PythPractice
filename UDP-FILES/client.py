import socket
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
adresse_serveur = ("127.0.0.1", 9999)
with open(r"UDP-FILES\image.png","rb") as fichier:
    while True:
        bloc = fichier.read(1024)
        if not bloc:
            break
        client.sendto(bloc, adresse_serveur)

client.sendto(b"EOF", adresse_serveur)
client.close()
print("image envoyéé !")