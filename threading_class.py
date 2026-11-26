import threading

def greet():
    print("Hello from the thread")

t1 = threading.Thread(target=greet)
t1.start()