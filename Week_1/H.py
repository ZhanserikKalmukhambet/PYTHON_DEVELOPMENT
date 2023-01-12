from readline import append_history_file


s = input()
c = input()
l = []
for i in range(len(s)):
    if s[i]==c:
        l.append(i)
print(l[0]) if len(l)==1 else print(l[0],l[-1])