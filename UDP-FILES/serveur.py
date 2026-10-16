
import socket

serveur = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serveur.bind(("127.0.0.1", 9999))

print("Serveur en attente de l'image...")

with open(r"UDP-FILES\image_recue.jpg", "wb") as fichier:
    while True:
        donnees, adresse = serveur.recvfrom(1024)

        # Compare bytes with bytes
        if donnees == b"EOF":
            print("FIN")
            break

        fichier.write(donnees)

serveur.close()
print("Fin du transfert")
