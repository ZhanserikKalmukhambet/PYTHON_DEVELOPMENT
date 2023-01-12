n,f = map(int,input().split())
IsPrime = False
for i in range(2,n):
    if n%i==0:
        IsPrime = True
        break
if IsPrime==0 and n<=500 and f%2==0:
    print('Good job!')
else:
    print('Try next time!')

def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n,f = map(int,input().split())
if is_prime(n) and n<=500 and f%2==0:
    print('Good Job!')
else:
    print('Try next time!')
