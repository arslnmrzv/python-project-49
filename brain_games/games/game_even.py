from random import randint

def is_even(number):
    return number % 2 == 0

def main():
    DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
    question = randint(1, 100)
    if is_even(questinon):
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return question, correct_answer
