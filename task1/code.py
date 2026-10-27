case study 3:Hospital billing and Patient classification

name = input("Enter patient name: ")
age = int(input("Enter patient age: "))

consultation = float(input("Enter consultation charge: "))
diagnostic = float(input("Enter diagnostic charge: "))
treatment = float(input("Enter treatment charge: "))

total = consultation + diagnostic + treatment

if age >= 60:
    discount = total * 0.10
else:
    discount = 0
bill = total - discount
if bill >= 5000:
    category = "High Bill"
else:
    category = "Normal Bill"
print("Patient Name:", name)
print("Total Charges:", total)
print("Discount:", discount)
print("Final Bill:", bill)
print("Patient Category:", category)
