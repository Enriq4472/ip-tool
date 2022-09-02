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
		#Removing "\n" and sending to vld()
		li=li.strip()
		
		#Handling the ip values
		li = hdlr(li)
		
		#ipclass = class or invalid
		if(vld(li)==1):
			ipclass = clss(li)
		else:
			ipclass = 'unknown'
			
		ipline[ipcount] = ipclass
		ipcount++
		
		'''
		#Writing value in file ipfinal.txt
		#ff.write(li + " - class: " + ipclass + "\n")
		
		#print(vld(li))
		
		#ff.write("%s" %(li.strip()))
		#"strip() will return a copy of the string with the leading and trailing characters removed."
		'''
		
		
	f.close()
	ff.close()
	
	
main()




