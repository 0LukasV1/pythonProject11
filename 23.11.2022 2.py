# hladanie maximalny prvok v slovniku

for j in range(3):
    index_max = slov.keys()[0]
    moj_max =slov[index_max]
    for prvok in slov:
        if slov[prvok] > moj_max:
            moj_max = slov[prvok]
            index_max = prvok
    print(moj_max, index_max)
    temp = slov. pop(index_max)
