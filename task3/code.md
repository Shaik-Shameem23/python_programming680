##Case Study 2: Progressive Electricity Billing

##1. Problem Statement
Develop a Python program to calculate electricity bills based on the units consumed using different billing slabs. The program should add fixed charges, apply a surcharge or rebate, compare monthly bills, and identify unusual increases in electricity bills.

##2. Algorithm
1. Start the program.
2. Define a function to calculate the electricity bill.
3. If units are less than or equal to 100, charge Rs. 2 per unit.
4. If units are between 101 and 200, calculate charges using Rs. 2 for the first 100 units and Rs. 3 for the remaining units.
5. If units exceed 200, charge Rs. 5 for units above 200.
6. Add Rs. 50 as a fixed charge.
7. If the amount exceeds Rs. 1,000, add a 5% surcharge.
8. If the amount is below Rs. 500, subtract Rs. 50 as a rebate.
9. Enter the number of months and electricity units consumed each month.
10. Calculate and store each monthly bill.
11. Compare consecutive monthly bills and identify increases above 25%.
12. Display the bills and comparison results.
13. Stop.

##3. Flowchart (Mermaid Code)

flowchart TD
    ```A([Start]) --> B[Define calculate_bill function]
    B --> C[/Enter number of months/]
    C --> D[Initialize bills list]
    D --> E[/Enter units consumed for each month/]
    E --> F{Units <= 100?}
    F -- Yes --> G[Amount = units * 2]
    F -- No --> H{Units <= 200?}
    H -- Yes --> I[Amount = 200 + units minus 100 * 3]
    H -- No --> J[Amount = 500 + units minus 200 * 5]
    G --> K[Add fixed charge Rs. 50]
    I --> K
    J --> K
    K --> L{Amount > 1000?}
    L -- Yes --> M[Add 5 percent surcharge]
    L -- No --> N{Amount < 500?}
    M --> N
    N -- Yes --> O[Subtract Rs. 50 rebate]
    N -- No --> P[Return bill]
    O --> P
    P --> Q[Store and display monthly bill]
    Q --> R{More months?}
    R -- Yes --> E
    R -- No --> S[Compare consecutive monthly bills]
    S --> T{Bill increased?}
    T -- Yes --> U[Calculate percentage increase]
    U --> V{Increase > 25 percent?}
    V -- Yes --> W[Display unusual increase]
    V -- No --> X[Display normal increase]
    T -- No --> Y[Display decrease or unchanged]
    W --> Z([Stop])
    X --> Z
    Y --> Z```
##4.Sample input
    Enter number of months: 3

Month 1
Enter electricity units consumed: 80

Month 2
Enter electricity units consumed: 150

Month 3
Enter electricity units consumed: 250

##5.Sample output
Month 1
Electricity Bill: Rs. 160

Month 2
Electricity Bill: Rs. 450

Month 3
Electricity Bill: Rs. 925

--- Monthly Bill Comparison ---
Month 1 : Rs. 160
Month 2 : Rs. 450
Increase: Rs. 290
Unusual increase detected!
Month 3 : Rs. 925
Increase: Rs. 475
Unusual increase detected!
