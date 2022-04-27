##### 미완성~~~~
##인덱스 값을 탑 번호로 다 짰는데 sort()를 해줘서 인덱스가 엉망됨
# 인덱스 값도 정보 배열에 따로 저장하면 답은 나올거같은데 몰겠다요 


import sys

n = int(sys.stdin.readline())
a = [list(map(int,sys.stdin.readline().split())) for _ in range(n)] # 밑면넓이, 높이, 무게
print(a)
top = dict()
for i in range(n) :
    top[a[i][0], a[i][1], a[i][2]] = i+1
# index = top.get((a[i][0], a[i][1], a[i][2]))
# print(index)

a.sort(reverse=True)
result = [0] * (n+1)
hight = [0] * (n+1)
for i in range(n) :
    h = a[i][1]
    end_w,end_k = a[i][0],a[i][2]
    temp = [top.get((a[i][0], a[i][1], a[i][2]))]
    for j in range(i+1,n) :
        if a[j][2] < end_k :
            h += a[j][1]
            end_w,end_k = a[j][0],a[j][2]
            index = top.get((a[j][0], a[j][1], a[j][2]))
            temp.append(index)
    result[i+1] = temp
    hight[i+1] = h

# # print(result)
# # print(hight)

maxi = hight.index(max(hight))
# print(maxi)

# 벽돌수, 벽돌 번호
print(len(result[maxi]))
for i in result[maxi][::-1] :
    print(i)


