import threading

def greet(name,age):
    print("Hello",name,age)
    print("name:",name)
    print("age:",age)

t1 = threading.Thread(args=("Arjun",23),target=greet)
t1.start()
t1.join()