from um import count

def test_boundary_cases():
    assert count("um blah blah um") == 2

def test_uppercase():
    assert count("UM") == 1

def test_punctuation():
    assert count("um,") == 1

def test_words():
    assert count("album") == 0
