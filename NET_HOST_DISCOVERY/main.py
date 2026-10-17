import socket
import nmap
pool=input("Donner la plage d'adresse: ")
scanner=nmap.PortScanner()
scanner.scan(hosts=pool,arguments="-sn")
nb=0
for host in scanner.all_hosts():
    if scanner[host].state=="up":
        print("host discovered:",host)
        nb=nb+1

print("total host is:",nb)