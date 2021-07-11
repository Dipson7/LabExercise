'''
N students take K apples and distribute them among each other evenly. The remaining (the non divisible) part remains
in the basket. How many apples will each single student get? How many apples will remain in the basket? The program
reads the numbers N and K. It should print the two answers for the questions above.
'''
N = int(input("enter the total no. of students: "))
K = int(input("enter the total no. of apples: "))
distri = K // N
rem = K % N
print(f'Each students get {distri} apples')
print(f'{rem} apples remain in the basket')