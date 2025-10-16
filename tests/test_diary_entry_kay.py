from lib.DiaryEntryKay import DiaryEntryKay
import pytest

"""
Give an empty title 
#count_words returns zero
"""
def test_errors_on_empty_title():
    with pytest.raises(Exception) as err:
        DiaryEntryKay("", "My contents")
    assert str(err.value) == "Title cannot be empty"

"""
Give an empty contents
#count_words returns zero
"""
def test_errors_on_empty_contents():
    with pytest.raises(Exception) as err:
        DiaryEntryKay("my title", "")
    assert str(err.value) == "Contents cannot be empty"


"""
Given a title and contents
#format returns a formatted entry
"My Title: These are the contents"
"""

def test_formats_with_title_and_contents():
    diary_entry = DiaryEntryKay("My Title", "These are the contents")
    result = diary_entry.format()
    assert result == "My Title: These are the contents"

"""
Given a title and contents
#count_words returns the number of words in the contents
"""

def test_count_words_with_title_and_contents():
    diary_entry = DiaryEntryKay("My Title", "These are the contents")
    result = diary_entry.count_words()
    assert result == 5

"""
Given a wpm of 2
And a text with 2 words
#reading_time returns 1 minute
"""

def test_reading_time_with_two_wpm_and_two_words():
    diary_entry = DiaryEntryKay("My Title", "One two")
    result = diary_entry.reading_time(2)
    assert result == 1

"""
Given a wpm of 2
And a text with 4 words
#reading_time returns 2 minutes
"""

def test_reading_time_with_two_wpm_and_four_words():
    diary_entry = DiaryEntryKay("My Title", "One two three four")
    result = diary_entry.reading_time(2)
    assert result == 2

"""
Given a wpm of 2
And a text with 3 words
#reading_time returns 2 minutes
"""

def test_reading_time_with_two_wpm_and_three_words():
    diary_entry = DiaryEntryKay("My Title", "One two three")
    result = diary_entry.reading_time(2)
    assert result == 2

"""
Given a wpm of 0
#reading_time Raises an error
"""
def test_reading_time_with_zero_wpm():
    diary_entry = DiaryEntryKay("My Title", "One two three")
    with pytest.raises(Exception) as err:
        diary_entry.reading_time(0)
    assert str(err.value) == "WPM must be greater than zero"

"""
Given a contents of six words
And a wpm of 2
And a minutes of 1
#reading_chunk returns first two words
"""
def test_reading_chunk_with_two_wpm_one_minute():
    diary_entry = DiaryEntryKay("My Title", "One two three four five six")
    result = diary_entry.reading_chunk(2, 1)
    assert result == "One two"

"""
Given a contents of six words
And a wpm of 2
And a minutes of 2
#reading_chunk returns first four words
"""
def test_reading_chunk_with_two_wpm_two_minutes():
    diary_entry = DiaryEntryKay("My Title", "One two three four five six")
    result = diary_entry.reading_chunk(2, 2)
    assert result == "One two three four"

"""
Given a contents of six words
And a wpm of 2 and 1 minute
First time #reading_chunk(2, 1) returns "One two"
Second time #reading_chunk(1, 1) returns "Three four"
Next time, #reading_chunk(2, 1) returns "Five six"
"""
def test_reading_chunk_called_multiple_times_with_two_wpm_one_minute():
    diary_entry = DiaryEntryKay("My Title", "One two three four five six")
    result = diary_entry.reading_chunk(2, 1)
    assert result == "One two"
    result = diary_entry.reading_chunk(1, 1)
    assert result == "Three"
    result = diary_entry.reading_chunk(2, 1)
    assert result == "Four five"

"""
Given a contents of six words
If #reading_chunk is called repeatedly
The last chunk is the last words in the text, even if shorter than could be the reading time
The next chunk after that is at the start again
"""
def test_reading_chunk_wraps_around_on_multiple_calls():
    diary_entry = DiaryEntryKay("My Title", "One two three four five six")
    result = diary_entry.reading_chunk(2, 2)
    assert result == "One two three four five six"
    result = diary_entry.reading_chunk(2, 2)
    assert result == "one two three four"
    result = diary_entry.reading_chunk(2, 2)
    assert result == "Five six"
    result = diary_entry.reading_chunk(2, 2)
    assert result == "One two three four"

"""
Given a contents of six words
If #reading_chunk is called repeatedly with an exact ending
The last chunk is the last words in the text
The next chunk after that is at the start again
"""

def test_reading_chunk_wraps_around_on_multiple_calls_with_exact_ending():
    diary_entry = DiaryEntryKay("My Title", "One two three four five six")
    result = diary_entry.reading_chunk(2, 2)
    assert result == "One two three four five six"
    result = diary_entry.reading_chunk(2, 2)
    assert result == "one two three four"
    result = diary_entry.reading_chunk(2, 1)
    assert result == "Five six"
    result = diary_entry.reading_chunk(2, 2)
    assert result == "One two three four"