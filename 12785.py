from sys import stdin

#trabajado con esteban cardona

h = 0

def kmp_prefix(s):
    n = len(s)
    P = [None]*n
    i,j = 0,-1
    P[0] = -1
    while i < n-1:
        while j> -1 and s[i] != s[j]:
            j = P[j]
        i += 1
        j += 1
        if s[i] == s[j]:
            P[i] = P[j]
        else:
            P[i] = j
    return P

def kmp_search(s1,s2):
    global h
    i = 0
    P = kmp_prefix(s1)
    while h < len(s2):
        while i > -1 and s1[i] != s2[h]:
            i = P[i]
        i += 1
        h += 1
        if i >= len(s1):
            return True
            i = P[i-1]
    return False

def solve(t, p):
    global h
    h = 0
    i = 0
    temp = ''
    band = True
    p = p.strip('\n')
    while i < len(p) and band:
        if p[i] != '*':
            temp += p[i]
        elif len(temp)>0:
            band = kmp_search(temp,t)
            temp = ''
        i+=1
    if len(temp)> 0:
        band = kmp_search(temp,t)
        temp = ''

    return band





def main():
    n = stdin.readline()
    while len(n)!= 0:
        n = int(n)
        t  = stdin.readline()
        for _ in range(n):
            l = stdin.readline()
            x = solve(t,l)
            if x:
                print("yes")
            else:
                print("no")
        n = stdin.readline()
    
main()
    
    
