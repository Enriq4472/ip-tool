def main():
	readfile()
	
main()




def readfile():
	fn = str(raw_input("Escreva o nome do arquivo (exemplo: arquivos.txt): "))
	
	f = open(fn,"r")

#	print(f.readline())
