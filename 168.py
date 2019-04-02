from sys import stdin


def parse_tree(line):
	
	ans = [[] for _ in range(255)]
	i = 0
	while i < len(line):
		x = ord(line[i]) - 65
		j = i + 2
		
		while j < len(line) and line[j] != ';'  and line[j] != '.':
			ans[x].append(ord(line[j])-65)
			j+=1

		i = j + 1
	
	return ans


def dfs(A,m,k,t):
	stack = list()
	visited = [0 for _ in range(len(A))]
	stack.append(m)
	cont = 1
	ans = list()
	ant = t
	while len(stack) != 0:
		x = stack.pop()
		
		i = 0
		while(i < len(A[x]) and (visited[A[x][i]] == 1 or A[x][i] == ant)):
			i+=1
		
		if len(A[x]) == i:
			ans.append('/' + chr(x+65))
			break

		if cont == k:
			visited[x] = 1
			ans.append(chr(x+65))
			cont =  1
		else:
			cont+=1

		
		stack.append(A[x][i])
		ant = x
	return ans
				

def main():
	line = stdin.readline().split()
	while line[0] != '#':
		k = int(line.pop())
		the = ord(line.pop()) - 65
		mi = ord(line.pop()) - 65
		G = parse_tree(line[0])
		ans = dfs(G,mi,k,the)
		c = 0
		for i in ans:
			if c == 0:
				print(i,end= '')	
				c = 1
			else:
				print('',i,end= '')
		print()

		line = stdin.readline().split()		

main()