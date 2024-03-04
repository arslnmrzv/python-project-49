#!/usr/bin/env python3
from random import randint


DESCRIPTION = "What number is missing in the progression?"


def get_progression(first_num, len_num, step):
    progression = [first_num]
    for i in range(len_num):
        next_num = first_num + step
        progression.append(next_num)
        first_num = next_num
    return progression


def game():
    game_prog = get_progression(randint(0, 10), randint(5, 8), randint(2, 3))
    miss_index = randint(0, len(game_prog)-1)
    correct_answer = str(game_prog[miss_index])
    game_prog[miss_index] = ".."
    question = " ".join(map(str, game_prog))
    return question, correct_answer
