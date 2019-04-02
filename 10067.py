#discuti con Bantu Agustin Valencia la forma de sacar los 8 siguientes numeros sin usar tuplas , listas o string solo numeros

from sys import stdin
from collections import deque

visited = list()
dist = list()
mod = [1000,100,10,1]

def num(t):
	return t[0]*1000 + t[1]*100 +t[2]*10 + t[3]



def bfs(ini,end):
	global visited,dist,mod

	queue = deque()
	queue.append(ini)
	visited[ini] = 1
	dist[ini] = 0
	while len(queue)!= 0 and dist[end] == -1 :
		x = queue.popleft()

		for i in range(4):
			a,b = 0,0
			r = (x//mod[i])%10
			if r == 9:
				a = x - 9*mod[i]
				b = x - mod[i]

			elif r == 0:
				a = x + 9*mod[i]
				b = x + mod[i]

			else:
				a = x + mod[i]
				b = x - mod[i]
		
			if visited[a] == 0:
				visited[a] = 1
				dist[a] = dist[x] + 1
				queue.append(a)

			if visited[b] == 0:
				visited[b] = 1
				dist[b] = dist[x] + 1
				queue.append(b)






	


def main():
	global visited,dist
	
	cases = int(stdin.readline())

	for i in range(cases):
		c = stdin.readline()
		start= list(map(int,stdin.readline().split()))
		end = list(map(int,stdin.readline().split()))
		case = int(stdin.readline())
		visited = [0 for _ in range(10000)]
		dist = [-1 for _ in range(10000)]

		for j in range(case):
			temp = list(map(int,stdin.readline().split()))
			visited[num(temp)] = 1
		
		bfs(num(start),num(end))
		print(dist[num(end)])

	print()

main()

