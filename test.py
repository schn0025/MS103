from pygame import*
from yapf import*
from isort import*
from flake8 import*
from bandit import*
from mypy import*
from unittest import*
from sphinx import*

def test(n):
    for i in range(n):
        print('test')
    return None
test(3)