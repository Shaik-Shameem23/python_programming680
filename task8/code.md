##Case Study 34: Examination Answer Evaluation
##1. Problem Statement
Develop a Python program to evaluate a student's examination answers by comparing them with a predefined answer key. The program counts correct, wrong, and unanswered questions and calculates the final score by awarding 1 mark for each correct answer and deducting 0.25 marks for each wrong answer.
##2. Algorithm
1. Start the program.
2. Store the correct answers in a list called key.
3. Initialize correct, wrong, and unanswered to zero.
4. Repeat for each question in the answer key.
5. Input the student's answer and convert it to uppercase.
6. If the answer is empty, increase the unanswered count.
7. If the answer matches the key, increase the correct count.
8. Otherwise, increase the wrong count.
9. Calculate the final score by subtracting 0.25 for each wrong answer from the marks earned for correct answers.
10. Display the correct answers, wrong answers, unanswered questions, and final score.
11. Stop the program.
##3. Flowchart (Mermaid Code)

flowchart TD
  ```  A([Start]) --> B[Initialize answer key and counters]
    B --> C[/Enter answer for each question/]
    C --> D[Convert answer to uppercase]
    D --> E{Answer is empty?}
    E -- Yes --> F[Increase unanswered count]
    E -- No --> G{Answer matches key?}
    G -- Yes --> H[Increase correct count]
    G -- No --> I[Increase wrong count]
    F --> J{More questions?}
    H --> J
    I --> J
    J -- Yes --> C
    J -- No --> K[Calculate final score]
    K --> L[Display examination results]
    L --> M([Stop])```
##4. Sample Input
In this example, the student answers three questions correctly, one incorrectly, and leaves one unanswered.
Enter answer for question 1: A
Enter answer for question 2: B
Enter answer for question 3: A
Enter answer for question 4: D
Enter answer for question 5:


##5. Sample Output
--- Examination Result ---
Correct Answers: 3
Wrong Answers: 1
Unanswered: 1
Final Score: 2.75

