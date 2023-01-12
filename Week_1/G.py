def convert(num):
    cnt = 0
    res = 0
    while num != 0:
        res += 2**cnt * (num%10)
        cnt += 1
        num //= 10
    return res
    
n = int(input())
print(convert(n))