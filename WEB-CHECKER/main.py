import socket
import threading

websites = ["google.com","cloudflare.com","facebook.com","opera.com","microsoft.com"]

def check_website(url):
    ip=socket.gethostbyname(url)
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(2) #It should be before the connection
    r=s.connect_ex((ip,80))
    s.close()
    if (r==0):
        print(f"Website {url} is reachable.")
    else:
        print(f"Website {url} is unreachable.")

threads=[]

for website in websites:
    t=threading.Thread(target=check_website,args=(website,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("All checks Completed!")