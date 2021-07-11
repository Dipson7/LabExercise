'''
WAP to sum of three given integers. However, if two values are equal sum will be zero
'''
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
c = int(input("Enter third integer: "))
if a != b != c:
    print(f'The sum of given integers is: {a+b+c} ')
else:
    print('0')