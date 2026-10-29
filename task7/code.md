##Case Study 30: Student Email and Identifier Validation
##1. Problem Statement
Develop a Python program to validate a student's email address and registration ID. The program checks whether the email contains valid basic formatting with @ and . symbols and whether the registration ID starts with BTECH.
##2. Algorithm
1. Start the program.
2. Input the student's email address.
3. Input the student's registration ID.
4. Check whether the email contains @ and ..
5. Find the positions of @ and the last ..
6. If @ is not at the beginning and . appears sufficiently after @, display “Email is valid”; otherwise, display “Email is invalid”.
7. Check whether the registration ID starts with BTECH and has at least five characters.
8. Display whether the registration ID is valid or invalid.
9. Stop the program.
##3. Flowchart (Mermaid Code)

flowchart TD
   ``` A([Start]) --> B[/Enter student email/]
    B --> C[/Enter registration ID/]
    C --> D{Email contains @ and dot?}
    D -- No --> E[Display Email is invalid]
    D -- Yes --> F[Find positions of @ and last dot]
    F --> G{At position > 0 and dot position > at position + 1?}
    G -- Yes --> H[Display Email is valid]
    G -- No --> E
    E --> I{Registration ID starts with BTECH and length >= 5?}
    H --> I
    I -- Yes --> J[Display Registration ID is valid]
    I -- No --> K[Display Registration ID is invalid]
    J --> L([Stop])
    K --> L```
4. Sample Input
Enter student email: student@gmail.com
Enter registration ID: BTECH123


5. Sample Output
Email is valid
Registration ID is valid

