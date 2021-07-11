'''
WAP called fizz_buzz that takes that takes a number. If it is divisible by 3, it should return fizz.
If it is divisible by 5 return buzz. It it is divisible by both return fizzbuzz.
Otherwise it should return the same number.
'''
def div():
    a = int(input("Enter any number: "))
    if a/5 == a//5 and a/3 == a//3:
        print(f'fizzbuzz')
    elif a/3 == a//3:
        print(f'fizz')
    elif a/5 == a//5:
        print(f'buzz')

    else:
        print(a)

div()
        


