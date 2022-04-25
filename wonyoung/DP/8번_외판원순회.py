import sys
sys.stdin = open("wonyoung/input.txt", "r")
N = int(sys.stdin.readline())

W = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if W[i][j] == 0:
        	# 최소비용을 구하는 문제이기 때문에 0 대신 큰값(1e9)을 설정
            W[i][j] = 1e9

# 1 << N  == 2**(n-1)-1 모든 부분집합의 개수
dp = [[1e9]*N for _ in range(1<<N)]
dp[0][0] = 0
# 0(출발) -> S(을 거쳐서) -> i(도착지)
# S : 경유지 집합
for S in range(1<<N):
	# i : 도착지
    for i in range(N):
    	# j도시 빼기
        for j in range(N):
            if S & (1<<j):
 				# 👇아래에서 설명
                dp[S][i] = min(dp[S][i], dp[S&(~(1<<j))][j] + W[j][i])
for i in dp:
  print(i)
print(dp[-1][0])
