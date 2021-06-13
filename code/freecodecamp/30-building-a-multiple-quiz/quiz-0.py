from question import Question

question_prompts = [
        "What cholor are apples?\n(a) Red/Green\n(b) purple\n(c) orange\n\n", 
        "What cholor are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n", 
        "What cholor are Strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n" 
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c"),
] 

def run_test(questions):
    score = 0 
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + "Correct")

run_test(questions) 

