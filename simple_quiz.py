questions = {
    "What is the capital of Palestine?": "Jerusalem",
    "How many days in February?": "28",
    "What the historical top scorer of the FIFA World Cup?": "Messi",
    "What is the longest river in the world?": "Nile",
    "What is the tallest mountain in the world?": "Everest",
    "(True or False) Is Messi bigger than Ronaldo?": "False",
    "(True or False) You can lead a cow down stairs but not up stairs.": "False",
    "(True or False) Approximately one quarter of human bones are in the feet.": "True",
    '(True or False) Google was originally called "Backrub".': "True",
    "(True or False) In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.": "True",
}

score = 0

for question, answer in questions.items():
    user_answer = input(f"{question} ")
    if user_answer.strip().lower() == answer.strip().lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong!! The answer is {answer}")

print(f"Result => You have got {score} out of {len(questions)}")
