from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

"""Make prime check"""
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False
    return True

"""Ask question and give answer"""
def game():
    question = randint(0, 100)
    if is_prime(question):
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return question, correct_answer
