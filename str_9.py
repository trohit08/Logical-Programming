#To add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
def change_ing(str):
    a = 'ing'

    if str[-3:] == a:
        print(str+'ly')
    else :
        print(str+a)


change_ing(str)