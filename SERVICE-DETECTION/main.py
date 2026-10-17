import socket
import nmap
import time

target = input("Donner la cible: ")
ip = socket.gethostbyname(target)


scanner=nmap.PortScanner()
print("Votre cible est: ",ip)
print("Scanning",ip,"...")
start=time.time()
scanner.scan(hosts=ip,ports="1-1024",arguments="-sV")
nb_ports=0
for host in scanner.all_hosts():
    for proto in scanner[host].all_protocols():
        for port in scanner[host][proto]:
            if scanner[host][proto][port]["state"]=="open":
                nb_ports=nb_ports+1
                print("port:",port)
                print("state: open")
                print("Service",scanner[host][proto][port]["name"])
                print("Version:",scanner[host][proto][port]["version"])

duration=time.time()-start
print("Total open ports:",nb_ports,"in",round(duration,2))