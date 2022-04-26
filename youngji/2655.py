import sys

n = int(sys.stdin.readline())
a2 = [list(map(int,sys.stdin.readline().split())) for _ in range(n)] # 밑면넓이, 높이, 무게

a = sorted(a2,reverse=True)
result = [0] * (n+1)
hight = [0] * (n+1)
for i in range(n) :
    h = a[i][1]
    end_w,end_k = a[i][0],a[i][2]
    temp = [i+1]
    for j in range(n) :
        # if a[j][0] < end_w and a[j][2] < end_k :
        #     h += hight[j+1]
        
        if a[j][0] < end_w and a[j][2] < end_k :
            h += a[j][1]
            end_w,end_k = a[j][0],a[j][2]
            temp.append(j+1)
    result[i+1] = temp
    hight[i+1] = h

print(result)
print(hight)

maxi = hight.index(max(hight))
# print(maxi)

# 벽돌수, 벽돌 번호
print(len(result[maxi]))
for i in result[maxi][::-1] :
    print(i)


