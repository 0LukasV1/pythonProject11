import random
zoz: []
for i in range(10):
    zoz.append(random.randrange(0,100))

#vzbrat nahodny prvok
index = random.randrange(0,10)
print(zoz[index])

#vdaka random
print(random.choice(zoz))

print(zoz)
nov_zoz = sorted(zoz)
print(nov_zoz)
