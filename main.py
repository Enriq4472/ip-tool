#read file "f"
def readfile():
	fn = str(raw_input("Escreva o nome do arquivo (exemplo: arquivos.txt): "))
	global f
	f = open(fn,"r")

#number of lines
def nlines():
	nl = len(f.readlines())
	return nl+1

#main
def main():
	readfile()
	
	
	#print(f.readline())
	#print(nlines())
	
	
	
	f.close()
	
main()




