# case study10: Campus Event Financial Planning

venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
catering = float(input("Enter catering cost: "))
transport = float(input("Enter transport cost: "))
certificates = float(input("Enter certificate cost: "))
sponsorship = float(input("Enter sponsorship amount: "))
fee = float(input("Enter registration fee per student: "))
total_cost = venue + equipment + catering + transport + certificates
remaining_cost = total_cost - sponsorship
if remaining_cost < 0:
    remaining_cost = 0
if fee > 0:
    students = remaining_cost / fee
    # Round up to the next whole student
    students = int(students)
    if students * fee < remaining_cost:
        students = students + 1
else:
    students = 0
print("\n--- Event Budget ---")
print("Total Expenses:", total_cost)
print("Sponsorship:", sponsorship)
print("Remaining Cost:", remaining_cost)
print("Registration Fee:", fee)
print("Minimum Registrations:", students)
if fee == 0 and remaining_cost > 0:
    print("Break-even is not possible with zero registration fee.")
