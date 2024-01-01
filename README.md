"""
# NetworkScan
 Use case: 
 To scan the management network to identify swtiches, routers and other networking devices. Improvment features will be check their hardware model, firmware version and serial numbers.
 
 Version Beta:
	- pingScan:
		+ Similar to ping sweep.
		+ Use OS base ping command
		+ Send ICMP request only one
		+ Check the output whether is there any TTL (Windows) or ttl (Linux)
		
		+ Accept network address with subnet
		+ Output is in json format whether as in Active IP List or Inactive IP List
		
		> Usage
		> portScan.py --network <network address>/<subnet> --active
		> portScan.py --network <network address>/<subnet> --inactive
		> portScan.py --network <network address>/<subnet> --all 
		! If there is no command parameters
		> portScan.py
		> Enter the network to scan : 
		
	
	- portScan
		+ Similar to nmap
		+ Use socket library
		
		+ Accept IP address
		+ Output is in json format only avaialable/open port between 50-500
		
		> Usage
		> portScan.py --IP <ip address>
		! If there is no command parameters
		> portScan.py
		> Enter the IP to be scanned:
		
		
	
"""