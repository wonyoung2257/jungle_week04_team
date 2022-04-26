import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
#lambda 로 sorting을 한다?
 
N = int(input())
dimension = [list(map(int, input().split())) for _ in range(N)]
dimension= [[0,0,0]] + dimension
smallest = min(dimension)
ans = []

for i in range(N+1):
    if dimension[i][0] >= smallest[0] and dimension[i][2] >= smallest[2] :
        ans.append(i)
    
# print(ans)

##area weight 가장 작은 거랑 비교하면서 리스트에 넣어주고, 작은수를 계속 갱신 