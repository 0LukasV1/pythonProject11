fr = open('data/udaje.txt','r', encoding ="utf-8")

slovnik ={}
ms = fr.read()
konriad = 0
for znak in ms:
    if znak.isupper() or znak.islower():
        slovnik[znak]= slovnik.get(znak,0) + 1
    if znak == '\n':
        konriad +=1

print(slovnik)
print(konriad)
