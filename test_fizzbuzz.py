from fb import fizzbuzz
import pytest


def test_fizzbuzz_returns_str():
    assert isinstance(fizzbuzz(1), str)


@pytest.mark.parametrize('num', [1, 2, 4, 7, 8, 11, 13, 14])
def test_fizzbuzz_non_mod3_non_mod5_returns_self(num):
    assert fizzbuzz(num) == str(num)


@pytest.mark.parametrize('num', [3, 6, 9, 12])
def test_fizzbuzz_3_returns_fizz(num):
    assert fizzbuzz(num) == 'fizz'


@pytest.mark.parametrize('num', [5, 10])
def test_fizzbuzz_5_returns_buzz(num):
    assert fizzbuzz(num) == 'buzz'

@pytest.mark.parametrize('num', [0, 15, 30, 45, 75, 135])
def test_fizzbuzz_15_returns_fizzbuzz(num):
    assert fizzbuzz(num) == 'fizzbuzz'
