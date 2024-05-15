from plates import is_valid

def test_alpha():
    assert True == is_valid('MAH11')

def test_len():
    assert True == is_valid('MAHA11')

def test_alnum():
    assert True == is_valid('MAHA11')

def test_number():
    assert True == is_valid('MAHA11')