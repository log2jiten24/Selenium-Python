import pytest

def test_01():
    a = 3
    b = 4
    assert a + 1 == b, 'a and b value not matching'
    assert  a == b,'test failed a is not eqaul to b '

def tes_02 ():
    str = 'selenium'
    assert  str.upper() == 'SELENIUM'

def test_03():
    assert  True

def test_04():
    assert False

def test_05():
    assert  100 == 100

def test_06():
    list = ['Java' , 'Selenium' , 'Python']
    #fail assertion message
    assert 'Zalenium'  in list ,'Zalenium not present '

