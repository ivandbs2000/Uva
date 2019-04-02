from sys import stdin


baj, alt = 0,0

def by(l,x):

	global baj , alt
	low = 0
	hi = len(l)

	while  low+ 1 != hi:
		mid = low+((hi-low)>>1)
		if x < l[mid] : hi = mid
		else : low = mid

	baj,alt = low,hi

		



def main():

	global baj , alt

	nA = int(stdin.readline())

	A = list(map(int,stdin.readline().split()))

	nC = int(stdin.readline())

	C = list(map(int,stdin.readline().split()))

	for i in range(nC):

		by(A,C[i])

		h = baj

		while A[h] == C[i] and h> 0:
			h-=1
		
		if h == 0 and A[h] >= C[i] :
			print("X",A[alt])

	
		elif alt == nA and A[h] != C[i]:
			print(A[h],"X")

		
		else:
			print(A[h],A[alt])

		baj,alt = 0 , 0

main()