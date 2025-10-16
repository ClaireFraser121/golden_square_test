# tests/test_diary_entry_kay.py
import pytest
from lib.DiaryEntryKay import DiaryEntryKay

"""
Empty inputs should raise specific errors
"""

def test_errors_on_empty_title():
    with pytest.raises(Exception) as err:
        DiaryEntryKay("", "My contents")
    assert str(err.value) == "Title cannot be empty"

def test_errors_on_empty_contents():
    with pytest.raises(Exception) as err:
        DiaryEntryKay("my title", "")
    assert str(err.value) == "Contents cannot be empty"


"""
Formatting
"""

def test_formats_with_title_and_contents():
    diary_entry = DiaryEntryKay("My Title", "These are the contents")
    result = diary_entry.format()
    assert result == "My Title: These are the contents"


"""
Word counting (contents only)
"""

def test_count_words_with_title_and_contents():
    diary_entry = DiaryEntryKay("My Title", "These are the contents")
    result = diary_entry.count_words()
    assert result == 4


"""
Reading time (ceil division)
"""

def test_reading_time_with_two_wpm_and_two_words():
    diary_entry = DiaryEntryKay("My Title", "One two")
    assert diary_entry.reading_time(2) == 1

def test_reading_time_with_two_wpm_and_four_words():
    diary_entry = DiaryEntryKay("My Title", "One two three four")
    assert diary_entry.reading_time(2) == 2

def test_reading_time_with_two_wpm_and_three_words():
    diary_entry = DiaryEntryKay("My Title", "One two three")
    assert diary_entry.reading_time(2) == 2

def test_reading_time_with_zero_wpm_raises():
    diary_entry = DiaryEntryKay("My Title", "One two three")
    with pytest.raises(Exception) as err:
        diary_entry.reading_time(0)
    assert str(err.value) == "WPM must be greater than zero"


"""
Reading chunk (stateful; wraps to start)
"""

def test_reading_chunk_with_two_wpm_one_minute():
    diary_entry = DiaryEntryKay("My Title", "One two three four five six")
    result = diary_entry.reading_chunk(2, 1)
    assert result == "One two"

def test_reading_chunk_with_two_wpm_two_minutes():
    diary_entry = DiaryEntryKay("My Title", "One two three four five six")
    result = diary_entry.reading_chunk(2, 2)
    assert result == "One two three four"

def test_reading_chunk_called_multiple_times_with_two_wpm_one_minute():
    diary_entry = DiaryEntryKay("My Title", "One two three four five six")
    # 1st call: 2 words
    assert diary_entry.reading_chunk(2, 1) == "One two"
    # 2nd call: next 1 word
    assert diary_entry.reading_chunk(1, 1) == "three"
    # 3rd call: next 2 words
    assert diary_entry.reading_chunk(2, 1) == "four five"

def test_reading_chunk_wraps_around_on_multiple_calls():
    diary_entry = DiaryEntryKay("My Title", "One two three four five six")
    # Capacity 4 → first four words
    assert diary_entry.reading_chunk(2, 2) == "One two three four"
    # Next call returns remaining 2 words
    assert diary_entry.reading_chunk(2, 2) == "five six"
    # Next call wraps to start again
    assert diary_entry.reading_chunk(2, 2) == "One two three four"

def test_reading_chunk_wraps_around_on_multiple_calls_with_exact_ending():
    diary_entry = DiaryEntryKay("My Title", "One two three four five six")
    # 4 words, then 2 words hits the end exactly
    assert diary_entry.reading_chunk(2, 2) == "One two three four"
    assert diary_entry.reading_chunk(2, 1) == "five six"
    # Next chunk restarts at the beginning
    assert diary_entry.reading_chunk(2, 2) == "One two three four"
