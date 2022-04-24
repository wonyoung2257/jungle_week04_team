import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


for i in range(0,int(input())):
    Cnt = 1
    N = int(input())
    spec = [list(map(int,input().split())) for _ in range(N)]

    spec.sort() # 서류 기준 오름차순 정렬
    Max = spec[0][1]
    
    for i in range(1,N):
        if Max > spec[i][1]:
            Cnt += 1
            Max = spec[i][1]

    print(Cnt)