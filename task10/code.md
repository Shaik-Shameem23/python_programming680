##Case Study 32: Text-Based Invoice Data Extraction

##1. Problem Statement
Develop a Python program to extract product codes, quantities, and amounts from text-based invoice records. The program separates the records using commas and extracts individual details using hyphens. It validates the record format, displays valid invoice details, and calculates the total invoice amount.

##2. Algorithm
1. Start the program.
2. Input invoice records as a single string.
3. Split the records using commas.
4. Initialize the total invoice amount to zero.
5. Read each invoice record one by one.
6. Split each record using hyphens.
7. If the record contains three parts, extract the product code, quantity, and amount.
8. Display the extracted details and add the amount to the total.
9. If the record format is invalid, display an error message.
10. Display the total invoice amount.
11. Stop the program.
    
##3. Flowchart (Mermaid Code)
```(mermaid)
flowchart TD
    A([Start]) --> B[/Enter invoice records/]
    B --> C[Split records using commas]
    C --> D[Set total amount = 0]
    D --> E[Read next invoice record]
    E --> F[Split record using hyphens]
    F --> G{Number of parts = 3?}
    G -- Yes --> H[Extract code quantity and amount]
    H --> I[Display product details]
    I --> J[Add amount to total]
    G -- No --> K[Display invalid invoice record]
    J --> L{More records?}
    K --> L
    L -- Yes --> E
    L -- No --> M[Display total invoice amount]
    M --> N([Stop])```


5. Sample Input
Enter invoice records: P101-2-500,P102-3-750,P103-1-200


6. Sample Output
--- Invoice Details ---
Product Code: P101
Quantity: 2
Amount: 500.0
Product Code: P102
Quantity: 3
Amount: 750.0
Product Code: P103
Quantity: 1
Amount: 200.0
Total Invoice Amount: 1450.0


