from personne import Personne
from student import Student

def test_personne():
    assert Personne.firstname == "Gauss"

def test_student():
    assert  Student.firstname == "Gauss"

