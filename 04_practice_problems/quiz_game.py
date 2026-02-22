# Python quiz game using list and tuple

questions = (
    "1. What is the correct file extension for Python files?: ",
    "2. Which of the following data types is immutable in Python?: ",
    "3. What is the output of the following code? print(type(5 // 2)): ",
    "4. How is a code block indicated in Python?: ",
    "5. What is the correct way to declare a dictionary in Python?: "
)

options = (
    ("A. '.python'", "B. '.py'", "C. '.pl'", "D. '.p'"),
    ("A. list", "B. set", "C. tuple", "D. dict"),
    ("A. <class: 'float'>", "B. <class: 'int'>", "C. <class: 'double'>", "D. <class: 'number'>"),
    ("A. Curly braces", "B. Parenthesis", "C. Indentation", "D. Square brackets"),
    ("A. d = ['a': 1, 'b': 2]", "B. d = {'a': 1, 'b': 2}", "C. d = ('a': 1, 'b': 2)", "D. d = <'a': 1, 'b': 2>")
)

answers = ("B", "C", "B", "C", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C ,D): ").upper()
    guesses.append(guess)
    if guess not in ["A","B","C","D"]:
        print("invalid option")
    elif guess == answers[question_num]:
        score += 1
        print("Correct!!")
    else:
        print("Incoreect!!")
        print(f"{answers[question_num]} is the correct answer...")

    question_num += 1



print("--------------------------")
print("          Results         ")
print("--------------------------")

print("answers: ",end="")
for ans in answers:
    print(ans, end="")
print()

print("guesses: ",end="")
for guess in guesses:
    print(guess, end="")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")