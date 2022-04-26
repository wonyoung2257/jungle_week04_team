import sys

T = int(sys.stdin.readline())

for _ in range(T) :
    n = int(sys.stdin.readline())
    juga = list(map(int,sys.stdin.readline().split()))

    add = 0
    maxi = 0
    for i in range(n-1,-1,-1) :
        if juga[i] > maxi :
            maxi = juga[i]
            continue
        add += (maxi-juga[i])
    
    print(add)
