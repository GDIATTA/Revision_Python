#import inc_dec    # The code to test
from mathe import Mathe

def test_attrib():
    point1 = Mathe
    assert point1.x == 0 and point1.y == 0

def test_addition():
    assert Mathe(1,2).addition() == 3

def test_subtraction():
    assert Mathe(1,2).soustraction() == -1

def test_multiplication():
    assert Mathe(1,2).multiplication()  == 2

def test_division():
    assert Mathe(1,0).division() == "Impossible to divide by zero"