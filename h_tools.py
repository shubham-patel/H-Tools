#!/usr/bin/env python
# -*- coding: ascii -*-

import subprocess

from pip._vendor.distlib.compat import raw_input

subprocess.call(["clear"])

print("\n\n")
print("  __    __             .___________.   ______      ______     ___            ________.   ")
print(" |  |  |  |            |           |  /  __  \    /  __  \   |   |          /        |   ")
print(" |  |__|  |   ______   `---|  |----` |  |  |  |  |  |  |  |  |   |         |   (-----`   ")
print(" |   __   |  |______|      |  |      |  |  |  |  |  |  |  |  |   |         \    \        ")
print(" |  |  |  |                |  |      |  `--'  |  |  `--'  |  |   `-----.-----)   |       ")
print(" |__|  |__|                |__|       \______/    \______/   |_________|________/        ")
print("                                                                                         ")

print("please read all the instructions given in the readme to use this tool without any issues")
print("\n\n\n")
print(" [1] MAC Changer")
print(" [2] Network Scanner")
print(" [3] ARP Spoofer")
print(" [4] Packet Sniffer")
print(" [5] DNS Spoofer")
print(" [0] Exit")
print("[99] Update")
opt = int(input("\nEnter your choice :"))

if opt is 1:
    subprocess.call(["clear"])
    interface = raw_input("Interface:")
    mac = raw_input("new MAC:")
    subprocess.call(["python", "mac_changer.py", "-i ", interface, "-m", mac])

elif opt is 2:
    subprocess.call(["clear"])
    IP = raw_input("IP/Range:")
    subprocess.call(["python", "network_scanner.py", "-t", IP])

elif opt is 3:
    subprocess.call(["clear"])
    target = raw_input("Target IP:")
    router = raw_input("Router IP:")
    subprocess.call(["python", "arp_spoofer.py", "-t", target, "-r", router])

elif opt is 4:
    subprocess.call(["clear"])
    subprocess.call(["python", "packet_sniffer.py"])


elif opt is 5:
    subprocess.call(["clear"])
    target = raw_input("Target Website:")
    ip = raw_input("Redirect IP:")
    subprocess.call(["python", "dns_spoofer.py", "-t", target, "-r", ip])

elif opt is 0:
    subprocess.call(["clear"])
    exit()

elif opt is 99:
    subprocess.call(["clear"])
    subprocess.call(["git", "clone", "https://www.github.com/shubham-patel/H-Tools"])
    print("[+] Update Complete")

else:
    print("[-] Invalid Choice")
