#!/usr/bin/env python3
import random


DESCRIPTION = 'What is the result of the expression?'


def game():
    random_num1 = random.randint(1, 10)
    random_num2 = random.randint(1, 10)
    sign = ["+", "-", "*"]
    random_sign = random.choice(sign)
    question = (f"{random_num1} {random_sign} {random_num2}")
    if random_sign == "+":
        int_answer = random_num1 + random_num2
        correct_answer = str(int_answer)
    elif random_sign == "-":
        int_answer = random_num1 - random_num2
        correct_answer = str(int_answer)
    elif random_sign == "*":
        int_answer = random_num1 * random_num2
        correct_answer = str(int_answer)
    return question, correct_answer
