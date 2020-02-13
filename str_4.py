# To check wether the substring is present in the given string or not

given_str = 'rohit'
sub_str = 'n'
x = False
for i in range(len(given_str)):
    ch = given_str[i]
    if ch == sub_str:
        x = True
        break
if x == True:
    print('present')
else:
    print('not present')






