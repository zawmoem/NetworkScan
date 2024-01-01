# Port Scanner
# Ref https://www.tutorialspoint.com/python_penetration_testing/python_penetration_testing_network_scanner.htm
# Developed by zawmoem 
# Original code was using threading. I am using concurrent. As well as changed output to json
#
# Usage 
# portScan.py --IP <IPv4 network address> 

from socket import *
import subprocess
import ipaddress
import json
import concurrent.futures
import os
import platform
import sys

available_ports= {"open_ports": []}

def portscan(ip_addr,po):
	s = socket(AF_INET, SOCK_STREAM)
	conn = s.connect_ex((ip_addr, po))
	if(conn == 0) :
		available_ports["open_ports"].append(po)
	s.close()

if __name__ == "__main__":

	try:
		if sys.argv[1] == "--IP":
			ip = sys.argv[2]
		else:
			#Accept IP to be scanned
			ip = input('Enter the IP to be scanned: ')
	except:
		ip = input('Enter the IP to be scanned: ')
	
	#Create multiple thread for concurrent ping test	
	executor = concurrent.futures.ThreadPoolExecutor(500)
	scan_port = [executor.submit(portscan, str(ip), i) for i in range (1,500)]

	#To wait until all thread to be completed
	executor.shutdown(wait=True, cancel_futures=True)

	#Combine all resutls to JSON output
	json_open_ports = json.dumps(available_ports, indent=1)

	print(json_open_ports)
			
