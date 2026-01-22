from plates import is_valid

def test_0():
    assert is_valid('hol0')==False

def test_baplha():
    assert is_valid('89')==False
    assert is_valid('ISVA9')==True

def test_len():
    assert is_valid('abcdefg')==False
    assert is_valid('a')==False

def test_numbers():
    assert is_valid('abcd23')==True
    assert is_valid('ab87a')== False


def test_bal():
    assert is_valid('AB$/')== False

#def test_