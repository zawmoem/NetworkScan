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
import os
import platform
import sys

active_hosts= {"active_ip_addrs": []}
inactive_hosts= {"inactive_ip_addrs": []}

def pingsweep(cmdPing, ip_addr):
	
	#Run ping command with IP address
	response = os.popen(cmdPing + " " + ip_addr)

	#Check ping result
	for line in response.readlines():
		if(line.count("TTL")):
			active_hosts["active_ip_addrs"].append(ip_addr)
			exit
	inactive_hosts["inactive_ip_addrs"].append(ip_addr)

if __name__ == "__main__":

	# Verification of the command line parameters 		
	if len(sys.argv) < 1:
		network = ipaddress.ip_network(input("Enter the network to scan : "))
	if sys.argv[1] == "--network":
		network = ipaddress.ip_network(sys.argv[2])

	# convert network to list of IPs		
	hosts = network.hosts()

	# Verification of Operation System
	oper = platform.system()
	# Based on OS, different Ping Command need to be used
	if (oper == "Windows"):
		cmdPing = "ping -n 1 -w 1000"
	elif (oper == "Linux"):
		cmdPing = "ping -c 1 "
	else :
		cmdPing = "ping -c 1 "

	# Create multiple thread for concurrent ping test	
	executor = concurrent.futures.ThreadPoolExecutor(254)
	ping_hosts = [executor.submit(pingsweep, cmdPing, str(ip)) for ip in hosts]

	#To wait until all thread to be completed
	executor.shutdown(wait=True, cancel_futures=True)

	#Combine all resutls to JSON output
	json_active_hosts = json.dumps(active_hosts, indent=1)
	json_inactive_hosts = json.dumps(inactive_hosts, indent=1)

	#Check the command line output whether is there any filter
	#If there is no filter default is show both active and inactive hosts
	if len(sys.argv) < 4:
		print(json_active_hosts, json_inactive_hosts)
	else:
		if sys.argv[3] == "--active":
			print(json_active_hosts)
		if sys.argv[3] == "--inactive":
			print(json_inactive_hosts)
		if sys.argv[3] == "--all":
			print(json_active_hosts, json_inactive_hosts)
