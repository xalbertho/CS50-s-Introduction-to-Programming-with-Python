import pytest
from fuel import convert,gauge

def test_0div():
    assert convert('1/4')==25 

def test_2():
    assert gauge(percentage=99)=='F'
    assert gauge(percentage=1)=='E'

def test_3():
    assert gauge(percentage=50)=='50%'

def test_4():
    with pytest.raises(ValueError):
        convert('3/1')
        convert('-1/4')
    with pytest.raises(ZeroDivisionError):
        convert('1/0')
    with pytest.raises(ValueError):
        convert('-1/4')