from sys import stdin
import math


def buscar(lista, name):

	for i  in range(len(lista)):
		if(lista[i] == name):
			return i


def main():
	y = 0
	m = stdin.readline().strip()
	while(m != ''):
		
		if(y != 0):
			print()

		
		m = int(m)
		
		lf = [0]*10

		name = stdin.readline().split()	

		c = 0
		while(c < m):

			temp  = stdin.readline().split(	)
			temp[1] = int(temp[1])
			temp[2] = int(temp[2])
			i = buscar(name, temp[0])
			if(temp[1] == 0 or temp[2] == 0):
				c+=1
				continue

			k = int(temp[1]/temp[2])	
			lf[i] += (-k*temp[2] )	
			
			for e in temp[3:]:
				ind = buscar(name,e)
				lf[ind] += k 		

			c+= 1

		
		for i in range(len(name)):
			print(name[i],lf[i])
		y+= 1
		m = stdin.readline().strip()


main()
