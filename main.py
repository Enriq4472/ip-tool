#read file "f"
def readfile():
	fn = str(raw_input("Escreva o nome do arquivo (exemplo: arquivos.txt): "))
	global f
	f = open(fn,"r")

#number of lines
def nlines():
	nl = len(f.readlines())
	return nl
	
#main
def main():
	readfile()
	
	for li in f.readlines():
		print(li)
	
	f.close()
	
main()



