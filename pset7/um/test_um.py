from um import count

def test_1():
    assert 1 == count('Hello, um')

def test_2():
    assert 2 == count('Hello, um, world, um')

def test_3():
    assert 3 == count('Hello, um, um, um')