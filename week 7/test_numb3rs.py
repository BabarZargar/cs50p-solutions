from numb3rs import validate

def test_under_255():
    assert validate("1.2.3.275") == False

def test_leading_zeroes():
    assert validate("01.2.3.4") == False

def test_string():
    assert validate("cat") == False

def test_length():

    assert validate("1.2.3.4.5") == False
    assert validate("1.2.3") == False

