import time


start_time = time.time()
seconds = 4


while True:
    current_time = time.time()
    elapsed_time = current_time - start_time
    
    if elapsed_time%3 ==0:
        print("Finished iterating in: " + str(int(elapsed_time))  + " seconds")
        