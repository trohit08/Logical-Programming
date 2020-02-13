
def lst_of_words(words) :

    z = 0
    for a in words :
        length = len(a)

        if z < length :
            z = length
            y = a
   
   
   
    print('Longest word =' ,y , ' digit contains = ', z)
lst_of_words(['asdws','g58467956585g','hjr','juyd'])


#type 2

def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append([len(n), n])
    
    word_len.sort()
    print(word_len)
    
    print(word_len[-1][1])
    
find_longest_word(["PHP", "Exercises", "Backend","PHP"])     
