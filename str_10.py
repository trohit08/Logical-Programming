
'''def inkblot(str):
    n=0
    
    for a in str:
        if a >= 'a' and a <= 'z' or a >= 'A' and a <= 'Z':
            vary = a
            print(vary)
            

    for s in str.split():
        if s.isdigit() == True:
            s1 = int(s)
            n = n - s1
    #n1 = str(n) 
    print(n) 

    print(str.replace('x ',str(n)))
    

inkblot('x + 2 = 5')  '''

def abc(str):
    splt = str.split()
    print(splt)
    if splt[0] == 'x':
        result = int(splt[-1]) - int(splt[2])
        splt[0] = result
    elif splt[2] == 'x':
        result = int(splt[-1]) - int(splt[0])
        splt[2] = result
    elif splt[-1] == 'x':
        result = int(splt[0]) + int(splt[2])
        splt[-1] = result

    return splt
print(abc("1 = 3 + x"))

