n = int(input())
arr = []
for i in range(n):
    l = ['.']*n
    arr.append(l)
for i in range(n):
    for j in range(n):
        if n%2==0 and i>=j:
            arr[i][j] = '#'
        elif n%2!=0 and i+j>=n-1:
            arr[i][j] = '#'
            
for l in arr:
    for char in l:
        print(char,end='')
    print()
