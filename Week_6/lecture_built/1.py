# The all() function returns True if all items in an iterable are true, otherwise it returns False.

list = [True, True, True]
print(all(list))

tuple = (0,1,1,1,0)
print(all(tuple))

##########################################

# The any() function returns True if any item in an iterable are true, otherwise it returns False.

list2 = (1,0,0,0)
print(any(list2))

###########################################

x = int(input())
bin_version = bin(x)
print(bin_version[2:])

###########################################

list3 = [1,15,20]
print(bool(list3)) # true 
list4 = []
print(bool(list4)) # false, because it is empty
