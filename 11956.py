from sys import stdin
import math


def hx(x):

	s = []

	while(x >= 10):
		d = x/16 - int(x/16)
		x = int(x/16)
		if(d*16 >= 10):
			if(d*16 == 10):
				s.append('A')
			elif(d*16 == 11):
				s.append('B')
			elif(d*16 == 12):
				s.append('C')
			elif(d*16 == 13):
				s.append('D')
			elif(d*16 == 14):
				s.append('E')
			elif(d*16 == 15):
				s.append('F')
		else:
			s.append(str(int(d*16)))

	s.append(str(x))

	if(len(s) >=2):
		f = s[1] + s[0]
	else:
		f = '0' + s[0]

	return f

def imprimir(l):
	c = 0
	f = []
	while( c < len(l)):
		if(l[c] != '00'):
			tem = hx(l[c])
			f.append(tem)
		else:
			f.append('00')
		c+= 1
	return f	

def mostrar(l):
	print(l[0],end="")
	for i in l[1:]:
		print('',i,end="")
	print()
			
			

def main():
	h = 1
	x = int(input())
	while(h <= x):
		by = ['00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', 
	 	'00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
	 	'00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', 
	 	'00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', 
	 	'00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', 
	 	'00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', 
	 	'00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00']

		s = stdin.readline().strip()
		p = 0
		
	 		 		
		for i in s:

	 		if(i == "<"):
	 			if(p == 0):
	 				p = 99
	 			else:
	 				p-= 1

	 		elif(i == ">"):
	 			if(p == 99):
	 				p = 0
	 			else:
	 				p+= 1

	 		elif(i == "-"):
	 			if(by[p] == 0 or by[p] == '00'):
	 				by[p] = 255
	 			else:
	 				by[p] = int(by[p])
	 				by[p]-= 1

	 		elif(i == "+"):
	 			if(by[p] == 255 ):
	 				by[p] = 0
	 			else:
	 				by[p] = int(by[p])
	 				by[p]+= 1


		"""s = stdin.readline().strip()"""
		print("Case",h,end="")
		print(": ",end="")
		mostrar(imprimir(by))
		h+=1

main()


