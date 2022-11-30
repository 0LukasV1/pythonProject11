fr = open('data/udaje.txt','r', encoding ="utf-8")
# mam subor a ako ho prechadzat:
# 3. sposob (ked riadky potrebujem spracovat inak)

prvy_riadok = fr.readline() #citacia hlava precita prvy s caka na
print(prvy_riadok)

druhy_riadok = fr.readline()
print(druhy_riadok)
