from twttr import shorten

def test_lower():
    assert shorten("TWITTER") == "TWTTR"

def test_upper():
    assert shorten("twitter") == "twttr"

def test_number():
    assert shorten("1") == "1"

def test_punctuation():
    assert shorten(",") == ","
