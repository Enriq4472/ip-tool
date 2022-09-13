def clss(ip):
	if(ip[0]>=1 and ip[0]<=127):
		return 'A'
	
	elif(ip[0]>=128 and ip[0]<=191):
		return 'B'
	
	elif(ip[0]>=192 and ip[0]<=223):
		return 'C'
	
	elif(ip[0]>=224 and ip[0]<=239):
		return 'D'
	
	else:
		return 'E'
