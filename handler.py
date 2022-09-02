def hdlr(ip):
	ip = ip.split(".")
	
	#converting all itens in list to integer
	for num in range(0, len(ip)):
		ip[num]=int(ip[num])
	
	return ip
