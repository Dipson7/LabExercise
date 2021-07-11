'''
Check wheather the given year is leap year or not.If yes print 'Leap year' else print 'Common year'
'''
a=int(input("Enter a year: "))
if a % 4 == 0 and a % 100 != 0:
    print('leap year')
else:
    print('common year')
