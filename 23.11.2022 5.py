#aby je zoznam ktory je naplneny nahodnymi stringami, vytvorte novy zoznam ktory bude obsahovat

def fun(list):
    sam= 'eyuioa'
    x = 0
    for i in range (0, len(list)):
        for j in range(len(i)):
            if j in sam:
                x+=1
                print(x)

list(['jano', 'jozo'])