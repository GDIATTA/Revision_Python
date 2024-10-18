from carre import Carre
from Point import Point

def test_point():
    assert Point(1,2).x == 1

def test_carre():
    assert Carre(20,10,1,0).x == 1 and Carre(20,10,1,0).y == 0