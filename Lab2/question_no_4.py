'''
Enter three integers, print the smallest one
'''
a = int(input("Enter any number"))
b = int(input("Enter any number"))
c = int(input("Enter any number"))
if a<=b and a<=c:
    print (f"{a} is the smallest number")
elif b<=a and b<=c:
    print (f"{b} is the smallest number")
else:
    print (f"{c} is the smallest number")