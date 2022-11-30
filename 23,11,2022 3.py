from string import ascii_lowercase
print(ascii_lowercase)
vstup = input('zadaj mi retazec:')
poc = {}
#boc = dect()
for i in vstup:
    if i in ascii_lowercase:
        #poc[i] = poc.get(i,+0)+1
        if i in poc.keys():
            poc[i]+=1
        else:
            poc[i]=1

print(poc)