# case study 12:Attendance Recovery Computation

attended = int(input("Enter classes attended: "))
total = int(input("Enter total classes conducted: "))

required = 75

if total == 0:
    print("Attendance cannot be calculated.")
elif attended > total or attended < 0:
    print("Invalid attendance details.")
else:
    percentage = (attended / total) * 100
    print("Current Attendance:", percentage, "%")
    if percentage >= required:
        print("You are eligible for the examination.")
        print("No extra classes are required.")
    else:
        extra = 0
        while ((attended + extra) / (total + extra)) * 100 < required:
            extra = extra + 1
        print("You are not eligible yet.")
        print("Minimum additional classes required:", extra)
        print("Total classes after recovery:", total + extra)
        print("Total attended classes:", attended + extra)
