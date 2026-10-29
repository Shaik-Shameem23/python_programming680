#case study:30 Student Email and Identifier Validation
email = input("Enter student email: ")
reg_id = input("Enter registration ID: ")
# Email validation
if "@" in email and "." in email:
    at_position = email.index("@")
    dot_position = email.rfind(".")
    if at_position > 0 and dot_position > at_position + 1:
        print("Email is valid")
    else:
        print("Email is invalid")
else:
    print("Email is invalid")
# Registration ID validation
if reg_id.startswith("BTECH") and len(reg_id) >= 5:
    print("Registration ID is valid")
else:
    print("Registration ID is invalid")
