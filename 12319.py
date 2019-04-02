from sys import stdin

INF = float('inf')

def frod(g):

	for k in range(len(g)):
		for i in range(len(g)):
			for j in range(len(g)):
				if g[i][j] > g[i][k] + g[k][j]:
					g[i][j] = g[i][k] + g[k][j]


def solve(g1,g2,a,b):
	frod(g1)
	frod(g2)
	for i in range(len(g1)):
		for j in range(len(g1)):
			if g2[i][j] > a*(g1[i][j]) + b: 
				return False

	return True

def main():
	n = int(stdin.readline())
	while n != 0:
		GA = list()
		GS = list()
		for k in range(n):
			t = list()
			for h in range(n):
				if k == h:
					t.append(0)
				else:
					t.append(INF)

			GA.append(t)
			GS.append(t.copy())

		for i in range(n):
			line = list(map(int,stdin.readline().split()))
			c = 1
			while c < len(line):
				GA[line[0]-1][line[c]-1] = 1
				c+=1

		for j in range(n):
			line = list(map(int,stdin.readline().split()))
			c = 1
			while c < len(line):
				GS[line[0]-1][line[c]-1] = 1
				c+=1
		A,B = map(int,stdin.readline().split())
		band = solve(GA,GS,A,B)
		if band:
			print("Yes")
		else:
			print("No")
		n = int(stdin.readline())

main()