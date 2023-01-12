open = ['(', '[', '{']
close = [')', ']', '}']
def check(s):
    l = []
    for i in s:
        if i in open:
            l.append(i)
        else:
            ind = close.index(i)
            if len(l) > 0 and open[ind] == l[len(l)-1]:
                l.pop()
            else:
                return False
    if len(l) == 0: 
        return True
    else:
        return False
s = input()
if check(s):
    print('Yes')
else:
    print('No')