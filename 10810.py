import sys
sys.setrecursionlimit(1000000)
from sys import stdin

MAX   = 50010
num   = [ None for i in range(MAX) ]

def solve(lo,hi):
    global num

    if(hi-lo <= 1):
        return 0
    #divir

    mid = (lo+hi)>>1
    cnt = solve(lo,mid)
    cnt += solve(mid,hi)

    #combinar
    aux = []
    i = lo
    j = mid

    while(i < mid and j < hi):

        if(num[i] <= num[j]):
            aux.append(num[i])
            i+=1

        else:
            aux.append(num[j])
            j+=1
            cnt += mid -i

    while(i < mid):
        aux.append(num[i])
        i+=1

    while(j < hi):
        aux.append(num[j])
        j+=1
    num[lo:hi] = aux
    return cnt


def main():
    global num
    inp = stdin
    n = int(stdin.readline().strip())
    while n>0:
        for i in range(n):
            num[i] = int(stdin.readline())
        print(solve(0,n))
        n = int(stdin.readline().strip())

main()


