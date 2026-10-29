#case study:5 Mobile Plan Cost Comparison
usage = float(input("Enter monthly data usage in GB: "))
# Plan A
if usage <= 2:
    cost_a = 199
else:
    cost_a = 199 + (usage - 2) * 20
# Plan B
if usage <= 5:
    cost_b = 299
else:
    cost_b = 299 + (usage - 5) * 15
# Plan C
if usage <= 10:
    cost_c = 399
else:
    cost_c = 399 + (usage - 10) * 10
print("\n--- Plan Costs ---")
print("Plan A:", cost_a)
print("Plan B:", cost_b)
print("Plan C:", cost_c)
if cost_a <= cost_b and cost_a <= cost_c:
    print("Cheapest Plan: Plan A")
elif cost_b <= cost_a and cost_b <= cost_c:
    print("Cheapest Plan: Plan B")
else:
    print("Cheapest Plan: Plan C")
