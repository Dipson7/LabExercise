'''
WAP to take a number as parameter and check the number is prime or not.
'''
def prime(num):
    count = 0
    for i in range (2,num-1):
        if num % i == 0:
            count += 1
        if count >= 1:
            print('It is a prime number')
        num = int(input("Enter any number: "))
prime(num)



