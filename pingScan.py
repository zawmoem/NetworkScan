# Ping Scanner
# Ref https://medium.com/@vickycena94/network-scanning-and-more-with-python-with-multithreading-d-a8590e1da064
# 29 Dec 2023 Updated by zawmoem 
# Original code is meant for Linux environemt and updated to suit it in Windows
# 
# Usage 
# pingScan.py --network <IPv4 network address>/<mask> --all/--active/--inactive 

import subprocess
import ipaddress
import json
import concurrent.futures

import sys

active_hosts= {"active_ip_addrs": []}
inactive_hosts= {"inactive_ip_addrs": []}

def pingda(ip_addr):

#Windows 
#Ref https://stackoverflow.com/questions/35750041/check-if-ping-was-successful-using-subprocess-in-python
#
	canPing = subprocess.call('ping -n 1 -w 500 %s' % ip_addr,stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)
	if canPing == 0:
		active_hosts["active_ip_addrs"].append(ip_addr)
	if canPing == 1:
		inactive_hosts["inactive_ip_addrs"].append(ip_addr)

#Linux	
#    try:
#        subprocess.check_output(["ping", "-c", "1", ip_addr])
#        active_hosts["active_ip_addrs"].append(ip_addr)
#    except:
#        inactive_hosts["inactive_ip_addrs"].append(ip_addr)

if __name__ == "__main__":
		
	if len(sys.argv) < 1:
		network = ipaddress.ip_network(input("Enter the network to scan : "))
	
	if sys.argv[1] == "--network":
		network = ipaddress.ip_network(sys.argv[2])
		
	hosts = network.hosts()
	
	executor = concurrent.futures.ThreadPoolExecutor(254)
	ping_hosts = [executor.submit(pingda, str(ip)) for ip in hosts]

	#this line was added to wait until all thread to be completed
	executor.shutdown(wait=True, cancel_futures=True)

	json_active_hosts = json.dumps(active_hosts, indent=1)
	json_inactive_hosts = json.dumps(inactive_hosts, indent=1)

	if len(sys.argv) < 4:
		print(json_active_hosts, json_inactive_hosts)
	else:
		if sys.argv[3] == "--active":
			print(json_active_hosts)
		if sys.argv[3] == "--inactive":
			print(json_inactive_hosts)
		if sys.argv[3] == "--all":
			print(json_active_hosts, json_inactive_hosts)
