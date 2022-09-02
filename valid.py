def vld(ipstr):
	ip = ipstr.split(".")
	
	for num in range(0, len(ip)):
		#ip[num]=int(ip[num])
		
		if (ip[num]<0 or ip[num]>255):
			return False
			break
	
	return True
