import pytest
from seasons import get_minutes


def test_wrong_format():
    with pytest.raises(SystemExit):
        get_minutes("29-04-2007")

    with pytest.raises(SystemExit):
        get_minutes("29th april 2007")
