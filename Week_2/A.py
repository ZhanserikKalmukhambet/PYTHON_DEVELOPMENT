list = [int(i) for i in input().split()]
ind = 0
last = len(list)-1
for i in range(len(list)):
    if i > ind:
        print(0)
        break
    if list[i] + i > ind:
        ind = list[i]+i
    if ind >= last:
        print(1)
        break
