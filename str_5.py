# Count vowels and consonents

s = 'aaakkk11'
s = s.lower()
vowels = 'aeiou'
vou = 0

for w in s:
    for i in range(len(vowels)):
        ch = vowels[i]
        if w == ch:
            vou += 1

cons = len(s) - vou
print("vowels = ",vou)
print("consonents = ",cons)


