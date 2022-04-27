from re import X
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, day = map(int,input().split())

def fibo(n):
    val = [[1,1],[1,2]]
    if n<2:
        return val[n]

    else:
        for i in range(2, n+1):
            val.append([ val[i-1][0] + val[i-2][0], val[i-1][1] + val[i-2][1] ])
        
        return val[n-3]
        
[a,b] = fibo(n)
print(a,b)
for i in range(1, day//a ):
    for j in range(1, 1000000):
        if (day - a *i) % b == 0:
            print(a)
            print(b)
            break

