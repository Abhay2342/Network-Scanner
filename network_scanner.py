#!/usr/bin/env python

import scapy.all as scapy
import optparse
from termcolor import colored

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest = "ip", help = "Enter IP Address.")
    options, arguments = parser.parse_args()

    if not options.ip:
        parser.error("[-] Please Enter An IP Address, Use --help For More Info ")
    else:
        return options

def scan(ip):
    arp_request = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request   
    answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout = 1, verbose = False)
    client_list = []
    for element in answered_list:
        client_dict = {"ip" : element[1].psrc, "mac" : element[1].hwsrc}
        client_list.append(client_dict)
    return client_list

def print_result(result_list):
    print("IP Address\t\tMAC Address\n---------------------------------------")
    for result in result_list:
        print(result["ip"], "\t    ",result["mac"])

def about():
		print(colored(" _   _      _                      _          _____                                 ", "green"))
		print(colored("| \ | |    | |                    | |        / ____|                                ", "green"))
		print(colored("|  \| | ___| |___      _____  _ __| | __    | (___   ___ __ _ _ __  _ __   ___ _ __ ", "green"))
		print(colored("| . ` |/ _ \ __\ \ /\ / / _ \| '__| |/ /     \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|", "green"))
		print(colored("| |\  |  __/ |_ \ V  V / (_) | |  |   <      ____) | (_| (_| | | | | | | |  __/ |   ", "green"))
		print(colored("|_| \_|\___|\__| \_/\_/ \___/|_|  |_|\_\    |_____/ \___\__,_|_| |_|_| |_|\___|_|   \n", "green"))
		print(colored("# Author      :", "green") + " Abhay Suryawanshi")
		print(colored("# Linkedin    :", "green") + " https://www.linkedin.com/in/abhay2342/")
		print(colored("# Github      :", "green") + " https://github.com/Abhay2342")
		print(colored("# Title       :", "green") + " Network Scanner")
		print(colored("# Description :","green") + " This is a simple network scanner used to grab mac addresses of a range of IP Addresses.")
		print(colored("# Date        :", "green") + " 29.08.2021")
		print(colored("# Version     :", "green") + " 1.0")
		print(colored("# ==============================================================================\n", "green"))

about()
options = get_arguments()
scan_result = scan(options.ip)
print_result(scan_result)

