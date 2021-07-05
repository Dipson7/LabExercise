'''
 WAP which accepts marks of four subjects and display total marks, percentage and grade. Hint: more than
 70% –> distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail
'''
a = int(input("enter marks in Maths"))
b = int(input("enter marks in Physics"))
c = int(input("enter marks in Chemistry"))
d = int(input("enter marks in Biology"))
m = a+b+c+d
tm = 400
p = (m/tm)*100
if p > 70:
    grade = "Your grade is Distinction"
elif (70 >= p) and (p > 60):
    grade = "Your grade is First Division"
elif (60 >= p) and (p > 40):
    grade = "You pass"
else:
    grade = "Nice try noob you Failed"
print (f"Total Marks is {m}")
print (f"Percentage is {p}%")
print (f"{grade}")

