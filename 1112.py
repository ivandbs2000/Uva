from sys import stdin
from heapq import heappop,heappush

INF = float('inf')

def dijkstra(G,e):
	ans = [INF for _ in G]
	ans[e] = 0
	visited = [False for _ in G]
	heap = [ (0,e) ]
	while len(heap)!=0:
		d,u = heappop(heap)
		if visited[u] == False:
			for v,dv in G[u]:
				if d+dv <= ans[v]:
					ans[v] = d+dv
					heappush(heap,(ans[v],v))
					
			visited[u] = True

	return ans


def solve(G,e,t):
	R = [list() for _ in range(len(G))]
	for u in  range(len(G)) :
		for v,dv in G[u]:
			R[v].append((u,dv))

	
	c = 0
	ans = dijkstra(R,e)
	for i in range(len(ans)):
		if ans[i] <= t:
			c+=1

	return c




def main():
	
	cases = int(stdin.readline())
	b = 0
	for _ in range(cases) :
		
		ignore = stdin.readline()
		n = int(stdin.readline())
		e = int(stdin.readline())
		t = int(stdin.readline())
		m = int(stdin.readline())

		G = [list() for _ in range(n)]

		for _ in range(m):
			u,v,d = map(int,stdin.readline().split())
			G[u-1].append((v-1,d))

		
		if b>=1:
			print()

		else:
			b = 1		

		print(solve(G,e-1,t))





main()