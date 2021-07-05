'''
WAP that accepts string and calculate the number of upper case and lower case letters.
'''
def UPPERLOWER(sentence):
    u = 0
    l = 0
    for i in sentence:
        if i >= 'A' and i <= 'Z':
            u += 1
        elif i >= 'a' and i <= 'z':
            l += 1
    print(f"Uppercase: " + str(u))
    print(f"Lowercase: " + str(l))
UPPERLOWER(sentence)




