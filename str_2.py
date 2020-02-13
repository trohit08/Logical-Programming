# D_strings

s = 'ArobinDo'

new_str = ' '

for i in range(len(s)) :
    if i % 2 == 0 :
        ch = s[i]
        c = ch.upper()
        new_str += c
    else :
        ch = s[i]
        c = ch.lower()
        new_str += c
print(new_str)

