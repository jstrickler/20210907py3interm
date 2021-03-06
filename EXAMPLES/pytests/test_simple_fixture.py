#!/usr/bin/env python
from collections import namedtuple
import pytest

Person = namedtuple('Person', 'first_name last_name')  # <1>

FIRST_NAME = "Guido"
LAST_NAME = "Von Rossum"

@pytest.fixture  # <2>
def person():
    """
    Return a 'Person' named tuple with fields 'first_name' and 'last_name'
    """
    return Person(FIRST_NAME, LAST_NAME)  # <3>

NUM_INTS = 10

@pytest.fixture
def small_integers():
    return list(range(NUM_INTS))

@pytest.fixture
def animal():
    return "wombat"

def test_first_name(person, small_integers, animal):  # <4>
    assert person.first_name == FIRST_NAME

def test_last_name(person):  # <4>
    assert person.last_name == LAST_NAME

def test_len_ints(small_integers):
    assert small_integers == list(range(NUM_INTS))
