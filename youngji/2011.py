import sys

n = sys.stdin.readline().strip()

l = len(n)

alpha = [False] * (l+1)
for i in range(1,l) :
    if int(''.join(n[i-1:i+1])) <= 26 :
        alpha[i+1] = True
# print(alpha)
count = 1
dp = [0] * (l+1)
for i in range(l,1,-1) :
    if alpha[i] == True :
        dp[i] = dp[i-2] + 2
