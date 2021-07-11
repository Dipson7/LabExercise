'''
WAP to find the max of three numbers
'''
def max():
    a = int(input("Enter any number: "))
    b = int(input("Enter any number: "))
    c = int(input("Enter any number: "))
    if a > b and a > c:
        print (f'{a} is the max of three')
    elif b > a and b > c:
        print (f'{b} is the max of three')
    elif c > b and c > a:
        print(f'{c} is the max of three')
max()
