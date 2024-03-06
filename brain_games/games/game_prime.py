#!/usr/bin/env python3
from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
        return True


def game():
    question = randint(0, 100)
    if is_prime(question):
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return question, correct_answer
