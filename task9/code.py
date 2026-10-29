# case study:34 Campus Registration Identifier Analyzer
reg_id = input("Enter registration ID: ")
parts = reg_id.split("-")
if len(parts) == 4 and parts[0] == "BTECH":
    branch = parts[1]
    year = parts[2]
    number = parts[3]
    if year.isdigit() and number.isdigit():
        print("Valid Registration ID")
        print("Branch:", branch)
        print("Admission Year:", year)
        print("Student Number:", number)
        if branch == "CSE":
            print("Department: Computer Science")
        elif branch == "ECE":
            print("Department: Electronics")
        elif branch == "EEE":
            print("Department: Electrical")
        else:
            print("Department: Other Branch")
    else:
        print("Invalid year or student number")
else:
    print("Invalid Registration ID format")
