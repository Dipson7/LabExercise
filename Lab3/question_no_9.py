'''
WAP the checks weather a passed string is palindrome or not
'''
def palindrome(pal):
    if pal[-1:-len(pal)-1:-1] == pal:
        print('It is palindrome')
    else:
        prine('It is not palindrome')
    pal = str(input('Enter any word: '))
palindome(pal)


