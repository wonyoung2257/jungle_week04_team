import sys
sys.stdin = open("wonyoung/input.txt", "r")
input = sys.stdin.readline

day, cake = map(int, input().split())

dp = [0,{'x':1, 'y':0}, {'x': 0, 'y':1}]

for i in range(3, day+1):
  dp.append({'x':dp[i-2]['x']+dp[i-1]['x'], 'y':dp[i-2]['y'] + dp[i-1]['y']})

day1 = 1
while True:
  if (cake - day1*dp[-1]['x']) % dp[-1]['y'] == 0:
    break
  day1+=1
day2 = int((cake - day1*dp[-1]['x']) / dp[-1]['y'])

print(day1)
print(day2)