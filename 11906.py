from sys import stdin

board = list()
even,odd = 0,0

def dfs(h,v,M,N):
	global even,odd
	even,odd = 0,0
	stack = [(0,0)]
	c = 0
	lx = [ M , M   , M*-1 , M*-1]
	ly = [ N , N*-1, N    , N*-1]
	board[0][0] = 1
	while len(stack) != 0:
			x,y = stack.pop()
			band = True
			p = 4
			if(M == 0 or N==0):
				p = p>>1

			if(M == N):
				band = False

			for i in range(p):
				if(N==0 and i == 1):
					i = 2

				dx,dy = lx[i]+x ,ly[i] + y
					
				if 0 <= dx < v and 0 <= dy < h and board[dx][dy] != 2 :
					if board[dx][dy] != 1:
						stack.append((dx,dy))
						board[dx][dy] = 1
					c+=1
				dx,dy = ly[i]+x ,lx[i] + y
				
				if 0 <= dx < v and 0 <= dy < h and board[dx][dy] != 2 and band :
					if board[dx][dy] != 1:
						stack.append((dx,dy))
						board[dx][dy] = 1
					c+=1
			
			if c%2 == 0:
				even+=1
			else :
				odd +=1
			c = 0



def main():
	global board,even, odd

	x = int(stdin.readline())
	tc = 1
	for i in range(x):	

		t = (stdin.readline().split())	
		t = list(map(int,t))					
		board = [[0 for q in range(t[0])] for w in range(t[1])]
		c = int(input())
		for j in range(c):
			r,f = map(int,stdin.readline().split())
			board[f][r] = 2
		dfs(t[0],t[1],t[2],t[3])		
		print('Case {0}: {1} {2}'.format(tc,even,odd))
		tc+= 1
main()