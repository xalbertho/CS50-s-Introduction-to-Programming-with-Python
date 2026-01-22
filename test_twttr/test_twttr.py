from twttr import shorten

def test_lowercase():
    assert shorten('hola')=='hl'
def test_uppercase():
    assert shorten('HOLA')== 'HL'
def test_mixed():
    assert shorten('Enterprise')=='ntrprs'
def test_numbers():
    assert shorten('CS50')=='CS50'
def test_punctuation():
    assert shorten("Hello, world!") == "Hll, wrld!"