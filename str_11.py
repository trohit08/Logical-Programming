 #fibonacci

def is_part_of_series(lst):
    a = 0
    b = 1
    #f = lst
    
    if lst == 0:
        print(lst)
    elif lst <= 0:
        print('Enter positive number')
    elif lst == 1:
        print(lst)
    else:
        print(a,b, sep='\n')
        for i in range(1,lst-1):
            c = a + b
            print(c)
            a = b
            b = c
        
        
is_part_of_series(6)   


