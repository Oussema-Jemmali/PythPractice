import socket
import nmap

target = input("Donner la cible : ")
ip = socket.gethostbyname(target)

scanner = nmap.PortScanner()
scanner.scan(ip, "1-1024")

for host in scanner.all_hosts():
    for proto in scanner[host].all_protocols():
        for port in scanner[host][proto]:
            if scanner[host][proto][port]["state"] == "open":
                print("Port", port, "is open")

print("Scan completed!")