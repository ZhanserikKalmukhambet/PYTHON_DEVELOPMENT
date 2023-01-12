# n = int(input())
# d = dict()
# for i in range(n):
#     name,pay = input().split()
#     if name in d:
#         d[name] += int(pay)
#     else:
#         d[name] = int(pay)
# maax = max(d.values())
# for key,val in sorted(d.items()):
#     print(f'{key} is lucky!') if maax==val else print(f'{key} has to receive {maax-val} tenge')

d = {
    'Dima': 2003,
    'Ajesnr': 684531
}

d.update({'Dima':654})
print(d)

for tup in sorted(d):
    print(tup)