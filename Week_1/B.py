def summ(s,i,res):
    if i==len(s):
        return res
    res += ord(s[i])
    return summ(s,i+1,res)

s = input()
res = 0
print('It is tasty!') if summ(s,0,res)>300 else print('Oh, no!')



