# -*- coding: utf-8 -*-
from __future__ import print_function
"""
Created on Sat Mar 24 09:26:31 2018

@author: jcerny
"""
import random


def is_valid_play(play):
    return play in ['rock', 'paper', 'scissors']


def random_play():
    return random.choice(['rock', 'paper', 'scissors'])


def determine_play(human, computer):
    if human == computer:
        return 'it\'s a tie!'
    elif human == 'paper' and computer == 'scissors':
        return 'computer wins'
    elif human == 'scissors' and computer == 'paper':
        return 'human wins'
    elif human == 'rock' and computer == 'scissors':
        return 'human wins'
    elif human == 'scissors' and computer == 'rock':
        return 'computer wins'
    elif human == 'rock' and computer == 'paper':
        return 'computer wins'
    elif human == 'paper' and computer == 'rock':
        return 'human wins'


def main(input_func=input):
    human = ''
    while not is_valid_play(human):
        human = input_func('RSP?')

    computer = random_play()
    print(computer)

    result = determine_play(human, computer)
    if result == 'it\'s a tie!':
        print('it\'s a tie!')
    else:
        print(result, 'wins')

if __name__ == '__main__':
    main()
