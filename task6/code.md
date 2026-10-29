##Case Study 2: Laboratory Chemical Inventory Validation
##1. Problem Statement
Develop a Python program to validate laboratory chemical inventory records. The program accepts chemical names, storage categories, and quantities. It checks whether the category is valid, whether the quantity is within the permitted limit, and displays a warning if both Acid and Base categories are present.
##2. Algorithm
1. Start the program.
2. Input the number of chemicals.
3. Create three lists to store chemical names, categories, and quantities.
4. Read the details of each chemical and store them in the lists.
5. Check each chemical's storage category.
6. If the category is invalid, display an error message.
7. If the quantity is negative, display an invalid quantity message.
8. If the quantity exceeds 50, display a maximum limit warning.
9. Otherwise, display that the chemical record is valid.
10. Check whether both Acid and Base categories are present.
11. If both are present, display an incompatibility warning.
12. Otherwise, display that no incompatible categories were detected.
13. Stop the program.
##3. Flowchart (Mermaid Code)

flowchart TD
    ```A([Start]) --> B[/Enter number of chemicals/]
    B --> C[Create names categories and quantities lists]
    C --> D[/Input chemical details/]
    D --> E[Store details in lists]
    E --> F{More chemicals?}
    F -- Yes --> D
    F -- No --> G[Validate each chemical]
    G --> H{Category valid?}
    H -- No --> I[Display invalid category]
    H -- Yes --> J{Quantity < 0?}
    J -- Yes --> K[Display invalid quantity]
    J -- No --> L{Quantity > 50?}
    L -- Yes --> M[Display maximum limit warning]
    L -- No --> N[Display record is valid]
    I --> O{More records to validate?}
    K --> O
    M --> O
    N --> O
    O -- Yes --> G
    O -- No --> P[Check for Acid and Base categories]
    P --> Q{Both categories present?}
    Q -- Yes --> R[Display incompatibility warning]
    Q -- No --> S[Display no incompatibility detected]
    R --> T([Stop])
    S --> T```


##4. Sample Input
   Enter number of chemicals:3
   
Chemical 1
Enter chemical name: Hydrochloric Acid
Enter storage category (Acid/Base/Neutral): Acid
Enter quantity: 20

Chemical 2
Enter chemical name: Sodium Hydroxide
Enter storage category (Acid/Base/Neutral): Base
Enter quantity: 30

Chemical 3
Enter chemical name: Water
Enter storage category (Acid/Base/Neutral): Neutral
Enter quantity: 10


##5. Sample Output
--- Inventory Validation ---

Chemical: Hydrochloric Acid
Chemical record is valid

Chemical: Sodium Hydroxide
Chemical record is valid

Chemical: Water
Chemical record is valid

Warning: Acid and Base categories are incompatible.









Do you like this personality?
