import threading
import time
def square(num):
    print(f"Square:{num*num}")
    time.sleep(1)
def cube(num):
    print(f"Cube:{num*num*num}")
    time.sleep(2)

#Create threads using threading module thread
t1 = threading.Thread(target=square,args=(4,))
#args tasks tuple so give,after 4
t2 = threading.Thread(target=cube,args=(4,))
#t1 = threading.Thread(target=square,args=(4,))
#Start threads
t1.start()
t2.start()

#wait for completion
t1.join()
t2.join()
print("Done!")