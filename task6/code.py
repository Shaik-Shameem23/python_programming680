#case study:2 Laboratory Chemical Inventory Validation
n = int(input("Enter number of chemicals: "))
names = []
categories = []
quantities = []
# Read chemical details
for i in range(n):
    print("\nChemical", i + 1)
    name = input("Enter chemical name: ")
    category = input("Enter storage category (Acid/Base/Neutral): ")
    quantity = float(input("Enter quantity: "))
    names.append(name)
    categories.append(category)
    quantities.append(quantity)
print("\n--- Inventory Validation ---")
# Validate each chemical
for i in range(n):
    print("\nChemical:", names[i])
    if categories[i] not in ["Acid", "Base", "Neutral"]:
        print("Invalid storage category")
    elif quantities[i] < 0:
        print("Invalid quantity")
    elif quantities[i] > 50:
        print("Quantity exceeds maximum limit")
    else:
        print("Chemical record is valid")
# Check compatibility
acid_found = False
base_found = False
for i in range(n):
    if categories[i] == "Acid":
        acid_found = True
    if categories[i] == "Base":
        base_found = True
if acid_found and base_found:
    print("\nWarning: Acid and Base categories are incompatible.")
else:
    print("\nNo incompatible categories detected.")
