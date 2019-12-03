# H-Tools

Use h-tools.py to access all the files.
[1] Mac Changer : need to provide interface(use ifconfig to know your interface) and mac address
[2] Network Scanner : need to provide IP address or IP range
[3] ARP Spoofer : need to provide target and router IP
[4] Packet sniffer :nothing to be given as input jusst run in bg and let let others use HTTP websites. Can use with ARP Spoofer to get to other's credentials(need to use multiple terminal window to activate both).
[5] DNS Spoofer : need to use the following commands to change the packet chaining: iptables -I FORWARD -j NFQUEUE --queue-num 0 (if want to spoof for any other user's system, need to activate arp spoofer first), to run in own system use iptables -I OUTPUT -j NFQUEUE --queue-num 0 and iptables -I INPUT -j NFQUEUE --queue-num 0 first then run the dns spoofer. Need to provide target website and your infected IP. After finishing don't forget to iptables --flush to make the setting of the queue default.
