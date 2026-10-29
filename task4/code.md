##Case Study 10: Campus Event Financial Planning
##1. Problem Statement
Develop a Python program to calculate the total expenses for a campus event, including venue, equipment, catering, transport, and certificate costs. Subtract the sponsorship amount from the total cost and calculate the minimum number of student registrations required to cover the remaining expenses.
##2. Algorithm
1. Start the program.
2. Input venue, equipment, catering, transport, and certificate costs.
3. Input the sponsorship amount and registration fee per student.
4. Calculate the total event expenses.
5. Subtract sponsorship from the total expenses.
6. If the remaining cost is negative, set it to zero.
7. If the registration fee is greater than zero, calculate the minimum number of registrations required, rounding up to a whole student.
8. Display total expenses, sponsorship, remaining cost, registration fee, and minimum registrations.
9. If the registration fee is zero and expenses remain, display that break-even is not possible.
10. Stop.
##3. Flowchart (Mermaid Code)
 
flowchart TD
    ```A([Start]) --> B[/Enter all event costs/]
    B --> C[/Enter sponsorship amount/]
    C --> D[/Enter registration fee per student/]
    D --> E[Calculate total expenses]
    E --> F[Remaining cost = Total expenses - Sponsorship]
    F --> G{Remaining cost < 0?}
    G -- Yes --> H[Set remaining cost to 0]
    G -- No --> I{Registration fee > 0?}
    H --> I
    I -- Yes --> J[Calculate required registrations]
    J --> K[Round up to whole student]
    K --> L[Display event budget]
    I -- No --> M[Set registrations to 0]
    M --> L
    L --> N{Fee = 0 and remaining cost > 0?}
    N -- Yes --> O[Display break-even not possible]
    N -- No --> P[End]
    O --> P```

##4. Sample Input
Enter venue cost: 10000
Enter equipment cost: 5000
Enter catering cost: 15000
Enter transport cost: 3000
Enter certificate cost: 2000
Enter sponsorship amount: 10000
Enter registration fee per student: 500


##5. Sample Output
--- Event Budget ---
Total Expenses: 35000.0
Sponsorship: 10000.0
Remaining Cost: 25000.0
Registration Fee: 500.0
Minimum Registrations: 50
