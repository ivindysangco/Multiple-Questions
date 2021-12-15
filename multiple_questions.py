# Imports the Question() class from Question_class.py
from Question_class import Question

# An array of questions
question_prompt = [
    "\n\nWhat is the color of an apple?\n(a) Red\n(b) Yellow\n(c) Orange\n",
    "\n\nWhat is the color of grapes?\n(a) Blue\n(b) Brown\n(c) Purple\n",
    "\n\nWhat is the color of orange?\n(a) Red\n(b) Orange\n(c) Brown\n"
]

# An array of object
questions = [
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "c"),
    Question(question_prompt[2], "b"),
]

# Takes all the objects from questions array
def run_test(questions):
    # Tracks the score of the user
    score = 0
    # Loop that goes through each questions array which are objects
    for question in questions:
        # The input prints the question prompt from the Question class and stores it in the variable answer
        answer = input(question.prompt)
        # The answer is compared to the answer from the Question class
        if answer == question.answer:
            score += 1
    # You have to convert all ints and floats into string to print out
    print("You got " + str(score) + "/" + str(len(questions)))

# Runs the program
run_test(questions)
