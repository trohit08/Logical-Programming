str = 'The lyrics is not that poor'

n = str.find('not')
p = str.find('poor')

if p > n and n > 0 and p > 0:
    str1 = str.replace( str [ n : p+4], 'good')
    print(str1)
else :
    print(str)