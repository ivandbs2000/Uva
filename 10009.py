from sys import stdin
from collections import deque


def dfs(l,i,f):

	queue = deque()
	visited = [[0,-1] for _ in range(len(l))]
	queue.append(i)
	
	visited[i][0] = 1
	c = -3
	while len(queue) != 0 and c != f:
		c = queue.popleft()
		for e in l[c]:
			if visited[e][0] == 0:
				visited[e][0] = 1
				visited[e][1] = c
				queue.append(e)
	g = c
	l = list()
	l.append(chr(g+65))

	while visited[g][1] != -1:
		g = visited[g][1]
		l.append(chr(g+65))
		

	return l



def main():

	n = int(stdin.readline())
	x = 0
	for _ in range(n):
		if x == 1:
			print()

		k = stdin.readline()
		a,b = map(int,(stdin.readline().split()))
		l = [[] for _ in range(26)]

		for i in range(a):

			cO,cT = stdin.readline().split()
			cO = ord(cO[0])-65
			cT = ord(cT[0])-65
			l[cO].append(cT)
			l[cT].append(cO)
		
		for _ in range(b):
			c1,c2 = stdin.readline().split()
			c1 = ord(c1[0])-65
			c2 = ord(c2[0])-65

			final =dfs(l,c1,c2) 
			li = len(final)-1
			while li >= 0:
				print(final[li],end = '')
				li-=1
			print()


		x= 1

main()