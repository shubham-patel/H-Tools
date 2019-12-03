#!/usr/bin/env python


import subprocess
import optparse
import re


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface")
    elif not options.new_mac:
        parser.error("[-] Please specify a new mac address")
    return options


def mac_change(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])


def current_MAC(interface):
    result = subprocess.check_output(["ifconfig", interface])
    mac_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", result)

    if mac_result:
        return mac_result.group(0)
    else:
        print("[-] Could not read MAC address.")


options = get_arguments()

current_mac = current_MAC(options.interface)
print("Current MAC address : " + str(current_mac))

mac_change(options.interface, options.new_mac)

current_mac = current_MAC(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC address was successfully changed.")
else:
    print("[-] MAC address did not get changed.")
