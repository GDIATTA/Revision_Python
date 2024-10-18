from rectangle_1 import Rectangle_1

def test_rectangle_0():
    assert Rectangle_1(1,2).a == 1 and Rectangle_1(1,2).b == 2

def test_rectangle_1():
    assert Rectangle_1(1,2).get_a() == 1 and Rectangle_1(1,2).get_b() == 2

def test_rectangle_2():
    assert Rectangle_1(1,2).perimetre() == 6

def test_rectangle_3():
    assert Rectangle_1(1,2,).surface() == 2