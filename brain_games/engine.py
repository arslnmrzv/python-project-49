import prompt

def main(brain_game_name):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print(brain_game_name.DESCRIPTION)
    print()
    n = 0
    while n < 3:
        question = brain_game_name.game()
        correct_answer = brain_game_name.game()
        print(f"Question: {questinon}")
        answer = prompt.string("Your answer: ")
        if answer == correct_answer:
            print("Correct!")
            n += 1
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {correct_answer}.")
            print(f"Let's try again,{name}!")
            return
    print(f"Congratuletions,{name}!")
