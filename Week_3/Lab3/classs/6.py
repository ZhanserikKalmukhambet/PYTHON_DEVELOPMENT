l = [int(i) for i in input().split()]

for i in range(2, int(max(l)**0.5)+2):
    l = list(filter(lambda x: (x%i!=0 or x == i) and x != 1, l))
print(l)

# 2 6 14 3 7 11 17 4 8
# max = 4 + 2 = 6





