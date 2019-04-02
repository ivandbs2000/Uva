from sys import stdin

r1,r2,r3 = 2*100, 3*9900 , 5*990000

def americas(x):
	if x == 0:
		return 0

	global r1,r2,r3
	d = x
	t = 0

	if d > 100:
		d-= 100
		t += r1

		if d > 9900:
			d-= 9900
			t+= r2

			if d > 990000:
				d -= 990000
				t+= r3

				if d > 0:
					t+= d*7
			else:
				t+= d*5
		else:
			t+= d*3
	else:
		t+= d*2

	return t

def consumo(x):
	if x == 0:
		return 0

	global r1,r2,r3
	d = x
	t = 0

	if d > r1:
		d-= r1
		t+= 100
		
		if d > r2:
			d-= r2
			t+= 9900
			
			if d > r3:
				d -= r3
				t+= 990000
				
				if d > 0:
					t+= d//7
					
			else:
				t+= d//5
				
		else:
			t+= d//3
			
	else:
		t+= d>>1
		

	return t



def solve(sum,diff):
	final = consumo(sum)
	low,hi = 0,final
	cm = 0
	while cm != diff:
		mid = low+((hi-low)>>1)
		cm = americas(final-mid) - americas(mid)
		if diff > cm : hi = mid
		else: low = mid

	return americas(mid)



def main():
	tsum,diff = map(int,stdin.readline().split())
	while tsum+diff!=0:	
		print(solve(tsum,diff))
		tsum,diff = map(int,stdin.readline().split())

main()

