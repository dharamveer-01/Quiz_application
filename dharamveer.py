class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer.lower() == question.answer.lower():
            score += 1
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer was: {question.answer}\n")
    print(f"You got {score} out of {len(questions)} correct!")


def main():
    question_prompts = [
        "1. What is the capital of France?\n(a) London\n(b) Paris\n(c) Rome\n\n",
        "2. What is 2 + 2?\n(a) 3\n(b) 4\n(c) 5\n\n",
        "3. What is the largest planet in our solar system?\n(a) Earth\n(b) Jupiter\n(c) Mars\n\n",
        "4. Who wrote 'Hamlet'?\n(a) Charles Dickens\n(b) William Shakespeare\n(c) Mark Twain\n\n",
        "5. What is the chemical symbol for water?\n(a) H2O\n(b) O2\n(c) CO2\n\n"
    ]

    questions = [
        Question(question_prompts[0], "b"),
        Question(question_prompts[1], "b"),
        Question(question_prompts[2], "b"),
        Question(question_prompts[3], "b"),
        Question(question_prompts[4], "a"),
    ]

    run_quiz(questions)


if __name__ == "__main__":
    main()