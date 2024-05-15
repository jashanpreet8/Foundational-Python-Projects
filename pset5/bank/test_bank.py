from bank import value

def test_hello():
    assert 0 == value('hello')

def test_h():
    assert 20 == value('howdy')

def test_else():
    assert 100 == value('whats up')