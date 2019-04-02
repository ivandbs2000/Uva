from sys import stdin
from collections import deque
import sys
sys.setrecursionlimit(100000)

A = list()
visited = list()
dist = list()
ci = 0
m = (0,0)

#si es un ciclo las lleno todos con ese valor

def fill(n,v):
	global visited, dist, A,m
	visited[n] = 2
	queue = deque()
	queue.append(n)
	
	while len(queue)!= 0:
		t = queue.popleft()	
		x = A[t][0]
		if visited[x] != 2: 
			visited[x] = 2
			queue.append(x)
			dist[x] = v
			
#i ya tiene un 2 significa que hice el camino y solo se lo sumo,si es un ciclo llamo a fill
#me doy cuenta que es un cuclo cuando al que apunta mi n ya esta visitado 


def bfs(n):

	global visited, dist,A,band,ci,m
	s = A[n][0]
	if visited[s] == 2:
		visited[n] = 2
		dist[n] += dist[s] + 1
		return dist[n]

	if visited[s] == 0:
		visited[s] = 1
		dist[n] = (bfs(s)) + 1
		if ci == n:
			fill(n,dist[n])
			ci = 0
		return dist[n]
	
	elif visited[s] == 1 and dist[s] == 0:
		ci = s
				
		return 0
	else:
		dist[n] = dist[s] + 1
		return dist[n]

def source(siz):
	global visited,m,dist,A

	for i in range(1,siz):
		if visited[i] == 0 and len(A[i]) > 0 :
			visited[i] = 1
			bfs(i)
			
		
		if dist[i] > m[0]:
			m = (dist[i],i)

def main():
	global A,visited,dist,m
	cases = int(stdin.readline())
	tc = 1
	for i in range(cases):

		case = int(stdin.readline())
		A = [[] for _ in range(case+1)]
		visited = [0 for _ in range(case+1)]
		dist = [0 for _ in range(case+1)]
	
		for j in range(case):
			x,r = map(int,stdin.readline().split())
			A[x].append(r)
			
		source(case+1)
		print('Case {0}: {1}'.format(tc,m[1] ))
		m = (0,0)
		

		tc+=1

main()


	
