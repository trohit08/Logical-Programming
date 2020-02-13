#to get a single string from two given strings, separated by a space and swap the first two characters of each string
str = 'abc ' , 'xyz '

strx = str[0][0] + str[1][1:]
stra = str[1][0] + str[0][1:]

print(strx+"        "+stra)