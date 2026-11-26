import threading
import time
def greet():
    print("Hello from the thread")
    time.sleep(2)
def greet1():
    print("Hello from the thread 1")
    time.sleep(2)
def greet2():
    print("Hello from the thread 2")
    time.sleep(2)
t1 = threading.Thread(target=greet)
t2 = threading.Thread(target=greet1)
t3 = threading.Thread(target=greet2)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("Main program ended.")