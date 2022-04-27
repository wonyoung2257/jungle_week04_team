import sys
sys.stdin = open("wonyoung/input.txt", "r")
input = sys.stdin.readline

arr = list(map(str, input().strip()))

dp = [0] *len(arr)
dp[0] = 1
end = arr[0]
for i in range(1, len(arr)):
  if end=='0' and arr[i]=='0':
    print(0)
    exit(0)
  if i==1 and arr[i] != '0':
    dp[i] = 2
    end = arr[i]
  else:
    if i < len(arr)-1 and (arr[i+1] == '0' or end == '0'):
      dp[i] = dp[i-1]
      end = arr[i+1]
      continue
    temp = end+arr[i]
    if int(temp) <=26 and end !='0':
      dp[i] = dp[i-1] +dp[i-2]
    else:
      dp[i] = dp[i-1]
    end = arr[i]

# print(dp)
print((dp[-1])%1000000)