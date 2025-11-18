import threading
import time

from datetime import date

today = date.today()
def resetDate():
    while True:
        time.sleep(3)
        print("Reset Occurred: " + str(today))

# Create threads
thread1 = threading.Thread(target=resetDate(), args=("One", 2))

# Start threads
thread1.start()

# Wait for threads to complete
thread1.join()

print("All threads have completed.")