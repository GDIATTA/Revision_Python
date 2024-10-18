from account import Account

def test_account_0():
    assert Account().balance == 0

def test_getbalance():
    assert Account().get_balance() == 0

def test_depose():
    assert Account().depose(20) == 20

def test_retire():
    assert Account().retire(20) == -20

def test_interet():
    assert Account().ajout_Interet(1)   == 0