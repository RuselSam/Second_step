import ipaddress as ipa
import subprocess as sub
import pprint

ip = ['192.168.88.1', '8.8.8.8', '1.1.1.1', '172.16.0.0', '10.3.1.1', '192.168.88.246']


def ping_ip_addresses(ip_list):
    reachable = []
    unreachable = []
    for addresses in ip_list:
        ip_address = ipa.IPv4Address(addresses)
        ip_address = str(ip_address)
        replay = sub.run(['ping', '-c', '3', '-n', ip_address])
        if replay.returncode == 0:
            ##reachable = reachable.append(addresses)
            ##print(reachable)
            continue
        else:
            ##unreachable = unreachable.append(addresses)
            ##print(unreachable)
            continue

    ##table_to_ipaddresses = [reachable, unreachable]

ping_ip_addresses(ip)

