from bank import value

def test_hello():
    assert value("hello") == 0

def test_HELLO():
    assert value("HELLO") == 0

def test_h():
    assert value("hey") == 20

def test_H():
    assert value("HEY") == 20

def test_Yo():
    assert value("Yo") == 100

def test_whitespace():
    assert value(" hello") == 0

def test_hello_phrase():
    assert value("hello there") == 0




