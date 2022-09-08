from handler import * #import function hdlr()
from valid import * #import function vld()
from classip import * #import funcion clss()

#read file "f"
def readfile():
	fn = str(input("Escreva o nome do arquivo (exemplo: arquivos.txt): "))
	global f
	f = open(fn,"r")

#number of lines
def nlines():
	nl = len(f.readlines())
	return nl
	
#main
def main():
	readfile()
	
	ff = open("ipfinal.txt", "w")
	
	ipcount=0
	for li in f.readlines():
		rawip = li 
		#Removing "\n" and sending to vld()
		li=li.strip()
		rawip = rawip.strip()
		
		#Handling the ip values
		li = hdlr(li)
		
		#ipclass = class or invalid
		if(vld(li)==1):
			ipclass = clss(li)
		else:
			ipclass = '?'
			
		
		ff.write("%s - class: %c\n" %(rawip, ipclass))
		
		#"strip() will return a copy of the string with the leading and trailing characters removed."
	
	f.close()
	ff.close()
	
	
main()




