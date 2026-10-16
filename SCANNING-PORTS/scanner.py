import socket
import time

target = input("Donner votre Target: ")
ip = socket.gethostbyname(target)
print("Target is: ",ip)

debut = time.time()
for port in range(21, 53):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.2)
    resultat = client.connect_ex((ip, port))
    if resultat == 0:
        print("port",port,"open")
    else:
        print("port",port,"closed")
    client.close()
fin = time.time()
duree = fin - debut
print(duree)

