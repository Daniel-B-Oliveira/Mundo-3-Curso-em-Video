v = (1, 2, 3, 4, 5, 6, 7, 8, 9)
b = (9, 8, 7, 6, 5, 4, 3, 2, 1)
# del b
h = v + b

print(sorted(h))
print(h.index(1))
print(h.index(1, h.index(1)+1))
print(h[h.index(1)], h[h.index(1, h.index(1)+1)])

print(v[:(len(v))])
print(v[::2])
print(sorted(v))
for c in v:
    print(c, end='')
print('')

for c in range(0, len(v)):
    print(v[c], end='')
print('')

for ps, nm in enumerate(v):
    print(f'{nm}-{ps}-', end='')
print('fim')

# /         /           /           /           /           /

p = 0

'''while p < len(v):
    if int(v[p]) % 2 != 0:
        print(v[p], end='')
    p += 1'''
