from itertools import cycle, islice

l= ['m', 'n']
c= cycle(l)
r= list(islice(c, 6))
print()
print(r)
print()
