import sys
import os

# Append the directory of calculator.py to sys.path
sys.path.append(os.path.abspath('../'))

from calculator import add, subtract


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(3, 2) == 1
