from sys import stdin

def solve(target):
	
	md,nd = 1 , 0			
	mi,ni = 0 , 1	
	m,n = 1,1
	x,y = target[0],target[1]	
	t = ''
	while(m != x or, n != y):
		if( x*n < m*y):
			md,nd = m,n
			m += mi
			n+= ni 
			t += 'L'

		if( x*n > m*y):
		
			mi,ni = m,n
			m += md
			n+= nd
			t+= 'R'

	return t

def main():
  target = [int(x) for x in stdin.readline().strip().split()]

  while target[0]!=1 or target[1]!=1:
    print(solve(target))
    target = [int(x) for x in stdin.readline().strip().split()]

main()