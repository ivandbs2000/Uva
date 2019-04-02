import sys
sys.setrecursionlimit(100000)

#para completar el codigo que ya habiamos hecho en clase de tarjan me documente en https://www.geeksforgeeks.org/articulation-points-or-cut-vertices-in-a-graph/
from sys import stdin

G,low,depth,p,comps= list(),list(),list(),list(),list()


def dfs(u):
	global low,depth,p,s,G,comps
	low[u] = depth[u]
	h = 0

	for v in G[u]:

		if depth[v] == -1: 
			h+=1
			depth[v] = depth[u] + 1
			p[v] = u
			dfs(v)
			low[u]  = min(low[u],low[v])
			if p[u] == -1 and h > 1:
				comps[u][0] +=1 
			if p[u]!= -1 and low[v] >= depth[u]:
				comps[u][0] +=1

		elif v != p[u] :			
			low[u] = min(low[u],depth[v])


def solve(lo,hi):
	global comps

	if hi-lo <= 1:
		return 0

	mid = (lo+hi)>>1
	cnt = solve(lo,mid)
	cnt += solve(mid,hi)

	aux = []
	i = lo
	j = mid
	x = []

	while i < mid and j < hi:
		if comps[i][0] > comps[j][0]:
			aux.append(comps[i])
			i+=1
		else:
			if comps[i][0] == comps[j][0]:
				if comps[i][1] < comps[j][1]:
					aux.append(comps[i])
					i+=1
				else:
					aux.append(comps[j])
					j+=1
					cnt += mid -i
			else:
				aux.append(comps[j])
				j+=1
				cnt += mid -i

	while i < mid:
		aux.append(comps[i])
		i+=1

	while j < hi:
		aux.append(comps[j])
		j+=1

	comps[lo:hi] = aux
	return cnt

def main():
	global low,depth,p,s,G,comps
	
	n,m = list(map(int,stdin.readline().split()))
	
	while n!= 0:
		G = [[] for _ in range(n)]
		x,y = list(map(int,stdin.readline().split()))

		while x!= -1 and  y!= -1:
			G[x].append(y)
			G[y].append(x)
			x,y = list(map(int,stdin.readline().split()))
		
		comps =[[0,i] for i in range(len(G))]
		low = [-1 for i in range(len(G))]
		depth = [-1 for i in range(len(G))]
		p = [-1 for i in range(len(G))]

		for u in range(n):
			if depth[u] == -1:
				depth[u] = 1
				dfs(u)
		solve(0,len(G))
		con = 0
		while con < m:
			print(comps[con][1],comps[con][0]+1)
			con+=1

		print()
		n,m = list(map(int,stdin.readline().split()))


main()