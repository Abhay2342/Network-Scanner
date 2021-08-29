#!/usr/bin/env python

'''This test file have all the explanation of the working of our network scanner'''

import scapy.all as scapy
import optparse

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
    # print(arp_request.summary())
    # ARP who has Net('10.0.2.1/24') says 10.0.2.42

    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    # print(broadcast.summary())
    # 08:00:27:94:c2:67 > ff:ff:ff:ff:ff:ff (0x9000)

    arp_request_broadcast = broadcast/arp_request
    # print(arp_request_broadcast.summary())
    # Ether / ARP who has Net('10.0.2.1/24') says 10.0.2.42

    answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout = 1, verbose = False)
    client_list = []
    for element in answered_list:
        client_dict = {"ip" : element[1].psrc, "mac" : element[1].hwsrc}
        client_list.append(client_dict)
        # print(element[1].psrc,"\t    ",element[1].hwsrc)
    return client_list


# This is the summary ( working ) of our network scanner :-
    # print(answered_list.summary())

    # Begin emission:
    # Finished sending 256 packets.
    # ****
    # Received 4 packets, got 4 answers, remaining 252 packets
    # Ether / ARP who has 10.0.2.1 says 10.0.2.42 ==> Ether / ARP is at 52:54:00:12:35:00 says 10.0.2.1 / Padding
    # Ether / ARP who has 10.0.2.2 says 10.0.2.42 ==> Ether / ARP is at 52:54:00:12:35:00 says 10.0.2.2 / Padding
    # Ether / ARP who has 10.0.2.3 says 10.0.2.42 ==> Ether / ARP is at 08:00:27:c9:99:67 says 10.0.2.3 / Padding
    # Ether / ARP who has 10.0.2.15 says 10.0.2.42 ==> Ether / ARP is at 08:00:27:e6:e5:59 says 10.0.2.15 / Padding
    # None

def print_result(result_list):
    print("IP Address\t\tMAC Address\n---------------------------------------")
    for result in result_list:
        print(result["ip"], "\t    ",result["mac"])

options = get_arguments()

scan_result = scan(options.ip)

print_result(scan_result)
