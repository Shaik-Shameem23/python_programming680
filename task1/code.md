
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

##3.flowchart
flowchart TD
``` A([Start]) --> B[/Enter patient name and age/]
    B --> C[/Enter consultation, diagnostic and treatment charges/]
    C --> D[Calculate total charges]
    D --> E{Age >= 60?}
    E -->|Yes| F[Discount = Total * 10 / 100]
    E -->|No| G[Discount = 0]
    F --> H[Calculate final bill]
    G --> H
    H --> I{Final bill >= 5000?}
    I -->|Yes| J[Category = High Bill]
    I -->|No| K[Category = Normal Bill]
    J --> L[/Display patient details and final bill/]
    K --> L
    L --> M([Stop])
```
4. Sample Input
Enter patient name: Ravi
Enter patient age: 65
Enter consultation charge: 1000
Enter diagnostic charge: 2000
Enter treatment charge: 3000


5. Sample Output
Patient Name: Ravi
Total Charges: 6000.0
Discount: 600.0
Final Bill: 5400.0
Patient Category: High Bill

