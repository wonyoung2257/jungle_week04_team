import sys
sys.stdin = open("wonyoung/input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
stone = set()
for _ in range(m):
  num = int(input())
  stone.add(num)
INF = int(1e9)
# 등차수열의 합까지가 점프를 할 수 있는 최소 횟 수 이다.
# 그래서 첫항이 1이고 공차가 1인 등차 수열의 합은 (2*n)**0.5
dp = [[INF]*int(((2*n)**0.5)+2) for _ in range(n+1)]

dp[1][0] = 0

for i in range(1, n+1):
  # i가 건널 수 없는 돌일 때
  if i in stone:
    continue

  for v in range(1, int(((2*n)**0.5)+1)):
    dp[i][v] = min(dp[i-v][v-1], dp[i-v][v], dp[i-v][v+1]) +1

print(-1) if min(dp[n]) == INF else print(min(dp[n]))
