from plates import is_valid

def test_isntalnum():
    assert is_valid("PI3.14") == False

def test_isalnm():
    assert is_valid("CS50") == True

def test_zero_first():
    assert is_valid("CS05") == False

def test_al():
    assert is_valid("CS") == True

def test_al_again():
    assert is_valid("CS50P") == False

def test_too_small():
    assert is_valid("C") == False

def test_too_big():
    assert is_valid("VERYBIG") == False

def test_start_letter():
    assert is_valid("50") == False

