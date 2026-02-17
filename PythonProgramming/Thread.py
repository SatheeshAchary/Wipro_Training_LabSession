# Thread is light-weight sub process or smallest unit of the process
#Thread is line of execution
#Multi-Threading is the process of execution of concurrent threads at a time without affecting the other threads

#Thread Example
import threading
import time
from importlib.metadata import files
from itertools import count


def task():
    print("Thread start running...")
    time.sleep(2)
    print("Thread is completed!")

t = threading.Thread(target=task)
t.start()
t.join()

#Multi-Threading
def numbers():
    for i in range(5):
        print("Number", i)

def letters():
    for k in "ABCDE":
        print("Letter", k)

t1 = threading.Thread(target=numbers)
t2=threading.Thread(target=letters)

t1.start()
t1.join()

t2.start()
t2.join()

##Real-time Example
def download_file(file_name):
    print("Downloading the files")
    time.sleep(2)
    print(f"{file_name} downloaded")

files = ["file1.txt", "file2.txt", "file3.txt"]

threads = [threading.Thread(target=download_file, args=(file,)) for file in files]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

## Race Condition - when multiple threads access shared data with out synchronization
count = 0
lock = threading.Lock()

def increment():
    global count
    with lock:
        for _ in range(100000):
            count += 1
t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()

t1.join()
t2.join()

print(count)