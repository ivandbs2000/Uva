from sys import stdin
from collections import deque
G,ans,visited = list(),list(),list()

def toposort(G):
	global ans

	
	indeg = [0 for _ in range(len(G))]
	
	for u in range(len(G)):
		for v in G[u] :
			indeg[v] +=1
			
	pending = list()

	

	for u in range(len(G)):
		if indeg[u] == 0:
			pending.append(u)
	

	while len(pending) != 0:
		u = pending.pop()
		ans.append(u)
		for v in G[u]:
			indeg[v] -= 1
			if indeg[v] == 0:
				pending.append(v)

	if len(ans) == len(G):
		return True
	else:
		return False


def bfs(G,n):
	global visited
	final = 0
	queue= deque()
	queue.append(n)
	visited[n] = 1
	visited[final] = 2
	c = 0
	while len(queue)!= 0:
		u = queue.popleft()
		band = True	
		for i in G[u]:
			band = False
			if visited[i] == 0:
				queue.append(i)
				visited[i] = 1
		if band and c== 0:
			final = u
			c=1
		elif band and c==1 and u != final:
			return False

	return True



def verificar():
	global ans , visited
	for i in ans:
		if visited[i] == 0:
			if not bfs(G,i):
				return False
	return True

def main():
	global G,ans,visited

	n,m = list(map(int,stdin.readline().split()))
	while n != 0 :
		G = [[] for _ in range(n)]
		for i in range(m):
			a,b = list(map(int,stdin.readline().split()))
			G[a].append(b)
			
		visited = [0 for i in range(len(G))]
		ans = list()
		if toposort(G):
			if verificar():
				print('1')
			else:
				print('0')
		else:
			print('0')
						
		


		n,m = list(map(int,stdin.readline().split()))

main()