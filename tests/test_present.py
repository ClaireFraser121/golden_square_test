import pytest
from lib.present import Present

'''
"""
test if content is none
"""


def test_if_contents_is_none():
    present = Present()
    with pytest.raises(Exception) as err:
        present.wrap()
    error_message = str(err.value)
    assert error_message


"""
test if there is content
"""


def test_if_is_not_none():
    present = Present()
    with pytest.raises(Exception) as err:
        present.unwrap()
    error_message = str(err.value)
    assert error_message


def test_with_no_error_message():
    present = Present()
    present.wrap("contents")
    assert "No contents have been wrapped."
'''

"""
When we wrap an item
We get it back when unwrapping
"""


def test_wrap_and_unwrap():
    present = Present()
    present.wrap(33)
    assert present.unwrap() == 33


"""
If we unwrap before wrapping
We get an error message
"""


def test_unwrap_without_wrapping():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    message = str(e.value)
    assert message == "No contents have been wrapped."

    """
    If we try to wrap an already-wrapped present
    we get an error message 
    """


def test_wrapping_already_wrapped_throws_error():
    present = Present()
    present.wrap(44)
    with pytest.raises(Exception) as e:
        present.wrap(66)
    message = str(e.value)
    assert message == "A contents has already been wrapped."


"""
If we try to wrap already-wrapped present
The first-wrapped value is unchanged
"""


def test_wrapped_already_wrapped_preserves_value():
    present = Present()
    present.wrap(44)
    with pytest.raises(Exception) as e:
        present.wrap(66)
    assert present.unwrap() == 44
