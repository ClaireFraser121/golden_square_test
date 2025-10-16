from lib.DiaryEntry import DiaryEntry

"""
See if content is parsing into the list
"""

def test_title_and_content():
    diary_entry = DiaryEntry("Title", "These are the contents")
    result = diary_entry.format()
    assert result == "Title\n\nThese are the contents"

"""
Test word count functionality
"""

def test_word_count_fuctionality():
    diary_entry = DiaryEntry("Title", "These are the contents")
    diary_entry.count_words()
    assert 5

"""
test word per minute reading time functionality
"""
def test_wpm_reading_time_functionality_zero_words():
    diary_entry = DiaryEntry("T", "")
    assert diary_entry.count_words() == 0
    assert diary_entry.reading_time(200) == 0 # 0 words need 0 minutes

"""
test word per minute reading time functionality
"""
def test_wpm_reading_time_functionality_hello_world():
    diary_entry = DiaryEntry("T", "hello world")
    assert diary_entry.count_words() == 2
    assert diary_entry.reading_time(1) == 2 # 2/1 -> 2
    assert diary_entry.reading_time(3) == 1 # 2/3 -> 0.6666 -> 1
 
"""
test word per minute reading time functionality
"""
def test_wpm_reading_time_functionality_201_words():
    diary_entry = DiaryEntry("T", "a " * 201) # 201 words
    assert diary_entry.reading_time(201) == 1 # 1.005 -> ceil -> 2
    
    
