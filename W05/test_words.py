"""Verify that the prefix and suffix functions work correctly."""

from words import prefix, suffix
import pytest


def test_prefix():
    """Verify that the prefix function works correctly.
    Parameters: none
    Return: nothing
    """
    # pre = prefix("upbeat", "upgrade")
    # assert isinstance(pre, str), "prefix function must return a string"

    assert prefix("cat", "catalog") == "cat"
    assert prefix("", "") == ""
    assert prefix("", "correct") == ""
    assert prefix("clear", "") == ""
    assert prefix("happy", "funny") == ""
    assert prefix("cat", "catalog") == "cat"
    assert prefix("dogmatic", "dog") == "dog"
    assert prefix("jump", "joyous") == "j"
    assert prefix("upbeat", "upgrade") == "up"
    assert prefix("Disable", "dIstasteful") == "dis"


def test_suffix():
    """Verify that the suffix function works correctly.
    Parameters: none
    Return: nothing
    """
    # suff = prefix("downbeat", "downgrade")
    # assert isinstance(suff, str), "prefix function must return a string"

    assert prefix("", "") == ""
    assert prefix("", "correct") == "" 
    assert prefix("clear", "") == ""
    assert prefix("angelic", "awesome") == ""
    assert prefix("found", "profound") == "found"
    assert prefix("ditch", "itch") == "itch"
    assert prefix("happy", "funny") == "y"
    assert prefix("tired", "fatigued") == "ed"    
    assert prefix("swimming", "FLYING") == "ing"


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
