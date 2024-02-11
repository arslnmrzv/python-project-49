from random import randint
from brain_games.cli import welcome_user
from brain_games.cli import name

def brain_even():
    print("Welcome to the Brain Games!")
    
    welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    questinon = randint(1, 100)
    print(f"Question: {questinon}")
    
    answer = input()
    print(f"Your answer: {answer}")

    n = 0
    while n<3:
        if questinon % 2 == 0 and answer == "yes":
            print("Correct!")
            n = n + 1
        
        elif questinon % 2 == 0 and answer == "no":
            print("'no' is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again,{name}!")
            break

        elif questinon % 2 != 0 and answer == "no":
            print("Correct!")
            n = n + 1

        elif questinon % 2 != 0 and answer == "yes":
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again,{name}!")
            break
    
    print(f"Congratuletions,{name}!")

        
    

        


