#!/usr/bin/env python3
from random import randint
import prompt


def is_even(number):
    return number % 2 == 0


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    n = 0
    while n < 3:
        questinon = randint(1, 100)
        print(f"Question: {questinon}")

        if is_even(questinon):
            correct_answer = "yes"
        else:
            correct_answer = "no"

        answer = prompt.string("Your answer: ")

        if answer == correct_answer:
            print("Correct!")
            n += 1
        else:
            print("'no' is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again,{name}!")
            return

    print(f"Congratuletions,{name}!")


if __name__ == '__main__':
    main()
