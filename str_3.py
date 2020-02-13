# Count the number of characters in a string in a form of dictionary.

def char_frequency(str1):
    dict = {}
    for n in str1:
        k = dict.keys()
        
        if n in k:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('aajkll112'))