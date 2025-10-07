import pytest
from lib.password_checker import PasswordChecker


"""
check if password length checker works if word too short

"""


def test_length_checker_password_to_short():
    passwordChecker = PasswordChecker()
    with pytest.raises(Exception) as e:
        passwordChecker.check("six")
    message = str(e.value)
    assert message == "Invalid password, must be 8+ characters."


"""
Checks if checker works if word correct length
"""


def test_length_checker_password_correct_length():
    passwordChecker = PasswordChecker()
    passwordChecker.check("security")
    assert passwordChecker.check
