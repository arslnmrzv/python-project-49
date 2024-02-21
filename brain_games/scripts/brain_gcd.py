#!/usr/bin/env python3
from random import randint
import prompt


def gcd(num1, num2):
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print('Find the greatest common divisor of given numbers.')
    n = 0
    while n < 3:
        random_num1 = randint(0, 100)
        random_num2 = randint(0, 100)
        print(f"Question: {random_num1} {random_num2}")
        answer = prompt.string("Your answer: ")

        if answer == gcd(random_num1, random_num2):
            print("Correct!")
            n += 1
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {gcd(random_num1, random_num2)}.")
            print(f"Let's try again,{name}!")
            return
    print(f"Congratuletions,{name}!")


if __name__ == '__main__':
    main()
