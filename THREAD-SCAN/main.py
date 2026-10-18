import threading
import socket
import queue

# Store the ports that must be scanned
queue_ports = queue.Queue()

def portscan(port):
    target= "127.0.0.1"
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(0.2)
    res=s.connect_ex((target,port))
    s.close()
    if res==0:
        print("port",port,"open")
    else:
        print("port",port,"closed")
    
def threader():
    while True:
        # Get the next port from the queue
        port = queue_ports.get()

        portscan(port)

        # Mark this queue item as completed
        queue_ports.task_done()

for _ in range(100):
    thread = threading.Thread(target=threader, daemon=True)
    thread.start()

for port in range(1, 1024):
    queue_ports.put(port)

queue_ports.join()
print("scan finished")