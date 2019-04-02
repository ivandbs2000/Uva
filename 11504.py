#discutido con Juan esteban cardona

from sys import stdin
from collections import deque
import sys
sys.setrecursionlimit(100000)
d = deque()
G = list()
I = list()
points = list()
visited = list()

scc_cnt = 0

def dfsI(n):
	global visited,d,I
	visited[n] = 1
	for i in I[n]:
		if visited[i] == 0 :
			dfsI(i)

	d.appendleft(n)
	return 

def dfs(n):
	global visited,G,points,scc_cnt
	visited[n] = 1
	points[n] = scc_cnt
	for i in G[n]:
		if visited[i] == 0:
			dfs(i)

	return 


def main():
	global d,G,I,visited,scc_cnt,points

	cases = int(stdin.readline())
	k = 1
	while k <= cases:

		#Entrada
		T,case = list(map(int,stdin.readline().split()))
		G  = [[] for _ in range(T+1)]

		for j in range(case):
			x,y = list(map(int,stdin.readline().split()))
			G[x].append(y)

		print(G)
		#invierto el grafo
		I = [[] for _ in range(T+1)]

		for j in range(1,len(G)):
			for v in G[j]:
				I[v].append(j)

		#dfs con el grafo invertido
		visited = [0 for _ in range(T+1)]
		d = deque()
		for j in range(1,len(G)):
			if visited[j] == 0:
				dfsI(j)
		print(d)
		points = [-1 for i in range(len(G))]
		scc_cnt = 0
		visited = [0 for i in range(len(G))]

		for u in d:
			if visited[u] == 0:
				scc_cnt+=1
				dfs(u)
				
		print(points)
		arr = [0 for _ in range(scc_cnt)]

		for u in range(1,len(G)):
			for v in G[u]:
				if points[u] != points[v] :
					arr[points[v]]+=1
		print(arr)
		c = 0
		for i in range(len(arr)):
			if arr[i] == 0:
				c += 1

		print("Case {0}: {1}".format(k,c))
		k+=1
		#hago el dfs para los dominos
main()
