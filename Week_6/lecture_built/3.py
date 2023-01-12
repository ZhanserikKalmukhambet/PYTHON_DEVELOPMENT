# divmod(dividend, divisor)
x = divmod(5, 2)
print(x) # function returns a tuple containing the quotient and the remainder

################################################

x = 'print(77)'
eval(x)

################################################

x = 'name="John"\nprint(name)\nprint(100)'
exec(x)

################################################

ages = [17,18,19,55,42,37,22]
func = lambda x: x>18
party = list(filter(func,ages))
print(party)

################################################

a = format(10,'b') # binary format
b = format(255,'X') # hexadecimal format
c = format(0.5,'%')
print(a,b,c)
