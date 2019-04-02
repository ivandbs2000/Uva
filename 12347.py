from sys import stdin
import sys
sys.setrecursionlimit(10000)
B = list()

def solve(low,hi,l):
	global B
	mid =low + 1
	while mid < hi and B[low] >= B[mid] :mid+=1
	if low+1 < mid:
		solve(low+1,mid,l)
	if mid < hi:
		solve(mid,hi,l)
	l.append(B[low])
				
	return l



def main():

	global B
	n = stdin.readline()
	while len(n) != 0:
		
		n = int(n)
		B.append(n)
		n = stdin.readline()
	x= solve(0,len(B),list())
	for i in x:
		print(i)

main()