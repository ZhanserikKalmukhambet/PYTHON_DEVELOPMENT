# def sum(a:int,b:int) -> float:
#    return float(a + b)

# c = sum(7,8)
# print(c)

####################################################
# def square(n):
#    global res
#    res = n*n
#    return res

# n = int(input())
# print(square(n))
# res += 100
# print(res)

#####################################################

# def fun(*args):
#    print(args)

# fun(7,'Jones','Kazakh',77,True,{'Name':'Jones'})

#####################################################

# def fun(a,b,c,*strings: str):
#    print(a,b,c)
#    print(strings)

# fun(7,55,88,'kazakh','kbtu','programmer','salam')

######################################################

# def fun(id,name,age,hobby):
#    print(name,age,id,hobby)

# fun(name='Jones',age='17',hobby='program',id='21B30108')

#######################################################

# def fun(id,name,**kwargs):
#    print(id)
#    print(name)
#    print(kwargs)

#    for key,val in kwargs.items():
#       print(f'{key}-->{val}')
# fun(id='21B01308',name='Ronaldo', gpa=3.86,age=20,course=1)

#########################################################

def sum(a,b=10):
   return a + b

print(sum(7,7)) # by default it takes a value from there

##########################################################

# from math import sqrt
# l1 = list(map(int,input().split()))
# l2 = list(map(sqrt,l1))
# l3 = list(map(lambda x:x*2,l2))
# print(l1,l2,l3)

###########################################################

# l = list(map(int,input().split()))

# even = list(filter(lambda x: x%2==0, l))
# odd = list(filter(lambda x: x%2!=0, l))
# print(even,odd)

###########################################################

# 