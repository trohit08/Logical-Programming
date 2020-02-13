#To get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself
print('Type 1')
def change_str(str):
    str = str.upper()
    ch = ""
    a = str[1:]
  
    for i in range(len(a)) :
        if str[0] == a[i]:
            ch = ch + '$'
        else:
            ch = ch + a[i]
    ch = str[0] + ch    
    return (ch)
   # print(ch)
print(change_str('return'))
print(change_str('alpha'))
print(change_str('Araund'))
print(change_str('AROUSEA'))


print('Type 2')

def change_char(str1):
    char = str1[0]
    str1 = str1.replace(char, '$')
    str1 = char + str1[1:]

    return str1

print(change_char('restart'))
