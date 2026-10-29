
# Case Study 3: Hospital Billing and Patient Classification

## 1. Problem Statement

Develop a Python program to calculate a patient's hospital bill based on consultation charges, diagnostic charges, and treatment charges. The program should accept the patient's name and age, calculate the total charges, provide a 10% discount for senior citizens aged 60 years or above, and calculate the final bill. Finally, classify the patient bill as "High Bill" if the final bill is ₹5,000 or more; otherwise, classify it as "Normal Bill".

## 2. Algorithm

1. Start.
2. Enter the patient's name.
3. Enter the patient's age.
4. Enter the consultation charge.
5. Enter the diagnostic charge.
6. Enter the treatment charge.
7. Calculate the total charges by adding consultation, diagnostic, and treatment charges.
8. Check whether the patient's age is 60 or above.
   - If yes, calculate a 10% discount on the total charges.
   - Otherwise, set the discount to zero.
9. Calculate the final bill by subtracting the discount from the total charges.
10. Check whether the final bill is greater than or equal to ₹5,000.
    - If yes, classify it as "High Bill".
    - Otherwise, classify it as "Normal Bill".
11. Display the patient's name, total charges, discount, final bill, and patient category.
12. Stop.

## 3. Flowchart

```(mermaid)
START
Enter patient name, age, and hospital charges
Calculate total charges
Consultation + Diagnostic + Treatment
Age ≥ 60?
YES
Calculate 10% discount
NO
Discount = 0
Calculate final bill
Total charges − Discount
Final bill ≥ ₹5,000?
YES
Category = High Bill
NO
Category = Normal Bill
Display patient details, charges, discount, final bill, and category
STOP
```
