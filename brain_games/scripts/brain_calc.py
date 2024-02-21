#!/usr/bin/env python3
import random

import prompt


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print('What is the result of the expression?')
    n = 0
    while n < 3:
        random_num1 = random.randint(1, 10)
        random_num2 = random.randint(1, 10)
        sign = ["+", "-", "*"]
        random_sign = random.choice(sign)
        if random_sign == "+":
            correct_answer = random_num1 + random_num2
        elif random_sign == "-":
            correct_answer = random_num1 - random_num2
        elif random_sign == "*":
            correct_answer = random_num1 * random_num2
        print(f"Question: {random_num1, random_sign, random_num2}")
        answer = prompt.string("Your answer: ")
        if answer == str(correct_answer):
            print("Correct!")
            n += 1
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {correct_answer}.")
            print(f"Let's try again,{name}!")
            return

    print(f"Congratuletions,{name}!")


if __name__ == '__main__':
    main()
