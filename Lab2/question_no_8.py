'''
Given a three digit number, find the sum of digits
'''
a = input("Enter any three digit number")
if len(a) <= 3:
    b = int(a[0]) + int(a[1]) + int(a[2])
    print(b)
else:
    print('Error')

