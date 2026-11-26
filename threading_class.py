import threading

def greet():
    print("Hello from the thread")
def greet1():
    print("Hello from the thread 1")
def greet2():
    print("Hello from the thread 2")
t1 = threading.Thread(target=greet)
t2 = threading.Thread(target=greet1)
t3 = threading.Thread(target=greet2)

t1.start()
t2.start()
t3.start()
