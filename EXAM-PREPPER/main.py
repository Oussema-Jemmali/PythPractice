import socket
import threading
import queue
target=input("Donner votre cible: ")
ip=socket.gethostbyname(target)
print("Votre cible est : ",ip)
qeuee=queue.Queue()

for i in range(21,81):
     qeuee.put(i)

def PORTSCANNER():
    while not qeuee.empty():
        try:
                i = qeuee.get_nowait()
        except queue.Empty:
                break
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        i = qeuee.get_nowait()
        s.settimeout(0.2)
        res=s.connect_ex((ip,i))
        if res == 0:
            print("Port",i,"open")
        else:
            print("Port",i,"closed")
        s.close()
        qeuee.task_done()

threads=[]
for i in range(5):
     t=threading.Thread(target=PORTSCANNER,daemon=True)
     t.start()
     threads.append(t)

for thread in threads:
     thread.join()

print("Scan finished in")