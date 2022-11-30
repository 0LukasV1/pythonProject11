def findmaximum(index:int)->int:
    max_value = zoz[index]
    max_index = index
    for i in range(index,len(zoz)):
        if zoz[i]>max_value:
            max_value= zoz[i]
            max_index= 1
    return max_index

print(*zoz)

for i in range(len(zoz)):
    max_index = findmaximum(i)
    zoz[i],zoz[max_index]= zoz[max_index],zoz[i]
