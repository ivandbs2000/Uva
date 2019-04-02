from sys import stdin
import math

def main():
	x = int(stdin.readline())
	c = 0
	while(c < x):
		m = 0
		f = 0
		s = stdin.readline().split()

		for i in s:
			if(i[0] == "M"):
				m+=1
			else:
				f+=1
			if(i[1] == "M"):
				m+=1
			else:
				f+=1

		if(m>=2 and f>=2 and f== m):
			print("LOOP")
		else:
			print("NO LOOP")
		c+=1



main()