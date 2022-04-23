li = input().split('-')
num = []
for i in li:
    ans = 0
    s = i.split('+')
    for j in s:
        ans += int(j)
    num.append(ans)
n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)