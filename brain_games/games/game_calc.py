import random


DESCRIPTION = 'What is the result of the expression?'


def calc(num1, num2, sig):
    if sig == "+":
        int_answer = num1 + num2
        return int_answer
    elif sig == "-":
        int_answer = num1 - num2
        return int_answer
    elif sig == "*":
        int_answer = num1 * num2
        return int_answer


def game():
    random_num1 = random.randint(1, 10)
    random_num2 = random.randint(1, 10)
    sign = ["+", "-", "*"]
    random_sign = random.choice(sign)
    question = (f"{random_num1} {random_sign} {random_num2}")
    correct_answer = str(calc(random_num1, random_num2, random_sign))
    return question, correct_answer
