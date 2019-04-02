from sys import stdin

M = list()
visited = list()

df = [-1, 0, 0,1]
dc = [0,-1, 1, 0]

def dfs(posX,posY,siz,num):
	global M, visited ,df , dc

	stack = [(posX,posY)]
	visited[posX][posY] = 1
	c = 1
	
	while len(stack) != 0 :

		x,y = stack.pop()
		
		for i in range(4):

			dx,dy = x + df[i], y + dc[i]

			if 0 <= dx < siz and 0 <= dy < siz and M[dx][dy] == num and visited[dx][dy] == 0 :

				stack.append((dx,dy))
				visited[dx][dy] = 1
				c+=1

	if c == siz :
		return True
	else:
		return False


def solve(siz):
	global M,visited
	
	for i in range(siz):
	
		for j in range(siz):

			if visited[i][j] == 0 :
				b = dfs(i,j,siz,M[i][j])
				if not b :
					return False

	return True 


def main():

	global M, visited

	c = int(stdin.readline())
	i = 0

	while c!= 0:

		M = [[0 for i in range(c)] for i in range(c)]
		visited = [[0 for i in range(c)] for i in range(c)]

		while i < c-1:

			temp = list(map(int,stdin.readline().split()))

			for j in range(0,c*2,2):
				M[temp[j] -1][ temp[j+1] - 1] = i + 1
			
			i+=1
		
		
		if solve(c) :
			print("good")
		else:
			print("wrong")

		c = int(stdin.readline())
		i = 0
	

main()


