import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ("127.0.0.1",9999)

message=input("Votre message : ")
client.sendto(message.encode(), server_address)

print("Message envoyé !")
client.close()