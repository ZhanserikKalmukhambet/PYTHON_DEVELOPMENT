x,y = map(int,input().split())
n = int(input())
arr = []
for i in range(n):
    l = tuple(map(int,input().split()))
    arr.append(l)

closest = lambda l: (l[0]-x)**2 + (l[1]-y)**2
arr.sort(key=closest)
for l in arr:
    for num in l:
        print(num,end=' ')
    print()

