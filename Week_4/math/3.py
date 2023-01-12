from math import tan

n = int(input('Number of sides: '))
l = int(input('Length of a side: '))

apothem = l/(2*tan(180/n))
perimeter = l*n
print(0.5*apothem*perimeter)


