def vld(ipstr):
	ip = ipstr.split(".")
	
	#converting all itens in list to integer
	for num in range(0, len(ip)):
		ip[num]=int(ip[num])
		
		if (ip[num]<0 or ip[num]>255):
			return False
			break
	
	return True
