import prompt


def engine(brain_game_name):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print(brain_game_name.DESCRIPTION)
    n = 0
    while n < 3:
        question, correct_answer = brain_game_name.game()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")
        if answer == correct_answer:
            print("Correct!")
            n += 1
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {correct_answer}.")  # noqa: E501
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
