#Given string is pure alphabet or not

s = input('Enter your sentence to check whether it is pure string or not ::')
count_al = 0
count_oth = 0
for i in range(len(s)):
    ch = s[i]
    if ch >= 'A' and ch <= 'Z' or ch >= 'a' and ch <= 'z'  or ch == ' ':
        count_al += 1
    else :
        count_oth += 1
       
if count_al == len(s):
    print ('Your entered sentence is pure string')
else :
    print('Your entered sentence is not a pure string')

