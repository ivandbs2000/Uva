from sys import stdin

def suffix(s):
    n = len(s)
    suffixes = [(s[i:],i) for i in range(n)] #O(n̈́2)
    suffixes.sort()
    suffixarr = [i for w,i in suffixes]
    return suffixarr


def suffix_arr(s): #O(n * log2(n))
    l = list(set(s))
    l.sort()
    n = len(s)
    d = {l[i]:i for i in range(len(l))}
    next_level = [d[s[i]] for i in range(n)]
    #lvl1 = [lvl0[i]*(n+1) + (1+lvl0[i+1] if i+1<n else 0) for i in range(n)]
    N = 2*n
    k = 1
    while N > 0:
        next_level  = [next_level[i]*(n+1) +(1+next_level[i+k] if i+k<n else 0)
                       for i in range(n)]
        
        l = list(set(next_level))
        l.sort()
        d = {l[i]:i for i in range(len(l))}
        next_level = [d[next_level[i]] for i in range(n)]
        N //=2
        k *= 2
        
    return next_level


def suffix_arr_util(s):
    n = len(s)
    last_level = suffix_arr(s)
    SA = [None]*n
    for i in range(n):
        SA[last_level[i]] = i
    return SA


def inv_permutation(l):
	inv = [0] * len(l)
	for i,j in enumerate(l):
		inv[j] = i
	return inv

def l_c_p(s,sa,pos = None):
	n = len(s)
	if pos == None:
		pos = [x+1 for x in inv_permutation(sa)]
	k = 0
	lcp = [0]*n
	for i in range(n):
		if pos[i] ==n:
			continue
		j = sa[pos[i]]
		top = n - max(i,j)
		while k < top and s[i+k] == s[j+k]:
			k+=1
		lcp[pos[i]] = k
		if k: k-=1
	lcp[0] = n - sa[0]
	return lcp

def maxi(lcp,sa,l1,final):
	m = 0
	ans = {}
	for i in range(len(lcp)):
		if lcp[i]>m:
			a,d = sa[i],sa[i-1]
			if a < l1 and d > l1:
				ans = {}
				ans[final[a:a+lcp[i]]] = 0
				m = lcp[i]
			elif a>l1 and d < l1:
				ans = {}
				ans[final[a:a+lcp[i]]] = 0
				m = lcp[i]

		elif lcp[i] != 0 and lcp[i]== m:
			a,d = sa[i],sa[i-1]
			if a < l1 and d > l1:
				ans[final[a:a+lcp[i]]] = 0
			elif a>l1 and d < l1:
				ans[final[a:a+lcp[i]]] = 0

	return ans

def solve(final,l1):
	sa = suffix_arr_util(final)
	lcp = l_c_p(final,sa)
	lcp[0] = -1
	m = maxi(lcp,sa,l1,final)
	return m

def convert(l):
	ans = list()
	for i in l:
		ans.append(i)
	return ans
def main():
	line  = stdin.readline()
	c = 0
	while len(line)!= 0:
		line2 = stdin.readline()
		if c != 0:
			print()

		line = line.strip('\n')
		line2 = line2.strip('\n')
		final = line + '$' + line2
		ans = solve(final,len(line))
		if len(ans) == 0:
			print("No common sequence.")
		elif len(ans) == 1:
			ans = convert(ans)
			print(ans[0])
		else:
			ans = convert(ans)
			ans.sort()
			for i in ans:
				print(i)
		c+=1
		paso = stdin.readline()
		line  = stdin.readline()

main()