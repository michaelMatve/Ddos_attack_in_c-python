from scapy.all import *
import time
import csv


f = open('ping_results_p.csv', 'w')
writer = csv.writer(f)
writer.writerow(["Index" , "Time_recev"])


count = 0
conf.verb = 0
while True:
    count = count+1
    start = time.perf_counter()
    packet = IP(dst="192.168.0.4")/ICMP()
    reply = sr1(packet, timeout = 6)
    end = time.perf_counter() - start

    if reply is None:
        end =0.6
    else:
        end = time.perf_counter() - start
    writer.writerow([count ,end])
    print('{:.6f}s for the calculation'.format(end))
    time.sleep(4)
f.close()