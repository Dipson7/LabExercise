'''
To input weight in kg/lbs and convert it to kg/lbs
'''
unit = input("Enter unit (kg/lbs): ").lower()
weight = int(input("Enter your weight: "))
if unit == 'kg':
    converted_weight = weight * 2.20462
    print(f"Your weight is {converted_weight} lbs.")
elif unit == "lbs":
    converted_weight = weight * 0.453592
    print(f"Your weight is {converted_weight} kg.")
else:
    print("Error! Use either 'kg' or 'lbs' as unit")