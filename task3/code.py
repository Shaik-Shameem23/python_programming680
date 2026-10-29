#case study 2: Progressive Electricity Billing

def calculate_bill(units):
    if units <= 100:
        amount = units * 2
    elif units <= 200:
        amount = (100 * 2) + (units - 100) * 3
    else:
        amount = (100 * 2) + (100 * 3) + (units - 200) * 5
    amount = amount + 50
    if amount > 1000:
        amount = amount + (amount * 0.05)
    if amount < 500:
        amount = amount - 50

    return amount
n = int(input("Enter number of months: "))
bills = []
for i in range(n):
    print("\nMonth", i + 1)
    units = int(input("Enter electricity units consumed: "))
    bill = calculate_bill(units)
    bills.append(bill)
    print("Electricity Bill: Rs.", round(bill, 2))

print("\n--- Monthly Bill Comparison ---")

for i in range(n):
    print("Month", i + 1, ": Rs.", round(bills[i], 2))
    if i > 0:
        increase = bills[i] - bills[i - 1]
        if increase > 0:
            percentage = (increase / bills[i - 1]) * 100
            print("Increase: Rs.", round(increase, 2))
            if percentage > 25:
                print("Unusual increase detected!")
        elif increase < 0:
            print("Bill decreased by Rs.", round(abs(increase), 2))
        else:
            print("Bill is unchanged.")
