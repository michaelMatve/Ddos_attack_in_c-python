from scapy.all import *
import time

count = 0
sum = 0
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
    sum += end
    print('{:.6f}s for the calculation'.format(end))
    time.sleep(4)