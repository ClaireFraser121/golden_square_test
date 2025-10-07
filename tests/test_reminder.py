import pytest  # <-- New code
from lib.reminder import Reminder


def test_reminds_the_user_to_do_a_task():
    reminder = Reminder("Claire")
    reminder.remind_me_to("Walk the dog")
    result = reminder.remind()
    assert result == "Walk the dog, Claire!"


"""
tests to see if none will remind if no reminder is set
"""


def test_no_reminder_set():
    reminder = Reminder("Claire")
    with pytest.raises(Exception) as e:  # <-- New code
        reminder.remind()
    error_message = str(e.value)  # <-- New code
    assert error_message == "No reminder set!"


"""
There are three key differences:

1. We import pytest so we can use it to check for errors.

2. We use with pytest.raises(Exception) as e: to set up a section of the code 
   where we expect an error to happen and then be caught by pytest.

3. We use str(e.value) to get the error message that was generated, and then assert 
   that it is the correct one.

"""
