from point import Point

def test_point_get():
    assert Point(1, 2).get_y() == 2 and Point(1,2).get_x() == 1


def test_point_distance():
    assert Point().distance(Point(2, 2)) == 4


def test_point_milieu():
    assert Point().milieu(Point(2, 2)).x == 1 and Point().milieu(Point(2, 2)).y == 1