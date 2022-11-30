pd = {}
fz = {'a':0,'b':5,'auto':418,5:416,'c':[4,8,7]}
print(fz['auto'])
print(fz['c'][-1])

for key in fz:
    print(key)
    print(fz[key])

print(fz)
print(*fz)