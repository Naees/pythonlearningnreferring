# daemon thread =   a thread that runs in the background, not important for program to run
#                   your program will not wait for daemon threads to complete before exiting
#                   non-daemon threads cannot normally be killed, stay alive until task is complete

#                   ex. background task, garvage collection, waiting for input, long running processes

import threading
import time

def timer():
    print()
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print(f"You are currently logged in for {count} seconds.\n")

# adding daemon will allow this thread to be turned into a daemon thread, therefore allowing us to kill the program
x = threading.Thread(target=timer, daemon=True)
x.start()

# additional learning
# x.setDaemon(True) # change daemon state BUT HAS TO BE USED BEFORE THE .Start() function, as daemons states can't be changed while actively in use
print(x.isDaemon()) # allows us to see if daemon state has been set to TRUE or FALSE

answer = input("Do you wish to exit?") # The main thread is in charged of this input