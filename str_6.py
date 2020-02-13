#To get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.

def both_end_string (s):
    ch1 = '  '
    ch2 = '  '
    a = len(s)
    if a > 1:
        print('Method 2 ',str( s[0:2] + s[-2:] ) )

        for i in range(2):
            ch1 += s[i]
            a -= 2
            ch2 += s[a]
            a += 3
        
        return(ch1 + ch2)
    else:
        return('empty string')

print('Method 1', both_end_string('w3scaol'))
