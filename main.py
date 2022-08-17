from valid import * #import function vld()

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
	
	for li in f.readlines():
		#Removing "\n" and sending to vld()

		ff.write("%s" %(li.strip()))
		#"strip() will return a copy of the string with the leading and trailing characters removed."
		
		
	f.close()
	ff.close()
	
	
main()




