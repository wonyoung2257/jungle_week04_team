import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 다음 숫자와 비교했을 떄 작으면, 리스트에 담는다
# 그 다음 숫자도 비교했을 때 작으면, 리스트에 담는다
# 그 다음 숫자가 줄어들면 , 그 전 숫자에 판다 
# 그 다음 숫자가 증가하면 줄어든 숫자도 산다
#사는 경우: 다음 숫자가 클 떄 무조건 산다
# 파는 경우: 가장 큰 숫자이면서도 index가 뒤에 있을 떄 
# 안 사는 경우: 그 다음 숫자들이 낮은 가격일 때 
for _ in range(int(input())):
    N = int(input())
    stock= list(map(int, input().split()))
    stock = [0] + stock
    li = [0] * (N+1)
    count = 0
    ans = []
    for i in range(N-1):
        if stock[i] <= stock[i+1] and stock[i+1] <= stock[i+2]:
            count += stock[i] + stock[i+1]
        if stock[i] > stock[i+1]:
        if stock[i] == max(stock):
            print(0)
        if stock[i] > stock[i+1] or i == N:
            gain = (stock[i] * i )- count  
            count = 0  
    ans.append(gain)
    print(ans)