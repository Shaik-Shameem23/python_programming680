 #case study:32 Text-Based Invoice Data Extraction
invoice = input("Enter invoice records: ")
records = invoice.split(",")
total_amount = 0
print("\n--- Invoice Details ---")
for record in records:
    parts = record.split("-")
    if len(parts) == 3:
        code = parts[0]
        quantity = int(parts[1])
        amount = float(parts[2])
        print("Product Code:", code)
        print("Quantity:", quantity)
        print("Amount:", amount)
        total_amount = total_amount + amount
    else:
        print("Invalid invoice record:", record)
print("Total Invoice Amount:", total_amount)
