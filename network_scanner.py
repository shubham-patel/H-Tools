#!/usr/bin/env python

import scapy.all as scapy
import argparse


def get_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP or IP range")
    option = parser.parse_args()
    return option


def scan(ip):
    arp_req = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_rb = broadcast/arp_req
    ans = scapy.srp(arp_rb, timeout=1, verbose=False)[0]
    data_list = []
    for ele in ans:
        data_dict = {"ip": ele[1].psrc, "mac": ele[1].hwsrc}
        data_list.append(data_dict)
    return data_list


def print_result(result_list):
    print("---------------------------------------------")
    print("IP\t\t\tMAC Address")
    print("---------------------------------------------")
    for data in result_list:
        print(data["ip"] + "\t\t" + data["mac"])


options = get_arg()
scan_result = scan(options.target)
print_result(scan_result)
