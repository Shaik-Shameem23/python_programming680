#case study:34 Examination Answer Evaluation

key = ["A", "B", "C", "D", "A"]
correct = 0
wrong = 0
unanswered = 0
for i in range(len(key)):
    answer = input("Enter answer for question " + str(i + 1) + ": ")
    answer = answer.upper()
    if answer == "":
        unanswered = unanswered + 1
    elif answer == key[i]:
        correct = correct + 1
    else:
        wrong = wrong + 1
score = (correct * 1) - (wrong * 0.25)
print("\n--- Examination Result ---")
print("Correct Answers:", correct)
print("Wrong Answers:", wrong)
print("Unanswered:", unanswered)
print("Final Score:", score)
