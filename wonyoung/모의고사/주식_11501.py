import sys
sys.stdin = open("wonyoung/input.txt", "r")
input = sys.stdin.readline

def main():
  t = int(input())
  for _ in range(t):
    n = int(input())
    days = list(map(int ,input().split()))
    
    days.reverse()
    max_day = days[0]
    answer = 0
    for i in range(1, n):
      if max_day > days[i]:
        answer += max_day- days[i]
      else:
        max_day = days[i]
    print(answer)

main()