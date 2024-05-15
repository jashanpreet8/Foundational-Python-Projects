from fuel import convert, gauge

def test_convert():
    assert 50 == convert('1/2')

def test_gauge():
    assert '50%' == gauge(50)