import random


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(num1, num2):
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)


def game():
    random_num1 = random.randint(0, 100)
    random_num2 = random.randint(0, 100)
    question = (f"{random_num1} {random_num2}")
    right_answer = gcd(random_num1, random_num2)
    correct_answer = str(right_answer)
    return question, correct_answer
