from sys import stdin

c= 0
dat = [1024,256,64,16,4,1]

class BinTree:
	def __init__(self,num,N1=None,N2=None,N3=None,N4=None):
		self.num = num
		self.n1 = N1
		self.n2 = N2
		self.n3 = N3
		self.n4 = N4
		return
	#preorden
	def __str__(self):
		str_n1 = str(self.n1) if self.n1!= None else ''
		str_n2 = str(self.n2) if self.n2!= None else ''
		str_n3 = str(self.n3) if self.n3!= None else ''
		str_n4 = str(self.n4) if self.n3!= None else ''
		s = '{} ({}) ({}) ({}) ({})'.format(self.num,str_n1,str_n2,str_n3,str_n4)
		return s



def parse_tree(inp):
	global c
	c+=1

	if inp[c]== 'e':
		return 0

	elif inp[c] == 'f':
		return 2

	else:
		return BinTree(1,parse_tree(inp),parse_tree(inp),parse_tree(inp),parse_tree(inp))


def solve(a,b,l):
	global dat
	
	if type(a) == int and type(b) == int:
		if a == 2 or b == 2:
			return dat[l]
		else:
			return 0

	elif type(a) == int:
		if a == 2:
			return dat[l]
		else:
			return cal(b,l)

	elif type(b) == int:
		if b == 2:
			return dat[l]
		else:
			return cal(a,l)

	else:
		return (solve(a.n1,b.n1,l+1)+solve(a.n2,b.n2,l+1) +solve(a.n3,b.n3,l+1) +solve(a.n4,b.n4,l+1))


def cal(a,l):
	global dat

	if type(a)!= int:
		return (cal(a.n1,l+1)+cal(a.n2,l+1)+cal(a.n3,l+1)+cal(a.n4,l+1))
	
	if a == 2:
		return dat[l]

	else:
		return 0



#z = BinTree(1,0,2,2,0)
#z = BinTree(1,BinTree(1,0,0,0,2),BinTree(1,2,2,0,0),2,0)
#h = BinTree(1,0,2,0,BinTree(1,0,0,2,0))
#print(solve(z,h,0))
#print(cal(z,0))



def main():
	global c
	n = int(stdin.readline())

	for i in range(n):

		x = stdin.readline()
		c = -1
		x = parse_tree(x)
		y = stdin.readline()
		c = -1
		y = parse_tree(y)
		num = solve(x,y,0)
		print("There are {0} black pixels.".format(num))

main()