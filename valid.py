def vld(ip):
	
	for num in range(0, len(ip)):
		
		if (ip[num]<0 or ip[num]>255):
			return 0
			break
	
	return 1
