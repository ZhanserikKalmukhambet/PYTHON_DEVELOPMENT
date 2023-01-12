n = int(input())
d = dict()
for i in range(n):
    name,weak = input().split()
    if weak in d:
        d[weak] += 1
    else:
        d[weak] = 1

m = int(input())
d2 = dict()
for i in range(m):
    name,force,cnt = input().split()
    if force in d2:
        d2[force] += int(cnt)
    else:
        d2[force] = int(cnt)

res = 0
for dem in d:
    if not dem in d2:
        res += d[dem]
    else:
        if d[dem] - d2[dem] > 0:
            res += d[dem] - d2[dem]
print(f'Demons left: {res}')



