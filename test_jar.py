from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar = Jar(5)
    assert jar.capacity == 5

    try:
        Jar(-1)
        assert False
    except ValueError:
        assert True


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(5)
    jar.deposit(3)
    assert jar.size == 3

    try:
        jar.deposit(3)   # exceeds capacity
        assert False
    except ValueError:
        assert True


def test_withdraw():
    jar = Jar(5)
    jar.deposit(3)
    jar.withdraw(2)
    assert jar.size == 1

    try:
        jar.withdraw(5)   # too much
        assert False
    except ValueError:
        assert True
