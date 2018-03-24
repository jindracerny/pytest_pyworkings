# -*- coding: utf-
import subprocess
import sys

import pytest

import pytest_pyworkings


def test_rock_is_valid_play():
    assert pytest_pyworkings.is_valid_play('rock') is True


def test_paper_is_valid_play():
    assert pytest_pyworkings.is_valid_play('paper') is True


def test_scissors_is_valid_play():
    assert pytest_pyworkings.is_valid_play('scissors') is True


def test_nuzky_is_invalid_play():
    assert pytest_pyworkings.is_valid_play('kamen') is False


def test_random_play():
    for _ in range(100):
        play = pytest_pyworkings.random_play()
        assert pytest_pyworkings.is_valid_play(play)


def test_random_play_is_fairish():
    """randomness check"""
    plays = [pytest_pyworkings.random_play() for _ in range(1000)]
    assert plays.count('rock') > 100
    assert plays.count('paper') > 100
    assert plays.count('scissors') > 100


def test_determine_play():
    assert pytest_pyworkings.determine_play('paper', 'scissors') == 'computer wins'
    assert pytest_pyworkings.determine_play('scissors', 'paper') == 'human wins'


def input_fake(fake):
    """function that returns a function"""
    def input_fake_(prompt):
        """fake input"""
        print(prompt)
        return fake
    return input_fake_


@pytest.mark.parametrize('play', ['rock', 'paper', 'scissors'])
def test_whole_game(capsys, play):
    pytest_pyworkings.main(input_func=input_fake(play))
    out, err = capsys.readouterr()
    assert 'RSP?' in out
    assert ('computer wins' in out or
            'human wins' in out or
            'it\'s a tie!' in out)


def test_in_subprocess():
    completed_process = subprocess.run([sys.executable, 'pytest_pyworkings.py'],
                                       input=b'qwerty\nrock',
                                       stdout=subprocess.PIPE)
    stdout = completed_process.stdout.decode('utf-8')
    assert stdout.count('RSP?') == 2
