import threading
import time

def worker(number):
    print("Worker",number,"started")
    time.sleep(2)
    print("Worker",number,"finished")

threads=[]

for i in range(1,6):
    t = threading.Thread(target=worker,args=(i,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("All workers finished!")
