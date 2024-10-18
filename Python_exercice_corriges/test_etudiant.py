from etudiant import Etudiant

# test (12+13)/2=13 of average
def test_moy():
    assert Etudiant("Gauss",12,14).calc_moy() == 13