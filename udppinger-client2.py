import time
import sys
from socket import *

# Create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# To set waiting time of one second for reponse from server
clientSocket.settimeout(1)
# Declare server's socket address
remoteAddr = (sys.argv[1],12000)

start_time = time.time()
i = 0

rtts = []
timeouts = 0

while True:
    
    current_time = time.time()
    elapsed_time = current_time - start_time
    
    if elapsed_time % 3 == 0:
        i+=1
        sendTime = time.time()
        message = 'PING ' + str(i) + ", time:" + str(time.strftime("%H:%M:%S"))
        clientSocket.sendto(message, remoteAddr)
        
        try:
            data, server = clientSocket.recvfrom(1024)
            recdTime = time.time()
            rtt = recdTime - sendTime
            rtts.append(rtt)
            print ("Message:", data)
            print ("RTT:", rtt)
        
        except timeout:
            print ('REQUEST TIMED OUT')
            timeouts += 1
        print
    if elapsed_time == 120:
        # Part 2
        print("Max RTT: " + str(max(rtts)))
        print("Min RTT: " + str(min(rtts)))
        print("Total # of RTTs: " + str(len(rtts)))
        print("Package Loss Rate: " + str(float(timeouts)/float(i) * 100) + "%")
        print("Average RTT: " + str(sum(rtts) / len(rtts)))
        break