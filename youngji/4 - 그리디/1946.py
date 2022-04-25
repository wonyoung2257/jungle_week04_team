import sys

t = int(sys.stdin.readline())

for _ in range(t) :
    n = int(sys.stdin.readline())
    p = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

    p.sort()
    result = [True] * n
    for i in range(n-1) :
        if result[i] == True :
            for j in range(i+1,n) :
                if p[i][1] < p[j][1] :
                    result[j] = False

    print(result.count(True))
        
