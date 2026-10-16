import socket
import time

def get_target():
    target=input("Enter the IP or the hostname of target: ")
    ip=socket.gethostbyname(target)

    return ip

def get_port_list():
    start_port = int(input("Give the starting port: "))
    end_port = int(input("Give the ending port: "))
    return range(start_port, end_port+1)

def scan_port(target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.2)
    res=s.connect_ex((target,port))
    s.close()
    if res==0:
        print(("Port",port,"open"))
    else:
        print(("Port",port,"closed"))

def port_scanner(target,ports):
    start=time.time()
    for port in ports:
        scan_port(target,port)

    duration = time.time() - start
    print("scan finished in",duration)
