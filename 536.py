from sys import stdin

import sys
sys.setrecursionlimit(10000)
pre,ino = list(),list()
c = 0
def solve(low,hi,l):
	global c
	mid =low
	while mid < hi and pre[c] != ino[mid] :mid+=1;
	n = c

	if low < mid < hi:
		c+=1	
		solve(low,mid,l)
	
	if mid + 1 < hi:
		c+=1
		solve(mid+1,hi,l)
	l.append(pre[n])
	
	return l



def main():
	global pre,ino,c
	p = stdin.readline()
	
	while len(p) != 0:
		c = 0		
		pre,ino =p.split()
		ans = solve(0,len(pre),list())
		for i in ans:
			print(i,end = '')
		print()
		
		p = stdin.readline()


main()