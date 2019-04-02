from sys import stdin
from collections import deque
B,count,l = {},0,list()

def parse_tree(A):
	global B
	cont = 0
	for i in A:
		c = 1
		if i[c] != ')':
			num = ''
			pos = ''
			while i[c] != ',' and c < len(i):
				num+=i[c]
				c+=1
			pos = i[c+1:len(i)-1]
			B[pos] = num
			cont+=1
			if cont != len(B):
				return False

	return True



def solve():
	global B,count,l
	queue = deque()
	queue.append('')
	while len(queue)!= 0:
		t = queue.popleft()
		if B.get(t) != None:
			count +=1
			l.append(B[t])
			queue.append(t+'L')
			queue.append(t+'R')
			
			




def main():
	global B,count,may,l
	A = stdin.readline().split()

	while len(A)!= 0:
		B = {}
		l = list()
		count = 0
		may = 0
		temp = parse_tree(A)
		if temp:
			solve()
			if count == len(B):
				for i in range(len(l)):
					if i!= len(l)-1:
						print(l[i],'',end = '')
					else:
						print(l[i])
				
			else:
				print("not complete")
					
		else:
			print("not complete")
			
		A = stdin.readline().split()



main()