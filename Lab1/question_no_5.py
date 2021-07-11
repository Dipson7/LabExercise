'''
A school decided to replace the desks in three classrooms. Each desk sits two students. Given the number of students in
each class, print the smallest possible number of desks that can be purchased. The program should read three integers:
the number of students in each of the three classes, a, b and c respectively. In the first test there are three groups.
The first group has 20 students and thus needs 10 desks. The second group has 21 students, so they can get by with no
fewer than 11 desks. 11 desks are also enough for the third group of 22 students. So, we need 32 desks in total.
'''
C1 = int(input("enter total no. of students in class 1"))
C2 = int(input("enter total no. of students in class 2"))
C3 = int(input("enter total no. of students in class 3"))
TD1 = C1//2
TD2 = C2//2
TD3 = C3//2
RS1 = C1%2
RS2 = C2%2
RS3 = C3%2
DR = TD1+TD2+TD3+RS1+RS2+RS3
print(f'total no. of desks required is {DR}')
