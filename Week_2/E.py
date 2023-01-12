l = list(map(int,input().split()))
if len(l)==1:   l.append(int(input()))
n,x,res = l[0],l[1],0
l = [x+2*i for i in range(n)]
for num in l:
    res ^= num
print(res)
