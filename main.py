


def readfile():
	fn = str(raw_input("Escreva o nome do arquivo (exemplo: arquivos.txt): "))
	global f

	f = open(fn,"r")



def main():
	readfile()
	
	
	print(f.readline())
	
	
	
	
	f.close()
	
main()




