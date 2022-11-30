# hladanie maximalny prvok v slovniku

for j in range(3):
    index_max = list(slov.keys())[0]
    print(index_max)
    moj_max=slov[index_max]
    for prvok in slov:
        if slov[prvok] > moj_max:
            moj_max = slov[prvok]
            index_max = prvok
    print(moj_max, index_max)
    
