n = int(input())
l = []
for i in range(n):
    s = input()
    if '@gmail.com' in s:
        l.append(s[:s.index('@')])
for user in l:
    print(user)