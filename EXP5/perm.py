from itertools import permutations

s = '190'
p = list(permutations(s))
print()
for x in p:
    print(''.join(x))
print()
