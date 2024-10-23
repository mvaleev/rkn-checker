#!/usr/bin/python3

import re
import pytricia
import argparse
from argparse import RawTextHelpFormatter

parser = argparse.ArgumentParser(description='RKN IP Checker',formatter_class=RawTextHelpFormatter)
parser.add_argument('-d', '--data_file', dest='data_file',  type=str, required=True, help='CSV dump file from here https://github.com/zapret-info/z-i/blob/master/dump.csv.\n\n', metavar='<filename>')
parser.add_argument('-i', '--ip_address', dest='ip_address',  type=str, required=True, help='IP address to check in dump.\n\n', metavar='<ip address>')


args = parser.parse_args()
data_file = args.data_file
ip_addr = args.ip_address

trie = pytricia.PyTricia()

def extract_ipv4_addresses(line):
    ipv4_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    return re.findall(ipv4_pattern, line)

with open(data_file, 'r', encoding='utf-8', errors='replace') as file:
    for line in file:
        ipv4_addresses = extract_ipv4_addresses(line)
        for ipv4 in ipv4_addresses:
            trie[ipv4] = 'IP Address'

result = trie.has_key(ip_addr)
if result:
    print(f'IP {ip_addr} banned.')
else:
    print(f'IP {ip_addr} not found in dump.')


