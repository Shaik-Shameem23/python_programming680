##Case Study 5: Mobile Plan Cost Comparison
##1. Problem Statement
Develop a Python program to compare the monthly costs of three mobile data plans based on the user's data usage in GB. Calculate the cost of each plan, including additional data charges, and display the cheapest plan.
##2. Algorithm
1. Start the program.
2. Input the monthly data usage in GB.
3. Calculate Plan A cost: Rs. 199 for up to 2 GB and Rs. 20 for each additional GB.
4. Calculate Plan B cost: Rs. 299 for up to 5 GB and Rs. 15 for each additional GB.
5. Calculate Plan C cost: Rs. 399 for up to 10 GB and Rs. 10 for each additional GB.
6. Display the costs of all three plans.
7. Compare the three costs.
8. Display the cheapest mobile plan.
9. Stop the program.
##3. Flowchart (Mermaid Code)
 
flowchart TD
   ``` A([Start]) --> B[/Enter monthly data usage in GB/]
    B --> C{Usage <= 2?}
    C -- Yes --> D[Plan A = 199]
    C -- No --> E[Plan A = 199 + extra GB * 20]
    D --> F{Usage <= 5?}
    E --> F
    F -- Yes --> G[Plan B = 299]
    F -- No --> H[Plan B = 299 + extra GB * 15]
    G --> I{Usage <= 10?}
    H --> I
    I -- Yes --> J[Plan C = 399]
    I -- No --> K[Plan C = 399 + extra GB * 10]
    J --> L[Display all plan costs]
    K --> L
    L --> M{Plan A cheapest?}
    M -- Yes --> N[Display Plan A]
    M -- No --> O{Plan B cheapest?}
    O -- Yes --> P[Display Plan B]
    O -- No --> Q[Display Plan C]
    N --> R([Stop])
    P --> R
    Q --> R```

##4. Sample Input
Enter monthly data usage in GB: 6


##5. Sample Output
--- Plan Costs ---
Plan A: 279.0
Plan B: 314.0
Plan C: 399
Cheapest Plan: Plan A

